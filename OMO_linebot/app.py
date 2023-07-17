import os 
from dotenv import load_dotenv
load_dotenv()
import openai
from OMO_aiBot.main import AI
openai.api_key = os.getenv("OPEN_AI_KEY")
# import flask related
from flask import Flask, request, abort
from urllib.parse import parse_qsl

# import linebot related
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
    LocationSendMessage, ImageSendMessage, StickerSendMessage,
    VideoSendMessage, TemplateSendMessage, ButtonsTemplate, PostbackAction, MessageAction, URIAction,
    PostbackEvent, ConfirmTemplate, CarouselTemplate, CarouselColumn,
    ImageCarouselTemplate, ImageCarouselColumn, FlexSendMessage
)
import json

# create flask server
app = Flask(__name__)

line_bot_api = LineBotApi(os.getenv("CHANNEL_ACCESS_TOKEN"))
handler = WebhookHandler(os.getenv("CHANNEL_SECRET"))

# get LINE info
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        print('receive msg')
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)
    return 'OK'

# when receive text message
@handler.add(MessageEvent, message=TextMessage)
def keyword(event):
    chatbot = AI()
    # chatbot.askQuestion()
    # match event.message.text:
    #     case "A":
    #         reply = 'keyword a'
    #     case _:
    #         reply = event.message.text
    line_bot_api.reply_message( event.reply_token, TextSendMessage(reply) )
    
# when receive postback
@handler.add(PostbackEvent)
def call_ai(event):
    match event.postback.data:
        case 'change-to-bbb':
            reply = 'whats your problem'
        case 'change-to-aaa':
            reply = 'close ai'
    line_bot_api.reply_message( event.reply_token, TextSendMessage(reply) )

# run app
if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5566)