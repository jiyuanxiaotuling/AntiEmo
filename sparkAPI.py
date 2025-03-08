# coding: utf-8
import _thread as thread
import os
import time
import base64
import datetime
import hashlib
import hmac
import json
from urllib.parse import urlparse
import ssl
from datetime import datetime
from time import mktime
from urllib.parse import urlencode
from wsgiref.handlers import format_date_time

import websocket
import openpyxl
from concurrent.futures import ThreadPoolExecutor, as_completed
import os


class Ws_Param(object):
    # 初始化
    def __init__(self, APPID, APIKey, APISecret, gpt_url):
        self.APPID = APPID
        self.APIKey = APIKey
        self.APISecret = APISecret
        self.host = urlparse(gpt_url).netloc
        self.path = urlparse(gpt_url).path
        self.gpt_url = gpt_url

    # 生成url
    def create_url(self):
        now = datetime.now()
        date = format_date_time(mktime(now.timetuple()))
        signature_origin = "host: " + self.host + "\n"
        signature_origin += "date: " + date + "\n"
        signature_origin += "GET " + self.path + " HTTP/1.1"
        signature_sha = hmac.new(self.APISecret.encode('utf-8'), signature_origin.encode('utf-8'),
                                 digestmod=hashlib.sha256).digest()
        signature_sha_base64 = base64.b64encode(signature_sha).decode(encoding='utf-8')
        authorization_origin = f'api_key="{self.APIKey}", algorithm="hmac-sha256", headers="host date request-line", signature="{signature_sha_base64}"'
        authorization = base64.b64encode(authorization_origin.encode('utf-8')).decode(encoding='utf-8')
        v = {
            "authorization": authorization,
            "date": date,
            "host": self.host
        }
        url = self.gpt_url + '?' + urlencode(v)
        return url


def on_error(ws, error):
    print("### error:", error)


def on_close(ws):
    print("### closed ###")


def on_open(ws):
    thread.start_new_thread(run, (ws,))


def run(ws, *args):
    data = json.dumps(gen_params(appid=ws.appid, query=ws.query, domain=ws.domain))
    ws.send(data)


def on_message(ws, message):
    data = json.loads(message)
    code = data['header']['code']
    if code != 0:
        print(f'请求错误: {code}, {data}')
        ws.close()
    else:
        choices = data["payload"]["choices"]
        status = choices["status"]
        content = choices["text"][0]["content"]
        print(content, end='')
        if status == 2:
            print("\n#### 关闭会话")
            ws.close()


def gen_params(appid, query, domain):
    """
    通过appid和用户的提问来生成参数，加入心理医生 Prompt
    """
    # 定义心理医生的系统指令
    system_prompt = {
        "role": "system",
        "content": "你是一位专业的心理医生，拥有丰富的心理学知识和同理心。你的目标是倾听用户的心声，提供温暖、支持和建设性的建议，帮助他们缓解情绪压力。请用亲切、自然的语气回应，避免过于正式或冷漠的表达。"
    }
    # 用户输入
    user_message = {
        "role": "user",
        "content": query
    }
    data = {
        "header": {
            "app_id": appid,
            "uid": "1234",
        },
        "parameter": {
            "chat": {
                "domain": domain,
                "temperature": 0.5,
                "max_tokens": 4096,
                "auditing": "default",
            }
        },
        "payload": {
            "message": {
                "text": [system_prompt, user_message]  # 将系统指令和用户输入组合
            }
        }
    }
    return data


def main(appid, api_secret, api_key, Spark_url, domain, query):
    wsParam = Ws_Param(appid, api_key, api_secret, Spark_url)
    websocket.enableTrace(False)
    wsUrl = wsParam.create_url()
    ws = websocket.WebSocketApp(wsUrl, on_message=on_message, on_error=on_error, on_close=on_close, on_open=on_open)
    ws.appid = appid
    ws.query = query
    ws.domain = domain
    ws.run_forever(sslopt={"cert_reqs": ssl.CERT_NONE})


if __name__ == "__main__":
    main(
        appid="659e9b50",
        api_secret="MmQ5MTYwNjExZmFiMGJhMzk3NzY1NjY1",
        api_key="5a1b34a30d042d2af5897c177e7ab0f2",
        # appid、api_secret、api_key三个服务认证信息请前往开放平台控制台查看（https://console.xfyun.cn/services/bm35）
        Spark_url="wss://spark-api.xf-yun.com/v1.1/chat",  # Max环境的地址
        # Spark_url = "wss://spark-api.xf-yun.com/v4.0/chat"  # 4.0Ultra环境的地址
        # Spark_url = "wss://spark-api.xf-yun.com/v3.1/chat"  # Pro环境的地址
        # Spark_url = "wss://spark-api.xf-yun.com/v1.1/chat"  # Lite环境的地址
        # domain="generalv3.5",     # Max版本
        # domain = "4.0Ultra"     # 4.0Ultra 版本
        # domain = "generalv3"    # Pro版本
        domain="lite",  # Lite版本址
        query="我最近感到很焦虑，压力很大，怎么办？"  # 用户输入示例
    )