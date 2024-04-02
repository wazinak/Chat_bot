from aiogram import F, types, Router

from Database.requests import get_ciders_fr, get_ciders_fr_brut

router = Router()


@router.callback_query(F.data == "normandy")
async def send_dry(callback: types.CallbackQuery):
    await callback.message.edit_text(text='Отлично! Что интересно дальше?', reply_markup=norman_cider_btn())


def norman_cider_btn():
    buttons = [
        [types.InlineKeyboardButton(text="Extra-Brut", callback_data="extra_normandy"),
         types.InlineKeyboardButton(text='Brut', callback_data="brut_normandy")],
        [types.InlineKeyboardButton(text='Demisec', callback_data="demisec_normandy"),
         types.InlineKeyboardButton(text='Doux', callback_data="doux_normandy")],
        [types.InlineKeyboardButton(text="Назад", callback_data="back_to_extra_doux")],
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


async def send_manufactor_normandy(callback: types.CallbackQuery, region: str, sour: str):
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

        [types.InlineKeyboardButton(text="Назад", callback_data="normandy")],
    ]
    list_btn = types.InlineKeyboardMarkup(inline_keyboard=list_btn)
    return list_btn


@router.callback_query(F.data == "extra_normandy")
async def send_extra_normandy(callback: types.CallbackQuery):
    await send_manufactor_normandy(callback, "Нормандия", "Extra-Brut")


@router.callback_query(F.data == "demisec_normandy")
async def send_demisec_normandy(callback: types.CallbackQuery):
    await send_manufactor_normandy(callback, "Нормандия", "Demisec")


@router.callback_query(F.data == "doux_normandy")
async def send_doux_normandy(callback: types.CallbackQuery):
    await send_manufactor_normandy(callback, "Нормандия", "Doux")


@router.callback_query(F.data == "brut_normandy")
async def send_brut_normandy(callback: types.CallbackQuery):
    await callback.message.edit_text(text='Здесь у нас по интереснее, прошу выбрать производителя',
                                     reply_markup=norman_brut_cider_btn())


def norman_brut_cider_btn():
    buttons = [
        [types.InlineKeyboardButton(text="La Cave Normande", callback_data="la_cave_normandy"),
         types.InlineKeyboardButton(text='Eric Bordelet', callback_data="eric_normandy")],
        [types.InlineKeyboardButton(text='Maison Herout', callback_data="herout_normandy"),
         types.InlineKeyboardButton(text='Christian Drouin', callback_data="christian_normandy")],
        [types.InlineKeyboardButton(text='Cidrerie de la Brique', callback_data="chevre_normandy"),
         types.InlineKeyboardButton(text='Pere Magloire', callback_data="magloire_normandy")],
        [types.InlineKeyboardButton(text='Duche de Longueville', callback_data="Duche_norman"),
         types.InlineKeyboardButton(text='Fournier', callback_data="Fournier_noramndy")],
        [types.InlineKeyboardButton(text='Vergers de Romilly', callback_data="vergers_normandy"),
         types.InlineKeyboardButton(text='Le Pere Jules', callback_data="jules_normandy")],
        [types.InlineKeyboardButton(text='Le Paulmier', callback_data="Paulmier_normandy")],
        [types.InlineKeyboardButton(text="Назад", callback_data="normandy")],
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


async def send_manufactor_normandy_brut(callback: types.CallbackQuery, region: str, manufacture: str):
    ciders = await get_ciders_fr_brut(f"{region}", f"{manufacture}")
    message_text = ""
    if ciders:
        for cider in ciders:
            message_text += (f"<b>Название - </b>{cider.name}\n"
                             f"<b>Сухость - </b>{cider.sour}\n"
                             f"<b>Содержание алкоголя:</b> {cider.alco}\n"
                             f"<i>Описание:</i>\n{cider.description}\n"
                             "__________________"
                             "\n"
                             )
        await callback.answer('')
        await callback.message.edit_text(
            text=message_text,
            parse_mode="HTML",
            reply_markup=list_button_brut()
        )
    else:
        await callback.answer("Информация о напитке не найдена")


def list_button_brut():
    list_btn = [

        [types.InlineKeyboardButton(text="Назад", callback_data="brut_normandy")],
    ]
    list_btn = types.InlineKeyboardMarkup(inline_keyboard=list_btn)
    return list_btn


@router.callback_query(F.data == "Duche_norman")
async def send_la_cave_normandy(callback: types.CallbackQuery):
    await send_manufactor_normandy_brut(callback, "Нормандия", "Duche de Longueville")


@router.callback_query(F.data == "Fournier_noramndy")
async def send_la_cave_normandy(callback: types.CallbackQuery):
    await send_manufactor_normandy_brut(callback, "Нормандия", "Fournier")


@router.callback_query(F.data == "vergers_normandy")
async def send_la_cave_normandy(callback: types.CallbackQuery):
    await send_manufactor_normandy_brut(callback, "Нормандия", "Vergers de Romilly")


@router.callback_query(F.data == "Paulmier_normandy")
async def send_la_cave_normandy(callback: types.CallbackQuery):
    await send_manufactor_normandy_brut(callback, "Нормандия", "Le Paulmier")


@router.callback_query(F.data == "la_cave_normandy")
async def send_la_cave_normandy(callback: types.CallbackQuery):
    await send_manufactor_normandy_brut(callback, "Нормандия", "La Cave Normande")


@router.callback_query(F.data == "eric_normandy")
async def send_eric_normandy(callback: types.CallbackQuery):
    await send_manufactor_normandy_brut(callback, "Нормандия", "Eric Bordelet")


@router.callback_query(F.data == "herout_normandy")
async def send_herout_normandy(callback: types.CallbackQuery):
    await send_manufactor_normandy_brut(callback, "Нормандия", "Maison Herout")


@router.callback_query(F.data == "christian_normandy")
async def send_christian_normandy(callback: types.CallbackQuery):
    await send_manufactor_normandy_brut(callback, "Нормандия", "Christian Drouin")


@router.callback_query(F.data == "chevre_normandy")
async def send_chevre_normandy(callback: types.CallbackQuery):
    await send_manufactor_normandy_brut(callback, "Нормандия", "Cidrerie de la Brique")


@router.callback_query(F.data == "magloire_normandy")
async def send_magloire_normandy(callback: types.CallbackQuery):
    await send_manufactor_normandy_brut(callback, "Нормандия", "Pere Magloire")


@router.callback_query(F.data == "jules_normandy")
async def send_jules_normandy(callback: types.CallbackQuery):
    await send_manufactor_normandy_brut(callback, "Нормандия", "Le Pere Jules")
