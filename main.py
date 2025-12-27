import telebot
import openai
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
OPENAI_KEY = os.getenv("OPENAI_KEY")

bot = telebot.TeleBot(BOT_TOKEN)
openai.api_key = OPENAI_KEY

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Salom! 🤖\nSavolingizni yozing.")

@bot.message_handler(func=lambda m: True)
def chat(message):
    try:
        resp = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": message.text}]
        )
        bot.reply_to(message, resp.choices[0].message.content)
    except:
        bot.reply_to(message, "Xatolik yuz berdi.")

bot.infinity_polling()
