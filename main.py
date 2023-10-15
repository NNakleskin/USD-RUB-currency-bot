import logging
from os import getenv
from aiogram import Bot, types
from aiogram.utils import executor
from aiogram.dispatcher import Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher.filters import Command
from dotenv import load_dotenv
import firebase_admin
from firebase_admin import credentials, db
import requests

load_dotenv()

cred = credentials.Certificate("DB_Key.json")
default_app = firebase_admin.initialize_app(cred, {
	'databaseURL': getenv("FIREBASE_URL")
	})
DBRef = db.reference("/commission")


bot = Bot(token=getenv("BOT_TOKEN"), parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)
logging.basicConfig(format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s',
                    level=logging.INFO)



def get_exchange_rate_CB():
    url = 'https://www.cbr-xml-daily.ru/daily_json.js'
    response = requests.get(url)
    data = response.json()
    usd_rate = data['Valute']['USD']['Value']
    return usd_rate


def get_exchange_rate_Tinkoff():
    url = 'https://api.tinkoff.ru/v1/currency_rates'
    params = {
        'fromCurrency': 'RUB',
        'toCurrency': 'USD'
    }
    response = requests.get(url, params=params)
    data = response.json()
    usd_rate = data['payload']['rates'][0]['buy']
    return usd_rate


@dp.message_handler(Command("help"), state=None)
async def start(message):
    await bot.send_message(
        message.chat.id, 
        text="/start - запуск бота\n/get_Tinkoff - получение актуального курса по Тинькофф\n/get_CB - получение актуального курса по ЦБ"
        )


@dp.message_handler(Command("start"), state=None)
async def start(message):
    await bot.send_message(
        message.chat.id, 
        text="Добрый день! Данный бот предназначен для получения курса доллара с учетом комиссии платформы!\nЕсли нужна помощь пиши /help)"
        )


@dp.message_handler(Command("get_CB"), state=None)
async def get(message):
    commission = DBRef.get("comission")
    current_rate = get_exchange_rate_CB() * (1 + float(commission[0]))
    await bot.send_message(
        message.chat.id, 
        text="Актуальный курс доллара по ЦБ {}".format(current_rate)
        )


@dp.message_handler(Command("get_Tinkoff"), state=None)
async def get(message):
    commission = DBRef.get("comission")
    current_rate = get_exchange_rate_CB() * (1 + float(commission[0]))
    await bot.send_message(
        message.chat.id, 
        text="Актуальный курс доллара по Тинькофф {}".format(current_rate)
        )


if __name__ == "__main__":
    executor.start_polling(dp)