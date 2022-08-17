from bs4 import BeautifulSoup
import requests
from config import token_bot

def parsersite(url)-> bool:
    try:
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')
        a = soup.find_all('meta')[0]
        print(a)
        if "Status: online" in str(a):
            return True
        else:
            return False
    except:
        print("parsersite 404")


def send_all_user(channel_id, text):
    url = "https://api.telegram.org/bot"
    url += token_bot
    method = url + "/sendMessage"

    r = requests.post(method, data={
         "chat_id": channel_id,
         "text": text
          })




