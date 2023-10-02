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
    "word": "good", //单词
    "headword": "good",  //单词原型
    "frequency": "82337", //词频
    "list": "1k", //词频统计
    "usPhone": "ɡʊd", //美式音标
    "ukPhone": "ɡʊd", //英式音标
    "examType": ["初中", "高中", "CET4", "CET6", "考研"], //考试类型
    "translations": ["adj.好的，优良的；能干的，擅长的；好的，符合心愿的；令人愉快的，合意的；（心情）愉快的；迷人的，漂亮的；可能会成功的，可能正确的；合适的，方便的；有益的，有好处的，有用的；温顺的，乖的，有礼貌的；虔诚的，遵守规则（或约定）的；健康的，健全的；状况好的；助人为乐的，心地善良的，好心的；符合道德的，正派的，高尚的；（数量或程度）相当大的，相当多的；很，非常；彻底的，完全的；合情理的，有说服力的，有充分根据的；划算的，收益可观的；赞同的，赢得赞许的，令人尊敬的；（用于表示回应）好的；表示惊讶、生气或者加强语气；（用于打招呼）好；至少，不少于；有趣的，逗笑的；在…时间内有效，非伪造的；（比赛中打的球）好的，有效的，可以得分的；（踢、射、投）命中；能提供……的；足够支付的；上流的，高贵的；（衣服）时髦的，适合正式场合穿着的；亲密的，友好的；尤指以屈尊俯就或幽默的方式好（人）；有……意向的；够了，到此为止了；精确的，准确的", "n.合乎道德的行为，正直的行为，善行；对的事情（the good）；好事（the good）；好的方面；好结果；有道德的人，高尚的人，好人（the good）；用处，益处，利益；商品，所有物；<英>（与乘客相区别的）待运货物（goods）；私人财物（goods）；<非正式>真货，正品（the goods）", "adv.<非正式>好地；<美>彻底地，完全地", "【名】 （Good）（英）古德，（瑞典）戈德（人名）"],  //中文释义
    "phrs": [{
        "headword": "good at",
        "translation": "善于"
    }, {
        "headword": "good and",
        "translation": "完全，非常"
    },{
        "headword": "for good",
        "translation": "永久地；一劳永逸地"
    }], //短语
    "sentences": [{
        "sentence": "She speaks good English.",
        "translation": "她英语说得很好。"
    }, {
        "sentence": "It was really good.",
        "translation": "这非常好。"
    }, {
        "sentence": "I'm going to write good jokes and become a good comedian.",
        "translation": "我要创作出好的笑话并且成为一个优秀的喜剧演员。"
    }]//例句
}
```
