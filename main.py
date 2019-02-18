from linebot import LineBotApi
from linebot.models import TextSendMessage
from flask import Flask
import os
import time

LINE_CHANNEL_ACCESS_TOKEN = "54SfB4WOh1G2/yf/1j3+BQdIGOAElTuieI0y12hqJ04+BsK3i5AVwXcD5TBYmp8hQzEKT9qC/lic8q4cdrG3KdIJKXJhr7QR+i+gxjkYkpHB4px4h4duTaMlR8iz2Vu57gKKGel9CUq1OVvBsO+r5QdB04t89/1O/w1cDnyilFU="

line_bot_api = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)

app = Flask(__name__)
app.debug = False

def main():
    while(True):
        user_id = "Ue8baeea0f29de588e397c74e7b3dcf31"

        messages = TextSendMessage(text="Send Toilet Pepar")
        line_bot_api.push_message(user_id, messages=messages)

        time.sleep(60)

if __name__ == "__main__":
    port = int(os.getenv("PORT"))
    app.run(host="0.0.0.0", port=port)
