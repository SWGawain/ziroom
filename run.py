# -*- coding: utf-8 -*-

import requests ,re
from ziroom import zrConfig

hea = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.118 Safari/537.36'}

page = requests.get("http://www.ziroom.com/z/vr/116152.html" , headers=hea)
page.encoding = "utf-8"

photo = re.findall("http://pic.ziroom.com/static/images/slist_1207/defaultPZZ/natie-.+\.jpg" , page.text , re.S)
print(photo)



