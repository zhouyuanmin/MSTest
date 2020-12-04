# --*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*-+
# -*- coding: utf-8 -*-                            |
# @Time    : 2020/7/14 11:06                       *
# @Author  : Bob He                                |
# @FileName: post_server.py                              *
# @Software: PyCharm                               |
# @Project : testpy                                *
# @Csdn    ：https://blog.csdn.net/bobwww123       |
# @Github  ：https://www.github.com/NocoldBob      *
# --*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*-+
import json
import requests
import threading
import base64
import time

# url = "https://papi.dingdangcode.cn/3d/v1/baseRun/createModule"
# url = "http://39.102.79.219:8101/3d/v1/baseRun/createModule"
url = "http://127.0.0.1:30001/3d/v1/baseRun/createModule"
f1 = open("code.txt", "r+", encoding="utf-8")
code_t = str(f1.read()).encode("u8")
code_str: str = base64.b64encode(code_t).decode("u8")

data_json = json.dumps(
    {"code": code_str})
headers = {'content-type': 'application/json;charset=UTF-8'}


def creat3D():
    start_t = time.time()
    r_json = requests.post(url, data_json, headers=headers)
    print(r_json.text[0:100])
    print("请求耗时：", time.time() - start_t, "秒")


if __name__ == '__main__':

    for _ in range(20):
        t1 = threading.Thread(target=creat3D)
        t1.start()
        print(_)


