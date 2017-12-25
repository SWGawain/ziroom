# -*- coding: utf-8 -*-

import requests ,re , random , time
from ziroom import zrConfig

while True:
    hea = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.118 Safari/537.36'}

    page = requests.get("http://www.ziroom.com/z/vr/"+ str(zrConfig.room) +".html" , headers=hea)
    page.encoding = "utf-8"

    loading = re.search('loading.jpg' , page.text , re.S)
    canbook = re.search("canbook.jpg" , page.text , re.S)

    if canbook or (not loading):
        print("房源状态变更，可以预定")
        zrConfig.sendNotice()

    print(loading , canbook)

    time.sleep(3 + random.random())