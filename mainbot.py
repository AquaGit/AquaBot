from email import message
import telebot
import os
from dotenv import load_dotenv
from keyboardbot import Keyboard

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")

bot_token = TOKEN
bot = telebot.TeleBot(token=bot_token)

# bot menu
@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(
        message.chat.id,
        f"Салют, {message.from_user.first_name}!",
        reply_markup=Keyboard.menu())

@bot.message_handler(content_types=["text"])
def bot_message(message):
    if message.text == "GAMES":
        bot.send_message(message.chat.id, f"Обрано {message.text}", reply_markup=Keyboard.games())
    elif message.text == "WEATHER":
        bot.send_message(message.chat.id, f"Обрано {message.text}", reply_markup=Keyboard.weather())
    elif message.text == "MUSIC":
        bot.send_message(message.chat.id, f"Обрано {message.text}", reply_markup=Keyboard.music())
    elif message.text == "ABOUT":
        bot.send_message(message.chat.id, f"Обрано {message.text}", reply_markup=Keyboard.about())
    elif message.text == "BACK":
        bot.send_message(message.chat.id, f"Повертаємось назад", reply_markup=Keyboard.menu())

bot.polling(none_stop=True)
