import asyncio
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.dispatcher.filters import Text
from freeGPT import Client
from googletrans import Translator

bot = Bot(token='6846549120:AAHWXClbIO1iBFl-NhKOeY9ukPfpgibtBSw')
dp = Dispatcher(bot)
translator = Translator()
text = " "
target_language = 'ru'

"""
while True:
    prompt = input("👦: ")
    try:
        resp = Client.create_completion("gpt3", prompt)
        print(f"🤖: {resp}")
    except Exception as e:
        print(f"🤖: {e}")"""


async def generate_response(message_text):
    try:
        response = Client.create_completion("gpt3", message_text)
        result = translator.translate(response, dest=target_language)
        result = result.text
        # print(result)
        return result
    except:
        print("error")

@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.reply("Привет это бесплатный бот для генерации текста. Спомощю модели GPT4.0")


@dp.message_handler(commands=["help"])
async def help_command(message: types.Message):
    await message.reply("Привет!\nЧтобы я отправил тебе сгенирированый текст по твоему запросу ты должен мне написать свой запрос\nИ я отправлю тебе сгенирированный ответ на товой запрос!")

@dp.message_handler(content_types=types.ContentType.TEXT)
async def gpt_generate(message: types.Message):
    await message.reply("Генерация текста")
    try:
        result = await generate_response(message.text)
        await message.reply(result)
    except:
        await message.reply("Произошла ошибка при генерации текста по вашему запросу")

#keep_alive()

if __name__ == '__main__':
    executor.start_polling(dp) 