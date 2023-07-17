import json
import requests
import os
from dotenv import load_dotenv
load_dotenv()
from linebot import (
    LineBotApi, WebhookHandler
)

token = os.getenv("CHANNEL_ACCESS_TOKEN")
Authorization_token = "Bearer " + token
headers = {"Authorization": Authorization_token, "Content-Type": "application/json"}
line_bot_api = LineBotApi(token)

rich_menu_list = line_bot_api.get_rich_menu_list()
for rich_menu in rich_menu_list:
    # print(rich_menu.rich_menu_id)
    line_bot_api.delete_rich_menu(rich_menu.rich_menu_id)