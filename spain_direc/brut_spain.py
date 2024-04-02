from aiogram import F, types, Router
from Database.requests import get_ciders_sp

router = Router()


# async def send_dry(callback: types.CallbackQuery):
#     await callback.message.edit_text(text='Отлично! Вот что у меня есть!', reply_markup=spain_brut_cider())

@router.callback_query(F.data == "brut_spain")
async def spain_brut_cider(callback: types.CallbackQuery, sour='Brut', region='Астурия'):
    ciders = await get_ciders_sp(f"{sour}", f"{region}")
    message_text = ""
    if ciders:
        for cider in ciders:
            message_text += (f"<b>Название:</b>\n{cider.name}\n"
                             f"<b>Содержание алкоголя:</b> {cider.alco}\n"
                             f"<b>Регион:</b> {cider.region}\n"
                             f"<i>Описание:</i>\n{cider.description}\n"
                             "___________________________________"
                             "\n"
                             )
        await callback.answer('')
        await callback.message.edit_text(
            text=message_text,
            parse_mode="HTML",
            reply_markup=list_button()
        )
    else:
        await callback.answer("Информация о напитке не найдена")


def list_button():
    list_btn = [

        [types.InlineKeyboardButton(text="Назад к сухости", callback_data="back_to_extra_dulce")],
    ]
    list_btn = types.InlineKeyboardMarkup(inline_keyboard=list_btn)
    return list_btn
