from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
    StickerMessage, StickerSendMessage,
    MessageAction
)

line_bot_api = LineBotApi(
    '你的LINE存取代碼 access code')
handler = WebhookHandler(
    '你的LINE頻道密鑰 secret')

passcode = 'zzzzz'    # 請自行修改密碼
ME = '你的LINE ID'

app = Flask(__name__)


def reply_text(token, id, txt):
    if txt == '你好' or txt == 'Hi':
        line_bot_api.reply_message(
            token,
            TextSendMessage(text="您好！"))
    else:
        line_bot_api.reply_message(
            token,
            StickerSendMessage(
                package_id=3, sticker_id=233
            ))


@app.route('/')
def index():
    return '我是聊天機器人！'


def send_msg(txt):
    line_bot_api.push_message(ME, TextSendMessage(text=txt))


@app.route('/btn')
def btn():
    key = request.args.get('key')
    id = request.args.get('id')

    if key != passcode:
        return '<h1>出錯啦！</h1>', 401, {'ContentType': 'text/html'}

    if id == 'wash_dish':
        send_msg('女王呼喚！\n快去洗碗！')
        return f'id:{id}'
    elif id == 'front_door':
        send_msg('入侵警報！！！')
        return f'id:{id}'
    else:
        return '請指定裝置代碼！'


@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

# 處理文字訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    _id = event.source.user_id
    print('使用者的ID：', _id)
    txt = event.message.text
    reply_text(event.reply_token, _id, txt)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)
    # app.run()
