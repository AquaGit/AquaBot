from telebot.types import ReplyKeyboardMarkup
from message import Message

class Keyboard:
    def __new__ (self, *buttons) -> ReplyKeyboardMarkup:
        keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
        _ = [keyboard.add(*i) for i in buttons]
        
        return keyboard

    @classmethod
    def menu(Keyboard):
        return Keyboard((Message.GAMES,), (Message.TODOLIST, Message.WEATHER, Message.ABOUT ))