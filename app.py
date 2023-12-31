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
from linebot import ( WebhookHandler, LineBotApi )
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
    LocationSendMessage, ImageSendMessage, StickerSendMessage,
    VideoSendMessage, TemplateSendMessage, ButtonsTemplate, PostbackAction, MessageAction, URIAction,
    PostbackEvent, ConfirmTemplate, CarouselTemplate, CarouselColumn,
    ImageCarouselTemplate, ImageCarouselColumn, FlexSendMessage, QuickReply
)
import json
from module import *

# create flask server
app = Flask(__name__)
line_bot_api = LineBotApi(os.getenv("CHANNEL_ACCESS_TOKEN"))
handler = WebhookHandler(os.getenv("CHANNEL_SECRET"))

class main:
    def __init__(self) -> None: 
        global ai_flag
        ai_flag = False
        port = int(os.environ.get('PORT', 5000))
        app.run(host='0.0.0.0', port='5566')
    
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
    def handle_text(event):
        global ai_flag # to make AI switch
        # print(ai_flag)
        match ai_flag:
            case True:
                chatbot = AI()
                reply = chatbot.askQuestion(event.message.text)
                send_message = TextSendMessage(reply)
                
            case False:
                match event.message.text:
                    case "最新優惠":
                        send_message = News.show_new_event()
                    case "我要預約":
                        send_message = Reservation.reservation_confirm()
                    case "會員":
                        send_message = Member.quick_reply_test()
                    case "門市查詢":
                        reply = "門市查詢"
                        send_message = Map.store_fliter_area() 
                    case _:
                        reply = "echo: " + event.message.text
                        send_message = TextSendMessage(reply)
                        
        line_bot_api.reply_message( event.reply_token, send_message )
        
    # when receive postback
    @handler.add(PostbackEvent)
    def handle_postback(event):
        global ai_flag
        # print(ai_flag)
        match event.postback.data:
            
            # when click on richmenu area B to turn on/off AI
            case "ai-on":
                ai_flag = True
                reply = "whats your problem"
                send_message = TextSendMessage(reply)
            case "ai-close":
                ai_flag = False
                reply = "byeeeeeee"
                send_message = TextSendMessage(reply)
                
            # when confirm the action of reservation
            case "reservation-yes":
                send_message = Reservation.reservation_select()
            case "reservation-no":
                reply = "取消預約"
                send_message = TextSendMessage(reply)
                
            # when choosing which type of service the user wants to make a reservation
            case "reservation-instore":
                reply = "現場"
                send_message = TextSendMessage(reply)
            case "reservation-online":
                reply = "線上"
                send_message = TextSendMessage(reply)
            
            # when look up for stores in different areas  
            case "check_north_store":
                reply = "北部"
                send_message = TextSendMessage(reply)
            case "check_mid_store":
                reply = "中部"
                send_message = TextSendMessage(reply)
            case "check_south_store":
                reply = "南部"
                send_message = TextSendMessage(reply)
            case "check_east_store":
                reply = "東部"
                send_message = TextSendMessage(reply)
                
            case "quick_reply_test":
                reply = "receive postback"
                send_message = TextSendMessage(reply)
                
        line_bot_api.reply_message( event.reply_token, send_message )


# run app
if __name__ == "__main__":
    main = main()