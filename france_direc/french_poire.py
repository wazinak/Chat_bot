from aiogram import F, types, Router

from Database.requests import get_ciders_poire

router = Router()


@router.callback_query(F.data == "poire")
async def send_brut_normandy(callback: types.CallbackQuery):
    await callback.message.edit_text(text='Здесь у нас по интереснее, прошу выбрать производителя',
                                     reply_markup=poire_manufacture_cider_btn())


def poire_manufacture_cider_btn():
    buttons = [
        [types.InlineKeyboardButton(text="Les Bulles  Ardennaises", callback_data="bulles_poire"),
         types.InlineKeyboardButton(text='Le Pere Jules', callback_data="pere_poire")],
        [types.InlineKeyboardButton(text='Kerisac', callback_data="kerisak_poire"),
         types.InlineKeyboardButton(text='Duche de Longueville', callback_data="duche_poire")],
        [types.InlineKeyboardButton(text='Chevre de Valognes', callback_data="chevre_poire"),
         types.InlineKeyboardButton(text='Cidreire de La Brique', callback_data="le_clos_poire")],
        [types.InlineKeyboardButton(text='Sorre', callback_data="sorre_poire"),
         types.InlineKeyboardButton(text='Le Paulmier', callback_data="paumier_poire")],
        [types.InlineKeyboardButton(text='La Cave Normande', callback_data="cave_poire"),
         types.InlineKeyboardButton(text='Fournier', callback_data="fournier_poire")],
        [types.InlineKeyboardButton(text='Eric Bordelet', callback_data="eric_poire")],
        [types.InlineKeyboardButton(text="Назад", callback_data="back_to_extra_doux")],
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


async def send_poire(callback: types.CallbackQuery, manufacture:str):
    ciders = await get_ciders_poire(f"{manufacture}")
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

        [types.InlineKeyboardButton(text="Назад", callback_data="poire")],
    ]
    list_btn = types.InlineKeyboardMarkup(inline_keyboard=list_btn)
    return list_btn


@router.callback_query(F.data == "bulles_poire")
async def send_bulles_poire(callback: types.CallbackQuery):
    await send_poire(callback, "Les Bulles  Ardennaises")


@router.callback_query(F.data == "pere_poire")
async def send_pere_poire(callback: types.CallbackQuery):
    await send_poire(callback, "Le Pere Jules")


@router.callback_query(F.data == "kerisak_poire")
async def send_kerisak_poire(callback: types.CallbackQuery):
    await send_poire(callback, "Kerisac")


@router.callback_query(F.data == "chevre_poire")
async def send_chevre_poire(callback: types.CallbackQuery):
    await send_poire(callback, "Cidrerie de La Brique")


@router.callback_query(F.data == "duche_poire")
async def send_duche_poire(callback: types.CallbackQuery):
    await send_poire(callback, "Duche de Longueville")


@router.callback_query(F.data == "le_clos_poire")
async def send_le_clos_poire(callback: types.CallbackQuery):
    await send_poire(callback, "Cidreire de La Brique")


@router.callback_query(F.data == "sorre_poire")
async def send_sorre_poire(callback: types.CallbackQuery):
    await send_poire(callback, "Sorre")


@router.callback_query(F.data == "paumier_poire")
async def send_paumier_poire(callback: types.CallbackQuery):
    await send_poire(callback, "Le Paulmier")


@router.callback_query(F.data == "fournier_poire")
async def send_fournier_poire(callback: types.CallbackQuery):
    await send_poire(callback, "Fournier")


@router.callback_query(F.data == "cave_poire")
async def send_bulles_poire(callback: types.CallbackQuery):
    await send_poire(callback, "La Cave Normande")


@router.callback_query(F.data == "eric_poire")
async def send_bulles_poire(callback: types.CallbackQuery):
    await send_poire(callback, "Eric Bordelet")
