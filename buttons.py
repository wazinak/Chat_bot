from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from info_text import LEXICON, lEXI_CONCEPTS


def get_cider_counrty_kb():
    kb = [
        [types.KeyboardButton(text="Франция"),
         types.KeyboardButton(text="Россия")],
        [types.KeyboardButton(text="Испания"),
         types.KeyboardButton(text="Англия")],
        [types.KeyboardButton(text="Италия"),
         types.KeyboardButton(text="Германия")]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        one_time_keyboard=True,
    )
    return keyboard


def info_btn():
    buttons = [
        [types.InlineKeyboardButton(text='История сидра', callback_data="history_cider")],
        [types.InlineKeyboardButton(text='Основные понятия и термины', callback_data="basic_concepts")],
        [types.InlineKeyboardButton(text='Классификация сидров', callback_data="classific_ciders")],
        [types.InlineKeyboardButton(text="Способы подачи сидра", callback_data="podacha_cider")],

    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


def basic_concepts_btn(width: int,
                       *args: str,
                       **kwargs: str) -> InlineKeyboardMarkup:
    kb_builder = InlineKeyboardBuilder()
    # Инициализируем список для кнопоку
    buttons: list[InlineKeyboardButton] = []
    # Заполняем список кнопками из аргументов args и kwargs
    if args:
        for button in args:
            buttons.append(InlineKeyboardButton(
                text=lEXI_CONCEPTS[button] if button in lEXI_CONCEPTS else button,
                callback_data=button))
    if kwargs:
        for button, text in kwargs.items():
            buttons.append(InlineKeyboardButton(
                text=text,
                callback_data=button))
    # распаковываем список с кнопками в билдер методом row с параметром width
    kb_builder.row(*buttons, width=width)

    return kb_builder.as_markup()


# Функция генерирует кнопки
def create_pagination_keyboard(*buttons: str) -> InlineKeyboardMarkup:
    kb_builder = InlineKeyboardBuilder()
    kb_builder.row(*[InlineKeyboardButton(
        text=LEXICON[button] if button in LEXICON else button,
        callback_data=button) for button in buttons], width=3)
    return kb_builder.as_markup()


def random_btn():
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(text="Рандомный сидр!", callback_data="random_value"))
    return builder.as_markup()


def podacha_btn():
    buttons = [
        [types.InlineKeyboardButton(text='Испания', callback_data="podacha_spain")],
        [types.InlineKeyboardButton(text='Франция', callback_data="podacha_french")],
        [types.InlineKeyboardButton(text='Англия', callback_data="podacha_uk")],
        [types.InlineKeyboardButton(text="Вернуться", callback_data="return")],

    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


def back_btn():
    buttons = [
        [types.InlineKeyboardButton(text="Вернуться", callback_data="basic_concepts")],
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


def back_podacha_btn():
    buttons = [
        [types.InlineKeyboardButton(text="Вернуться", callback_data="podacha_cider")],
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard
