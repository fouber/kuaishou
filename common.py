#!/usr/bin/env python
# encoding: utf-8
import requests

API = "https://api.appsign.vip:2688"

header = {
    "User-Agent": "kwai-ios"
}

APPINFO = {
    "ver": "5.9",
    "appver": "5.9.1.656"
}

# 获取Token       有效期60分钟
def getToken():
    #resp = requests.get(API + "/token/douyin").json()
    resp = requests.get(API + "/token/kuaishou").json()
    token = resp['token']
    print("Token: " + token)
    return token

# 拼装参数
def params2str(params):
    query = ""
    for k, v in params.items():
        query += "%s=%s&" % (k, v)
    query = query.strip("&")
    print("Sign str: " + query)
    return query

# 使用拼装参数签名
def getSign(token, query):
    if isinstance(query, dict):
        query = params2str(query)
    resp = requests.post(API + "/sign", json={"token": token, "query": query}).json()
    print("签名返回: " + str(resp))
    sign = resp['data']
    return sign
