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

class Richmenu:
    def __init__(self, body):
        self.body = body
        req = requests.request('POST', 'https://api.line.me/v2/bot/richmenu',
                       headers=headers, data=json.dumps(body).encode('utf-8'))
        
        # get richmenu id from req.text
        j = 0
        temp = ""
        for i in req.text:
            if i == "\"": j = j + 1
            elif (j >= 3) & (j != 4): temp = temp + i 
                
        self.richmenu_id = temp
        
    # set up image, can only be excuted once
    def set_image(self, img_path):
        with open(img_path, 'rb') as f:
            line_bot_api.set_rich_menu_image(self.richmenu_id, "image/png", f)
    
    # set up alias id        
    def set_alias_id(self, alias_id):
        body_alias = {
            "richMenuAliasId": alias_id,
            "richMenuId": self.richmenu_id
        }
        req = requests.request('POST', 'https://api.line.me/v2/bot/richmenu/alias',
                      headers=headers,data=json.dumps(body_alias).encode('utf-8'))
        print(req.text)
    
    # post rich menu to line bot      
    def post_richmenu(self): 
        req = requests.request('POST', 'https://api.line.me/v2/bot/user/all/richmenu/' + self.richmenu_id, headers=headers)
        print(req.text)
        rich_menu_list = line_bot_api.get_rich_menu_list()

    # set rich menu to default
    def default_richmenu(self):
        line_bot_api.set_default_rich_menu(self.richmenu_id)

    # need to delete ID first to reset
    def del_richmenu(richmenu_id):
        line_bot_api.delete_rich_menu(richmenu_id)
        
    def show_richmenu():
        rich_menu_list = line_bot_api.get_rich_menu_list
        for rich_menu in rich_menu_list:
            print("name: " + rich_menu.name)
            print("id: " + rich_menu.rich_menu_id + "\n")

# set up rich menu        
the_richmenu = '/function_test_b.json'
file_path = os.path.join(os.path.split(__file__)[0] + '/static/richmenu_template' + the_richmenu)
with open(file_path) as f:
    body = json.load(f)

r = Richmenu(body)   
r.set_image("/Users/ying/OMO/static/image/function_test_b.png")
r.set_alias_id("ai-on")
r.post_richmenu()
# r.default_richmenu()