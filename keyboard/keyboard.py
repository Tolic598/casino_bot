from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb = [
        [KeyboardButton(text="Слоты")],
        [KeyboardButton(text="Профиль")],
        [KeyboardButton(text="Статистика")],
        [KeyboardButton(text="Поддержать проект")]
    ]

menu = ReplyKeyboardMarkup(keyboard=kb)