import logging
import wikipedia

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '1875124545:AAEMW0TgBXqGEGycf-JWWMN4snVYKAVjLwE'
wikipedia.set_lang('uz')

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
   Start yoki Help tugamasi bosilganda
    """
    await message.reply("Wikipeida Botiga Xush Kelibsiz! Nurbek tomonidan yaratilgan")

@dp.message_handler()
async def sendWiki(message: types.Message):
    print(message.chat.id)
    try:
        respond = wikipedia.summary(message.text)
        await message.answer(respond)
    except:
        await message.answer("Bu mavzuga oid maqola topilmadi")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)