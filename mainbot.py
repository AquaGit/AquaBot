import python_weather
import telebot
from telebot import types
import random
from tunelgame.gamemain import get_map_str, cols, rows, maps
from tunelgame.mg import get_map_cell
from dotenv import load_dotenv
import os

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")

bot_token = TOKEN
bot = telebot.TeleBot(token=bot_token)

# bot menu
@bot.message_handler(commands=["start"])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("🎮 Ігри")
    item2 = types.KeyboardButton("🌡️ Погода")
    item3 = types.KeyboardButton("📞 Зв'язок")
    item4 = types.KeyboardButton("🤔Чи здасть Богдан курсову")
    item5 = types.KeyboardButton("🦅 Орел Решка")
    item6 = types.KeyboardButton("📷 Instagram")
    item7 = types.KeyboardButton("📲 Telegram")
    item8 = types.KeyboardButton("👩‍🏭 Tunel")
    item9 = types.KeyboardButton("💎 Todolist")

    markup.add(item1, item2, item3, item9)

    bot.send_message(message.chat.id, f"Салют, {message.from_user.first_name}\nЯ {message.from_user.first_name} ")


# add menu
@bot.message_handler(content_types=["text"])
def bot_message(message):
    if message.chat.type == "private":

        if message.text == "🎮 Ігри":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item4 = types.KeyboardButton("🤔 Чи здасть Богдан курсову?")
            item5 = types.KeyboardButton("🦅 Орел Решка")
            item8 = types.KeyboardButton("👩‍🏭 Tunel")
            back = types.KeyboardButton("↩ Назад")
            markup.add(item4, item5, item8, back)

            bot.send_message(
                message.chat.id,
                "Обрано: 🎮 ".format(message.from_user),
                reply_markup=markup,
            )

        elif message.text == "👩‍🏭 Tunel":
            bot.send_message(
                message.chat.id,
                "Обрано: 👩‍🏭",
            )
            bot.send_message(
                message.chat.id,
                "Ваше завдання: дійти до правого нижнього кута по заданому лабіринту.\nУдачі 🖤",
            )

            map_cell = get_map_cell(cols, rows)

            user_data = {"map": map_cell, "x": 0, "y": 0}

            maps[message.chat.id] = user_data

            bot.send_message(
                message.from_user.id,
                get_map_str(map_cell, (0, 0)),
                reply_markup=keyboard,
            )

        elif message.text == "🦅 Орел Решка":
            bot.send_message(message.chat.id, "Підкидую монетку\nУхх...\n")
            orel_reshka = [
                "Вам випав Орел\n🦅",
                "Вам випала Решка\n🔱",
                "Монетка загубилася...\n😔",
            ]
            bot.send_message(message.chat.id, random.choice(orel_reshka))

            # old orel reshka
            # a = str(random.randint(1, 2))
            # if a == "1":
            #     bot.send_message(message.chat.id, "Вам випав Орел\n🦅")
            # else:
            #     bot.send_message(message.chat.id, "Вам випала Решка\n🔱")

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

            # old MVCBOOK ARMY
            # b = str(random.randint(0, 3))
            # if b == "1":
            #     bot.send_message(message.chat.id, "Перездача 😔")
            # elif b == "2":
            #     bot.send_message(message.chat.id, "Армія 😬")
            # else:
            #     bot.send_message(message.chat.id, "Здасть 🙂")

        elif message.text == "🌡️ Погода":
            bot.send_message(message.chat.id, "Обрано: 🌡️\n")

            def getweather():
                client = python_weather.Client(
                    format=python_weather.IMPERIAL, locale="uk-UK"
                )
                weather = client.find("Lviv")
                celsius = (weather.current.temperature - 32) / 1.8
                bot.send_message(message.chat.id, str(round(celsius)) + "°")
                bot.send_message(message.chat.id, weather.current.sky_text)
                bot.send_message(message.chat.id, weather.location_name)

            bot.send_message(message.chat.id, f"Місто {getweather()}")

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

        elif message.text == "↩ Назад":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("🎮 Ігри")
            item2 = types.KeyboardButton("🌡️ Погода")
            item3 = types.KeyboardButton("📞 Зв'язок")
            item4 = types.KeyboardButton("🤔Чи здасть Богдан курсову")
            item5 = types.KeyboardButton("🦅 Орел Решка")
            item6 = types.KeyboardButton("📷 Instagram")
            item7 = types.KeyboardButton("📲 Telegram")
            item8 = types.KeyboardButton("👩‍🏭 Tunel")
            item9 = types.KeyboardButton("💎 Todolist")

            markup.add(item1, item2, item3, item9)

            bot.send_message(
                message.chat.id,
                "Wassup, {0.first_name}!".format(message.from_user),
                reply_markup=markup,
            )

        elif message.text == "💎 Todolist":
            bot.send_message(message.chat.id, "Аква думає як таку штуку зробити 🤔")

        else:
            bot.send_message(message.chat.id, "Не зрозумів тебе 😬")


# tunel game
keyboard = telebot.types.InlineKeyboardMarkup()
keyboard.row(
    telebot.types.InlineKeyboardButton("←", callback_data="left"),
    telebot.types.InlineKeyboardButton("↑", callback_data="up"),
    telebot.types.InlineKeyboardButton("↓", callback_data="down"),
    telebot.types.InlineKeyboardButton("→", callback_data="right"),
)


@bot.callback_query_handler(func=lambda call: True)
def callback_func(query):
    user_data = maps[query.message.chat.id]
    new_x, new_y = user_data["x"], user_data["y"]

    if query.data == "left":
        new_x -= 1
    if query.data == "right":
        new_x += 1
    if query.data == "up":
        new_y -= 1
    if query.data == "down":
        new_y += 1

    if new_x < 0 or new_x > 2 * cols - 2 or new_y < 0 or new_y > rows * 2 - 2:
        return None
    if user_data["map"][new_x + new_y * (cols * 2 - 1)]:
        return None

    user_data["x"], user_data["y"] = new_x, new_y

    if new_x == cols * 2 - 2 and new_y == rows * 2 - 2:
        bot.edit_message_text(
            chat_id=query.message.chat.id,
            message_id=query.message.id,
            text="Чудово! Аква ставить тобі лайк! 👍",
        )
        return None

    bot.edit_message_text(
        chat_id=query.message.chat.id,
        message_id=query.message.id,
        text=get_map_str(user_data["map"], (new_x, new_y)),
        reply_markup=keyboard,
    )


bot.polling(none_stop=True)
