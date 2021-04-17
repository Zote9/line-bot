from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('DVRDle+BHLNFBweh5ygR4pSxYDXcFZzXmg3T/1Jb1945Lys2yS6r3pHz0sdrUV2Hn4uuppY3zwsDsFxTRPg6p4G8hnxLfQXRDGNVNFGA5/nsokMxj6aEyNB9WJsRUwCteG7whn2sUafuOweM8pihkwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('a7641a195c580f2d084189c0892905ad')


@app.route("/callback", methods=['POST'])
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
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    r = '很抱歉 您說什麼?'
    if msg == 'hi':
        ry = 'hi'
    elif msg == '你吃飯了嗎':
        r = '還沒'

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=r))


if __name__ == "__main__":
    app.run()