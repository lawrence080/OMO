import os
from dotenv import load_dotenv
load_dotenv()
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
    ImageCarouselTemplate, ImageCarouselColumn, FlexSendMessage, QuickReply
)
import json

line_bot_api = LineBotApi(os.getenv("CHANNEL_ACCESS_TOKEN"))
handler = WebhookHandler(os.getenv("CHANNEL_SECRET"))

class File():
    def __init__(self) -> None:
        pass
    
    def read_file(file_path):
        file_path = os.path.join(os.path.split(__file__)[0] + file_path)
        with open(file_path) as f:
            reply = json.load(f)
        return reply       

class Reservation():
    def __init__(self) -> None:
        pass
    
    def reservation_confirm():
        reply = File.read_file("/static/flex_message_template/reservation_confirm.json")
        send_message = FlexSendMessage( alt_text="show on computer", contents=reply)
        return send_message
    
    def reservation_select():
        reply = File.read_file("/static/flex_message_template/reservation_select.json")
        send_message = FlexSendMessage( alt_text="show on computer", contents=reply)
        return send_message

class News():
    def __init__(self) -> None:
        pass 
    
    def show_new_event():
        reply = File.read_file("/static/flex_message_template/news.json")
        send_message = FlexSendMessage( alt_text="show on computer", contents=reply)
        return send_message
    
class Map():
    def __init__(self) -> None:
        pass
    
    def store_fliter_area():
        reply = File.read_file("/static/flex_message_template/store_area.json")
        send_message = FlexSendMessage( alt_text="show on computer", contents=reply)
        return send_message

    def check_north_stores():
        reply = "north"
        send_message = TextMessage(reply)
        return send_message
    
    def check_mid_stores():
        reply = "mid"
        send_message = TextMessage(reply)
        return send_message
    
    def check_south_stores():
        reply = "south"
        send_message = TextMessage(reply)
        return send_message
    
    def check_east_store():
        reply = "east"
        send_message = TextMessage(reply)
        return send_message
    
class Member():
    def __init__(self) -> None:
        pass
    
    def quick_reply_test():
        reply = QuickReply(items=File.read_file("/static/quick_reply_template/quick_reply_test.json"))
        send_message = TextSendMessage(text="quick reply test", quick_reply=reply)
        return send_message