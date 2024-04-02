from aiogram import F, types, Router
from Database.requests import get_ciders_rus

router = Router()


@router.callback_query(F.data == "dry")
async def send_manufacture(callback: types.CallbackQuery):
    await callback.message.edit_text(text='От какого производителя интересен сидр? ',
                                     reply_markup=manufacture_btn_dry())


def manufacture_btn_dry():
    manufacture_btn = [
        [types.InlineKeyboardButton(text='Andreev Ciderworks', callback_data="andreev_dry"),
         types.InlineKeyboardButton(text="Gravity Project", callback_data="gravity_dry")],
        [types.InlineKeyboardButton(text='Brodilka', callback_data="brodilka_dry"),
         types.InlineKeyboardButton(text="Bullevie", callback_data="bullevie_dry"),
         types.InlineKeyboardButton(text="Poma", callback_data="poma_dry")],
        [types.InlineKeyboardButton(text="Rebel Apple", callback_data="rebel_dry"),
         types.InlineKeyboardButton(text="Абрау Дюрсо", callback_data="abra_dry")],
        [types.InlineKeyboardButton(text="Русская Нормандия", callback_data="r_normand_dry"),
         types.InlineKeyboardButton(text="Заповедник", callback_data="zapad_dry")],
        [types.InlineKeyboardButton(text="Ля Фуар", callback_data="lya_dry"),
         types.InlineKeyboardButton(text="Октябрь", callback_data="october_dry"),
         types.InlineKeyboardButton(text="Птицы", callback_data="bird_dry")],
        [types.InlineKeyboardButton(text="Токсовская Сидрерия", callback_data="toksovo_dry"),
         types.InlineKeyboardButton(text="Трубачеевка", callback_data="truba_dry")],
        [types.InlineKeyboardButton(text="Try Wild", callback_data="wild_dry")],

        [types.InlineKeyboardButton(text="Назад", callback_data="back_to_sour_sweet")],
    ]
    manufacture_keyboard = types.InlineKeyboardMarkup(inline_keyboard=manufacture_btn)
    return manufacture_keyboard


async def send_manufactor_dry(callback: types.CallbackQuery, manufacture: str, sour="Сухой"):
    ciders = await get_ciders_rus(f"{manufacture}", f"{sour}")
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

        [types.InlineKeyboardButton(text="Назад к Сидроделу", callback_data="dry")],
    ]
    list_btn = types.InlineKeyboardMarkup(inline_keyboard=list_btn)
    return list_btn


@router.callback_query(F.data == "andreev_dry")
async def andreev_dry(callback: types.CallbackQuery):
    await send_manufactor_dry(callback, 'Andreev Ciderworks')


@router.callback_query(F.data == "gravity_dry")
async def gravity_dry(callback: types.CallbackQuery):
    await send_manufactor_dry(callback, 'Gravity Project')


@router.callback_query(F.data == "brodilka_dry")
async def brodilka_dry(callback: types.CallbackQuery):
    await send_manufactor_dry(callback, 'Brodilka')


@router.callback_query(F.data == "bullevie_dry")
async def bullevie_dry(callback: types.CallbackQuery):
    await send_manufactor_dry(callback, 'Bullevie')


@router.callback_query(F.data == "poma_dry")
async def poma_dry(callback: types.CallbackQuery):
    await send_manufactor_dry(callback, 'Poma')


@router.callback_query(F.data == "rebel_dry")
async def rebel_dry(callback: types.CallbackQuery):
    await send_manufactor_dry(callback, 'Rebel Apple')


@router.callback_query(F.data == "abra_dry")
async def abra_dry(callback: types.CallbackQuery):
    await send_manufactor_dry(callback, 'Абрау Дюрсо')


@router.callback_query(F.data == "r_normand_dry")
async def r_normand_dry(callback: types.CallbackQuery):
    await send_manufactor_dry(callback, 'Русская Нормандия')


@router.callback_query(F.data == "zapad_dry")
async def zapad_dry(callback: types.CallbackQuery):
    await send_manufactor_dry(callback, 'Заповедник')


@router.callback_query(F.data == "lya_dry")
async def lya_dry(callback: types.CallbackQuery):
    await send_manufactor_dry(callback, 'Ля Фуар')


@router.callback_query(F.data == "october_dry")
async def october_dry(callback: types.CallbackQuery):
    await send_manufactor_dry(callback, 'Октябрь')


@router.callback_query(F.data == "bird_dry")
async def bird_dry(callback: types.CallbackQuery):
    await send_manufactor_dry(callback, 'Птицы')


@router.callback_query(F.data == "toksovo_dry")
async def toksovo_dry(callback: types.CallbackQuery):
    await send_manufactor_dry(callback, 'Токсовская Сидрерия')


@router.callback_query(F.data == "truba_dry")
async def truba_dry(callback: types.CallbackQuery):
    await send_manufactor_dry(callback, 'Трубачеевка')


@router.callback_query(F.data == "wild_dry")
async def andreev_dry(callback: types.CallbackQuery):
    await send_manufactor_dry(callback, 'Try Wild')
