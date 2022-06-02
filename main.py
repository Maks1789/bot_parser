import requests
from bs4 import BeautifulSoup
from time import sleep
import logging
from aiogram import Bot, Dispatcher, executor, types
url = "https://www.battlemetrics.com/servers/dayz/15422954"
bot = Bot(token="00000000000000000000000")
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)


@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    while True:
        if print_hi(url) == "Online":
            #await message.answer("Server online")
            sleep(30)
        else:
            await message.answer("Server offline")
            sleep(600)


def print_hi(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    a = soup.find_all('meta')[0]
    print(a)
    if "Status: online" in str(a):
        return "Online"
    else:
        return "Server not found"



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)


