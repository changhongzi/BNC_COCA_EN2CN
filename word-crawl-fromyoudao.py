import requests
import csv
import time
import json
import os


# 解析coca文件
def parse_csv(file_path):
    result = []

    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        header = next(reader)  # 读取并跳过标题行

        for row in reader:
            word = row[1]
            related_forms = row[2].split(', ')
            total_frequency = row[3]
            word_list = row[0]

            for form in related_forms:
                form_parts = form.split(' (')
                form_word = form_parts[0]
                form_frequency = form_parts[1].replace(')', '')

                result.append({
                    'Word': form_word,
                    'Headword': word,
                    'frequency': form_frequency,
                    'List': word_list
                })

    return result


# 返回单个单词的coca信息
def single_word_bnccoca(file_path,word):
    data=parsed_data = parse_csv(file_path)
    for data in parsed_data:
        if data['Word'] == word:
            return data
    return {}


# 查询有道词典单词释义
def word_explanation(data):
    word = data['Word']
    headword = data['Headword']
    frequency= data['frequency']
    list =  data['List']



    url = 'https://dict.youdao.com/jsonapi_s'
    headers = {
    }
    params = {
        'doctype': 'json',
        'jsonversion': 4,
        'q': word,
        'le': 'en',
        't': 6,
        'client': 'web',
        'sign': 'aba9d04a3a92d29f9db12998535dd555',
        'keyfrom': 'webdict'
    }

    try:
        response = requests.get(url, headers=headers, params=params)
        data = response.json()

        word_prototype = data['ec']['word'].get('prototype', word) if 'ec' in data and 'word' in data['ec'] else word
        us_phone = data['ec']['word'].get('usphone', '') if 'ec' in data and 'word' in data['ec'] else ''
        uk_phone = data['ec']['word'].get('ukphone', '') if 'ec' in data and 'word' in data['ec'] else ''

        translations = [tr['tran'] for tr in data['ec']['word']['trs']] if 'ec' in data and 'word' in data['ec'] and 'trs' in data['ec']['word'] else []
        phrs = [{'headword': phr['headword'], 'translation': phr['translation']} for phr in data['phrs']['phrs']] if 'phrs' in data and 'phrs' in data['phrs'] else []
        sentences = [{'sentence': sp['sentence'], 'translation': sp['sentence-translation']} for sp in data['blng_sents_part']['sentence-pair']] if 'blng_sents_part' in data and 'sentence-pair' in data['blng_sents_part'] else []


        return {
            'word': word,
            'headword':headword,
            'frequency':frequency,
            'list':list,
            'usPhone': us_phone,
            'ukPhone': uk_phone,
            'translations': translations,
            'phrs': phrs,
            'sentences': sentences
        }

    except Exception as e:
        print("发生错误:", str(e))
        append_text_to_file('error-words.txt',word)
        return None


# 追加文件
def append_text_to_file(file_path, text):
    try:
        with open(file_path, 'a') as file:
            file.write(f"{text}\n")
    except IOError:
        print(f"{file_path} write error.")


# 写数据到文件
def write_text_to_file(file_path, text):
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(text)
        print(f"{file_path} has written。")
    except IOError:
        print(f"{file_path} write error.")

# 判断文件是否存在
def check_file_exists(file_path):
    if os.path.exists(file_path):
        print(f"{file_path} has exits.")
        return True
    else:
        print(f"{file_path} has not  exits.")
        return False


def test1():
    # 调用函数并打印结果
    file_path = 'BNC_COCA_lists.csv'  # 替换为实际的CSV文件路径
    parsed_data = parse_csv(file_path)
    for i in range(2):
        data = parsed_data[i]
        result = word_explanation(data)
        jsonData=json.dumps(result, ensure_ascii=False)
        write_text_to_file(f"data/{data['Word']}.json",jsonData);


# 主入口
def main():
    file_path = 'BNC_COCA_lists.csv' 
    parsed_data = parse_csv(file_path)
    for data in parsed_data:
        print(f"\nWill build {data['Word']} ...")
        dict_path=f"data/{data['Word']}.json"
        if check_file_exists(dict_path) == False:
            result = word_explanation(data)
            jsonData=json.dumps(result, ensure_ascii=False)
            write_text_to_file(dict_path,jsonData);
            # time.sleep(1/10) 

main()