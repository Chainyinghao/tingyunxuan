# -*- coding: utf-8 -*-
# date:2018/9/25
# comment:利用urllib读取JSON，然后将JSON解析为Python对象

import json
from urllib import request

def fetch_data(url):
    with request.urlopen(url) as f:
        for i, j in f.getheaders():
            print("%s:%s" %(i, j))
        return json.loads(f.read().decode("utf-8"))

URL = 'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=json'
data = fetch_data(URL)
print("\n获取数据为：")
print(data)
assert data['query']['results']['channel']['location']['city'] == 'Beijing'
print('ok')




