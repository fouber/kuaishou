#!/usr/bin/env python
# encoding: utf-8
import requests
from common import *

"""
拉取首页视频
"""

# 获取Token       有效期60分钟
token = getToken()

# 获取新的设备信息  有效期永久
#device_info = getDevice()
device_info = {
    "did": "XXXX-XXXX-XXXX-XXXX-XXXXXXXXXX",
    "c": "a",
    "extId": "0000000000000000000000000",
    "sys": "ios11.0.0",
    "mod": "iPhone8,0",
    "net": "mobile"
}

# 拼装参数
get_params = device_info.copy()
get_params.update(APPINFO)

post_params = {
    "client_key": "56c3713c",
    "coldStart": "true",
    "count": 20,
    "country_code": 'cn',
    "id": "42",
    "language": "zh-Hans-CN;q=1",
    "pv": False,
    "refreshTimes": 0,
    "source": 1,
    "type": 7
}

# 签名参数由 get和post参数共同组成
sign_params = get_params.copy()
sign_params.update(post_params)

# 获取签名
sign = getSign(token, sign_params)
post_params['sig'] = sign['sign']
print(post_params)

# 拉取首页视频列表
resp = requests.post("http://103.107.217.2/rest/n/feed/hot", params=get_params, data=post_params, headers=header).json()
print(resp)