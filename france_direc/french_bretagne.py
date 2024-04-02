from aiogram import F, types, Router

from Database.requests import get_ciders_fr

router = Router()


@router.callback_query(F.data == "bretagne")
async def send_bretagne(callback: types.CallbackQuery):
    await callback.message.edit_text(text='Отлично! Что интересно дальше?', reply_markup=bretagne_cider_btn())


def bretagne_cider_btn():
    buttons = [
        [types.InlineKeyboardButton(text='Brut Taditionnel', callback_data="trad_bretagne"),
         types.InlineKeyboardButton(text='Brut', callback_data="brut_bretagne")],
        [types.InlineKeyboardButton(text='Demisec', callback_data="demisec_bretagne"),
         types.InlineKeyboardButton(text='Doux', callback_data="doux_bretagne")],
        [types.InlineKeyboardButton(text="Назад", callback_data="back_to_extra_doux")],
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


async def send_manufactor_bretagne(callback: types.CallbackQuery, region: str, sour: str):
    ciders = await get_ciders_fr(f"{sour}", f"{region}")
    message_text = ""
    if ciders:
        for cider in ciders:
            message_text += (f"<b>Название - </b>{cider.name}\n"
                             f"<b>Сухость -</b> {cider.sour}\n"
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

        [types.InlineKeyboardButton(text="Назад", callback_data="bretagne")],
    ]
    list_btn = types.InlineKeyboardMarkup(inline_keyboard=list_btn)
    return list_btn


@router.callback_query(F.data == "trad_bretagne")
async def send_trad_bretagne(callback: types.CallbackQuery):
    await send_manufactor_bretagne(callback, "Бретань", "Brut Taditionnel")


@router.callback_query(F.data == "brut_bretagne")
async def send_brut_bretagne(callback: types.CallbackQuery):
    await send_manufactor_bretagne(callback, "Бретань", "Brut")


@router.callback_query(F.data == "demisec_bretagne")
async def send_demisec_bretagne(callback: types.CallbackQuery):
    await send_manufactor_bretagne(callback, "Бретань", "Demisec")


@router.callback_query(F.data == "doux_bretagne")
async def send_doux_bretagne(callback: types.CallbackQuery):
    await send_manufactor_bretagne(callback, "Бретань", "Doux")
