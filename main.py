from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
import openai
import asyncio
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
OPENAI_KEY = os.getenv("OPENAI_KEY")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

openai.api_key = OPENAI_KEY

@dp.message(CommandStart())
async def start(msg: types.Message):
    await msg.answer("Salom! Men Uzbek GPT botman. Savolingizni yozing.")

@dp.message()
async def chat(msg: types.Message):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": msg.text}]
        )
        await msg.answer(response.choices[0].message.content)
    except Exception as e:
        await msg.answer("Xatolik yuz berdi. Iltimos, keyinroq urinib ko‘ring.")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
