# 说明
可能是简中网网最全的英语词库，基于COCA构建的72372+中英文词汇库，包含单词、词频（COCA）、音标、中文释义、短语和例句。

# 来源
- 单词来源：BNC_COCA_lists.csv
- 单词释义：有道词典API https://dict.youdao.com/jsonapi_s?doctype=json&jsonversion=4&q=？

# 数据说明
- 所有单词数据存放在/data目录，每个单词一个json
- 访问方式：https://cdn.jsdelivr.net/gh/changhongzi/BNC_COCA_EN2CN/data/${word}.json
- json文件内容说明：
```javascript
{
    "word": "a", //单词
    "headword": "a", //单词原型
    "frequency": "2186984",  //词频
    "list": "1k", //词频级别
    "usPhone": "ə; eɪ", //美式
    "ukPhone": "ə; eɪ", //英式
    "translations": ["一；任一；每一"], //中文释义
    "phrs": [], //短语
    "sentences": [{
        "sentence": "They had a butler, a cook, and a maid.", //英语例句
        "translation": "他们有一位管家、一位厨师和一位女仆。" //例句释义
    }, {
        "sentence": "A man in a crash helmet was mounting a motorcycle.",
        "translation": "一个戴着防撞头盔的男子正骑上一辆摩托车。"
    }, {
        "sentence": "He's a scoundrel! A cad!",
        "translation": "他是个恶棍！一个卑鄙的无赖！"
    }]
}
```
