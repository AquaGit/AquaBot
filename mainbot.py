import telebot
import os
from dotenv import load_dotenv
from keyboardbot import Keyboard
from games import orel_reshka, mvcbookarmy


load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")

bot_token = TOKEN
bot = telebot.TeleBot(token=bot_token)

# bot menu
@bot.message_handler(commands=["start", "help"])
def start(message):
    bot.send_message(
        message.chat.id,
        f"Салют, {message.from_user.first_name}!\nБот Назара Лютого готовий до роботи\nМожеш подивитись який я Босс!",
        reply_markup=Keyboard.menu(),
    )
    photo = open("photo/aquaphoto.jpg", "rb")
    bot.send_photo(message.chat.id, photo)

    # bot.send_message(
    #     message.chat.id, "for now i have only commands\n/start\n/music\n/games\n"
    # )

bot.polling(none_stop=True)
