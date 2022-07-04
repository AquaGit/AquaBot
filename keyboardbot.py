from telebot.types import ReplyKeyboardMarkup


class Keyboard:
    def __new__ (self, *buttons) -> ReplyKeyboardMarkup:
        keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
        _ = [keyboard.add(*i) for i in buttons]
        
        return keyboard

    @classmethod
    def menu(cls):
        return Keyboard((Message.GAMES, Message.WEATHER, Message.ABOUT, Message.MUSIC ))

    @classmethod
    def games(cls):
        return Keyboard((Message.MVCBOOK, Message.COIN, Message.BACK))

    @classmethod
    def weather(cls):
        return Keyboard((Message.LOCAL, Message.BACK))

    @classmethod
    def music(cls):
        return Keyboard((Message.RANDOM, Message.PLAYLIST, Message.ADDTRACK, Message.BACK))

    @classmethod
    def about(cls):
        return Keyboard((Message.INSTAGRAM, Message.TELEGRAM, Message.BACK))

class Message:
# MAIN MENU
    GAMES = 'GAMES'
    WEATHER = 'WEATHER'
    ABOUT = 'ABOUT'
    MUSIC = 'MUSIC'
# GAMES MENU
    MVCBOOK = 'MVCBOOK GAME'
    COIN = 'COIN GAME'
    BACK = 'BACK'
# WEATHER MENU
    LOCAL = 'LOCAL WEATHER'
# MUSIC MENU
    RANDOM = 'RANDOM'
    PLAYLIST = 'PLAYLIST'
    ADDTRACK = 'ADD TRACK'
# ABOUT MENU
    INSTAGRAM = 'INSTAGRAM'
    TELEGRAM = 'TELEGRAM'
    


