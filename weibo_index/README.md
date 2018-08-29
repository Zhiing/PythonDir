# 说明

> [博客说明](https://xionzhi.com/scrapy-wei-index/ "weibo index")

## 配置参数

- 修改根目录下的 `key_words.txt`, 一行一个, 编码 `utf-8`

- 修改 `/weibo_index/spider/weibo.py` 中 `__init__` 的时间限制

- `pipelines.py` 中设置文件 保存

## 启动方法

- 根目录下运行 shell `scrapy crawl weibo_index`

- `scrapy crawl weibo_index -o items.csv`

## 关于字段

- 'wid': 新浪关键词 唯一id
- 'wname': 关键词
- 'daykey': 时间
- 'mobile': 移动
- 'pc': pc
