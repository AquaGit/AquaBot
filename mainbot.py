import telebot
from telebot import types
from dotenv import load_dotenv
from keyboard import Keyboard
import os
import random

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")

bot_token = TOKEN
bot = telebot.TeleBot(token=bot_token)

# bot menu
@bot.message_handler(commands=["start", "help"])
def start(message):
    bot.send_message(message.chat.id, f"Салют, {message.from_user.first_name}\n")
    bot.reply_to(
        message,
        "Тепер я вмію відповідати на твої повідомлення! :)\nА вот з клавіатурою траблс братан :(\nЯкщо знаєш як пиши сюда @uknowimaqua",
    )
    bot.reply_markup(Keyboard.menu)


# add menu
@bot.message_handler(content_types=["text"])
def bot_message(message):
    if message.chat.type == "private":
        if message.text == "🎮 Ігри":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item4 = types.KeyboardButton("🤔 Чи здасть Богдан курсову?")
            item5 = types.KeyboardButton("🦅 Орел Решка")
            back = types.KeyboardButton("↩ Назад")
            markup.add(item4, item5, back)

            bot.send_message(
                message.chat.id,
                "Обрано: 🎮 ".format(message.from_user),
                reply_markup=markup,
            )

        elif message.text == "🦅 Орел Решка":
            bot.send_message(message.chat.id, "Підкидую монетку\nУхх...\n")
            orel_reshka = [
                "Вам випав Орел\n🦅",
                "Вам випала Решка\n🔱",
                "Монетка загубилася...\n😔",
            ]
            bot.send_message(message.chat.id, random.choice(orel_reshka))

        elif message.text == "🤔 Чи здасть Богдан курсову?":
            bot.send_message(
                message.chat.id,
                "Хм...\nДивлячись як він старається\nЯ думаю...",
            )
            mvcbookarmy = [
                "Перездача 😔",
                "Армія 😬",
                "Здасть 🙂",
                "Богдан здасть і стане програмістом 💻",
                "Заплатить бабки 💸",
                "Курсова здасть Богдана 🧐",
                "Стане автомеханіком 🏎",
                "Відкриє свій політех і здасть сам собі курсову 🦉",
            ]
            bot.send_message(message.chat.id, random.choice(mvcbookarmy))

        elif message.text == "🌡️ Погода":
            bot.send_message(message.chat.id, "Обрано: 🌡️\nУ розробці")

        elif message.text == "📞 Зв'язок":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item6 = types.KeyboardButton("📷 Instagram")
            item7 = types.KeyboardButton("📲 Telegram")
            back = types.KeyboardButton("↩ Назад")
            markup.add(item6, item7, back)

            bot.send_message(
                message.chat.id,
                "Обрано: 📞 ".format(message.from_user),
                reply_markup=markup,
            )

        elif message.text == "📷 Instagram":
            bot.send_message(message.chat.id, "📷 Instagram\n@areyouaqua")

        elif message.text == "📲 Telegram":
            bot.send_message(message.chat.id, "📱 TELEGRAM AQUA 📱\n@areyouaqua")

        elif message.text == "💎 Todolist":
            bot.send_message(message.chat.id, "Аква думає як таку штуку зробити 🤔")

        else:
            bot.send_message(message.chat.id, "Не зрозумів тебе 😬")


bot.polling(none_stop=True)
