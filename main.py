from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo

TOKEN = "6276511476:AAFHVI04utaQGATEC3UKN9RCpFTi6dDUUPg"

bot = Bot(TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton('Web yala kun', web_app=WebAppInfo(url="https://crmneo.com/")))
    await bot.send_message(message.chat.id, 'Hello ot alirizo', reply_markup=markup)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
