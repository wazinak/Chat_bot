from aiogram import F, types, Router

from Database.requests import get_ciders_sp

router = Router()


@router.callback_query(F.data == "extra-dry")
async def spain_region_cider(callback: types.CallbackQuery):
    await callback.message.edit_text(
        text="Какой регион ты выберешь?",
        reply_markup=spain_region()
    )


def spain_region():
    buttons = [
            [types.InlineKeyboardButton(text='Астурия', callback_data="asturia")],
            [types.InlineKeyboardButton(text='Страна Басков', callback_data="baskov")],
            [types.InlineKeyboardButton(text="Вернуться к сухости", callback_data="back_to_extra_dulce")],

        ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


@router.callback_query(F.data == "asturia")
async def spain_brut_cider(callback: types.CallbackQuery, sour='Extra-Dry', region= 'Астурия'):
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


@router.callback_query(F.data == "baskov")
async def spain_brut_cider(callback: types.CallbackQuery, sour='Extra-Dry', region= 'Страна Басков'):
    ciders = await get_ciders_sp(f"{sour}", f"{region}")
    message_text = ""
    if ciders:
        for cider in ciders:
            message_text += (f"<b>Название:</b>\n{cider.name}\n"
                             f"<b>Содержание алкоголя:</b> {cider.alco}\n"
                             f"<b>Регион:</b> {cider.region}\n"
                             f"<i>Описание:</i>\n{cider.description}\n"
                             "__________________"
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

        [types.InlineKeyboardButton(text="Назад к сухости", callback_data="extra-dry")],
    ]
    list_btn = types.InlineKeyboardMarkup(inline_keyboard=list_btn)
    return list_btn
