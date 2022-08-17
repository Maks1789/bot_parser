import logging
from aiogram import Bot, Dispatcher, executor, types
import time
from pars import send_all_user, parsersite
from data import BotDB
from config import url, token_bot, basa_db



bot = Bot(token=token_bot)
BotDB = BotDB(basa_db)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)



def send_text_to_all(text: str):
    for i in BotDB.get_all_id():
        send_all_user(i, text)



def pars(url):
    try:
        while True:
            if parsersite(url) == True:
                print("Server online")
                send_text_to_all("Сервер доступний")
                time.sleep(60)
            elif parsersite(url) == False:
                print("Server offline")
                send_text_to_all("Сервер тимчасово недоступний")
                time.sleep(500)
            else:
                print("pars_else 404")

    except:
        print("pars 404")




@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Так! почати моніторинг", "Ні, не треба"]
    keyboard.add(*buttons)
    await message.answer("Повідомити коли сервер  -dayz- буде offline?", reply_markup=keyboard)




@dp.message_handler(lambda message: message.text == "Так! почати моніторинг")
async def without_puree(message: types.Message):

    user_id = message.from_user.id
    first_name = message.from_user.first_name
    username = message.from_user.username
    data = [user_id, first_name, username]

    if (not BotDB.user_exists(user_id)):
        BotDB.add_user(data)

        print(f"{data} - користувача додано до бази")
    await message.reply(f"Дякую {first_name}, {username}! Ми повідомимо вас коли сервер буде недоступний.", reply_markup=types.ReplyKeyboardRemove())
    pars(url)





@dp.message_handler(lambda message: message.text == "Ні, не треба")
async def without_puree(message: types.Message):
    await message.reply(f"Добре до зустрічі {message.from_user.username}.", reply_markup=types.ReplyKeyboardRemove())









# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

