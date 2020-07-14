import requests as req
from datetime import datetime
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
    StickerMessage, StickerSendMessage,
    ConfirmTemplate, TemplateSendMessage,
    MessageAction, URIAction, LocationMessage,
    ButtonsTemplate
)

line_bot_api = LineBotApi('你的LINE存取代碼 access code')
handler = WebhookHandler('你的LINE頻道密鑰 secret')

passcode = 'zzzzz'              # 請自行修改密碼
ME = '你的LINE ID'
ESP8266_IP = '192.168.0.113'    # 請自行修改微控制器的IP位址

app = Flask(__name__)

def reply_text(token, id, txt):
    if txt == '開燈':
        feedback = req.get(f'http://{ESP8266_IP}/sw?led=on').text
        print('控制器回應：', feedback)

        if feedback == 'OK!':
            txt = '已開燈！'
        else:
            txt = '控制器沒有回應！'

        line_bot_api.reply_message(
                token,
                TextSendMessage(text=txt))

    if txt == '關燈':
        feedback = req.get(f'http://{ESP8266_IP}/sw?led=off').text
        print('控制器回應：', feedback)

        if feedback == 'OK!':
            txt = '關掉了！'
        else:
            txt = '控制器沒有回應！'

        line_bot_api.reply_message(
                token,
                TextSendMessage(text=txt))

@app.route('/')
def index():
    return 'Welcome to Line Bot!'

@app.route('/btn')
def btn():
    key = request.args.get('key')

    if key != passcode:
        return '<h1>ERROR!</h1>', 401, {'ContentType':'text/html'}
    
    id = request.args.get('id')

    if id is not None and id == 'wash_dish':
        txt = '女王呼喚！\n快去洗碗！'
        line_bot_api.push_message(ME, TextSendMessage(text=txt))

        return f'id:{id}'
    else:
        return f'請指定編號！'

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

@handler.default()
def default(event):
    print('捕捉到事件：', event)

# 處理文字訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    _id = event.source.user_id
    profile = line_bot_api.get_profile(_id)
    # 紀錄用戶資料
    _name = profile.display_name
    print('大頭貼網址：', profile.picture_url)
    print('狀態消息：', profile.status_message)

    txt=event.message.text

    reply_text(event.reply_token, _id, txt)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)
    # app.run()