from aiogram import types, Router
from Database.requests import get_ciders_it

router = Router()


async def get_italy_cider(message: types.Message):
    ciders = await get_ciders_it()
    message_text = ""
    if ciders:
        for cider in ciders:
            message_text += (f"<b>Название: </b>\n{cider.name}\n"
                             f"<b>Производитель: </b>\n{cider.manufacture}\n"
                             f"<b>Регион: </b>\n{cider.region}\n"
                             f"<b>Сухость: </b>\n{cider.sour}\n"
                             f"<b>Содержание алкоголя:</b> {cider.alco}\n"
                             f"<i>Описание:</i>\n{cider.description}\n"
                             "___________________________________"
                             "\n"
                             )
        await message.answer(
            text=message_text,
            parse_mode="HTML",
            reply_markup=list_button()
        )
    else:
        await message.answer("Информация о напитке не найдена")


def list_button():
    list_btn = [

        [types.InlineKeyboardButton(text="Назад к Странам", callback_data="back_to_country")],
    ]
    list_btn = types.InlineKeyboardMarkup(inline_keyboard=list_btn)
    return list_btn
