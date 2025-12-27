from aiogram import Bot, Dispatcher, executor, types
import openai
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
OPENAI_KEY = os.getenv("OPENAI_KEY")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

openai.api_key = OPENAI_KEY


@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    await message.reply(
        "Salom! 🤖\n"
        "Men Uzbek GPT botman.\n\n"
        "Savolingizni yozing."
    )


@dp.message_handler()
async def chat_handler(message: types.Message):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": message.text}
            ]
        )
        await message.reply(response.choices[0].message.content)

    except Exception as e:
        await message.reply("❌ Xatolik yuz berdi. Keyinroq urinib ko‘ring.")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
