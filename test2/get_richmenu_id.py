import os
from dotenv import load_dotenv
load_dotenv()
import requests
import json


token = os.getenv("CHANNEL_ACCESS_TOKEN")
Authorization_token = "Bearer " + token
headers = {"Authorization": Authorization_token, "Content-Type": "application/json"}

# 設定一次就可以註解掉了

the_richmenu = './test2/static/richmenu_template/richmenu_a.txt'
json_path = os.path.join(os.path.split(__file__)[0], the_richmenu)
body = json_path

# get rich menu id
req = requests.request('POST', 'https://api.line.me/v2/bot/richmenu',
                       headers=headers, data=json.dumps(body).encode('utf-8'))
print(req.text)


