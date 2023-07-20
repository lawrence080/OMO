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
    ImageCarouselTemplate, ImageCarouselColumn, FlexSendMessage
)
import json

line_bot_api = LineBotApi(os.getenv("CHANNEL_ACCESS_TOKEN"))
handler = WebhookHandler(os.getenv("CHANNEL_SECRET"))

class Reservation():
    def __init__(self) -> None:
        pass
    
    def reservation_confirm(event):
        file_path = os.path.join(os.path.split(__file__)[0] + '/static/flex_message_template/reservation_confirm.json' )
        with open(file_path) as f:
            reply = json.load(f)
        send_message = FlexSendMessage( alt_text="show on computer", contents=reply)
        return send_message
    
