import requests
import time

cookies = {
    "PHPSESSID": "t1st7fkdflo0bungui5mh0fta3",
    "WEB3": "1a27ef96cd9c2e4d5d9a43d9ef97e5cc",
    # "_s_tentry": "-",
    # "Apache": "9032087486462.918.1526969207001",
    # "SINAGLOBAL": "9032087486462.918.1526969207001",
    # "ULV": "1526969207082:1:1:1:9032087486462.918.1526969207001:",
    # "UOR": ",,www.google.co.jp",
    # "WBStorage": "5548c0baa42e6f3d|undefined"
}

headers = {
    'Referer': 'http://data.weibo.com/index',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'
}

search_url = 'http://data.weibo.com/index/hotword?wid=c0KXz6XkS1m6r&wname=mix'

data_url = 'http://data.weibo.com/index/ajax/getchartdata?month=default&__rnd=1526970455244'

date_time = 'http://data.weibo.com/index/ajax/getchartdata?wid=120180517165805803232&sdate=2016-05-22&edate=2018-05-21&__rnd=1526972040494'
# search_html = requests.get(search_url, headers=headers, cookies=cookies)

# html = requests.get(data_url, headers=headers, cookies=cookies)
# print(html.text)

##################################

# ticks = time.time()
# print(str(ticks).replace('.', '')[:13])

##################################

s = requests.Session()
# cookiess = {'WEB3': 'bf504b4b55f0b40cedd4cdf9a8370ca8'}
url = 'http://data.weibo.com/index/hotword?wid=1030000000269&wname=iphone'
html = s.get(url, headers=headers)
print(html.text)

# http://data.weibo.com/index/hotword?wid=1030000000269&wname=iphone