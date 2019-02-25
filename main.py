from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, ImageSendMessage,
)
import os
import json

app = Flask(__name__)
app.debug = False

f = open('date.json', 'r')
DrinkDate = json.load(f)

line_bot_api = LineBotApi('54SfB4WOh1G2/yf/1j3+BQdIGOAElTuieI0y12hqJ04+BsK3i5AVwXcD5TBYmp8hQzEKT9qC/lic8q4cdrG3KdIJKXJhr7QR+i+gxjkYkpHB4px4h4duTaMlR8iz2Vu57gKKGel9CUq1OVvBsO+r5QdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('84f1dc304d0714dfa5266f0c10a99b00')

def GetDrinkDate(DrinkName):
    SendURL = ""
    if DrinkName in DrinkDate["GAKUSE-KA"]:
        SendURL = SendURL + "学生課前\nhttps://www.google.com/maps?q=34.482481,136.825055\n\n"
    if DrinkName in DrinkDate["SHIOSAI"]:
        SendURL = SendURL + "潮騒会館\nhttps://www.google.com/maps?q=34.482616,136.824430\n\n"
    if DrinkName in DrinkDate["TOSHOKAN"]:
        SendURL = SendURL + "図書館下\nhttps://www.google.com/maps?q=34.482325,136.824341\n\n"
    if DrinkName in DrinkDate["RYOSHOKU"]:
        SendURL = SendURL + "寮食堂前\nhttps://www.google.com/maps?q=34.480867,136.825025\n\n"
    if DrinkName in DrinkDate["B-to"]:
        SendURL = SendURL + "B棟１階\nhttps://www.google.com/maps?q=34.480462,136.824733\n\n"

    return SendURL

def DrinkSearch(DrinkName):
    if DrinkName in DrinkDate["GAKUSE-KA"]:
        return True
    elif DrinkName in DrinkDate["SHIOSAI"]:
        return True
    elif DrinkName in DrinkDate["TOSHOKAN"]:
        return True
    elif DrinkName in DrinkDate["RYOSHOKU"]:
        return True
    elif DrinkName in DrinkDate["B-to"]:
        return True
    else:
        return False

@app.route("/callback", methods=['POST'])
#この辺はコピペやから何をやっとるかよく分からん
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    if event.type == "message":
        DrinkTorF = DrinkSearch(event.message.text)
        if (event.message.text == "学生課前"):
            line_bot_api.reply_message(
                event.reply_token,
                [
                    TextSendMessage(text="お茶、サイダーなどがあります。"),
                    TextSendMessage(text="https://www.google.com/maps?q=34.482481,136.825055")
                ]
            )
        if (event.message.text == "潮騒会館"):
            line_bot_api.reply_message(
                event.reply_token,
                [
                    TextSendMessage(text="コーヒー、カフェオレなどがあります。"),
                    TextSendMessage(text="https://www.google.com/maps?q=34.482616,136.824430")

                ]
            )
        if (event.message.text == "図書館下"):
            line_bot_api.reply_message(
                event.reply_token,
                [
                    TextSendMessage(text="コーラ、ファンタなどがあります。"),
                    TextSendMessage(text="https://www.google.com/maps?q=34.482325,136.824341")
                ]
            )
        if (event.message.text == "寮食堂前"):
            line_bot_api.reply_message(
                event.reply_token,
                [
                    TextSendMessage(text="コーラ、ファンタなどがあります。"),
                    TextSendMessage(text="https://www.google.com/maps?q=34.480867,136.825025")
                ]
            )
        if (event.message.text == "B棟"):
            line_bot_api.reply_message(
                event.reply_token,
                [
                    TextSendMessage(text="カルピスソーダ、モンスターなどがあります。"),
                    TextSendMessage(text="https://www.google.com/maps?q=34.480462,136.824733")
                ]
            )
        if (DrinkTorF == False):
            line_bot_api.reply_message(
                event.reply_token,
                [
                    TextSendMessage(text="ごめんなさい、その飲み物は学校の自販機にないみたい。別のを探してね。")
                ]
            )
        elif (DrinkTorF == True):
            MapURLs = GetDrinkDate(event.message.text)
            line_bot_api.reply_message(
                event.reply_token,
                [
                    TextSendMessage(text=MapURLs + "にありますよ！")
                ]
            )

if __name__ == "__main__":
    port = int(os.getenv("PORT"))
    app.run(host="0.0.0.0", port=port)
