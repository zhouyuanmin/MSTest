import json
import base64
import time
import threading
from websocket import create_connection
from websocket._exceptions import WebSocketConnectionClosedException

# address = "ws://39.102.79.219:8101/3d/v1/wss_back/"
# address = "ws://127.0.0.1:30003/3d/v1/face_back/"
# 测试ai
address = "ws://127.0.0.1:30003/ai/v2/wss_back/"
f1 = open("code_face.txt", "r+", encoding="utf-8")
code_t = str(f1.read()).encode("u8")
code_str: str = base64.b64encode(code_t).decode("u8")
json_str = {"type": 1,
            "data": code_str,
            "files": []}


class WebSocket:
    def __init__(self, _address):
        self.ws = create_connection(_address)

    def send(self, params):
        # print("Sending ...")
        self.ws.send(json.dumps(params))
        # print("Receiving...")
        result = self.ws.recv()
        print("Received '{}'".format(result[0:23]))

    def quit(self):
        self.ws.close()


def run():
    try:
        web_so = WebSocket(address)
        web_so.send(json_str)
        web_so.quit()
    except WebSocketConnectionClosedException:
        print("========error========")
    finally:
        pass


if __name__ == '__main__':
    print(f'begin:{time.strftime("%Y-%m-%d %H:%M:%S")}')
    for i in range(1):
        print(f'time:{time.strftime("%Y-%m-%d %H:%M:%S")}')
        for _ in range(5):
            t1 = threading.Thread(target=run)
            t1.start()
        time.sleep(1)

"""face
1 * 100个=100 都请求成功 其中5个后来断掉了
10 * 100个=1000 138个失败 其中62个后来断掉了
30 * 50个=1500  2个失败 其中 其中190个后来断掉了
50 * 30个=1500  66个失败 其中 其中219个后来断掉了
"""