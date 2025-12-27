import asyncio
import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from openai import OpenAI

BOT_TOKEN = os.getenv("BOT_TOKEN")
OPENAI_KEY = os.getenv("OPENAI_KEY")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

client = OpenAI(api_key=OPENAI_KEY)

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer("Salom! 🤖\nSavolingizni yozing.")

@dp.message()
async def chat(message: types.Message):
    try:
        resp = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": message.text}]
        )
        await message.answer(resp.choices[0].message.content)
    except Exception as e:
        await message.answer("Xatolik yuz berdi.")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
