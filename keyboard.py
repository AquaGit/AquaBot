from telebot.types import ReplyKeyboardMarkup
from message import Message


class Keyboard:
    def __new__(self) -> ReplyKeyboardMarkup:
        keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

        return keyboard

    @classmethod
    def menu(Keyboard):
        return Keyboard(
            (Message.GAMES,), (Message.TODOLIST, Message.WEATHER, Message.ABOUT)
        )
