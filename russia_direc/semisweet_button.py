from aiogram import types, F, Router
from Database.requests import get_ciders_rus

router = Router()


@router.callback_query(F.data == "semisweet")
async def send_manufactor(callback: types.CallbackQuery):
    await callback.message.edit_text(text='От какого производителя интересен сидр? ',
                                     reply_markup=manufacture_semisweet())


def manufacture_semisweet():
    manufacture_btn = [
        [types.InlineKeyboardButton(text='Andreev Ciderworks', callback_data="andreev_semisweet"),
         types.InlineKeyboardButton(text="Gravity Project", callback_data="gravity_semisweet")],
        [types.InlineKeyboardButton(text='Brodilka', callback_data="brodilka_semisweet"),
         types.InlineKeyboardButton(text="Bullevie", callback_data="bullevie_semisweet"),
         types.InlineKeyboardButton(text="Лось и Кедр", callback_data="lik_semisweet")],
        [types.InlineKeyboardButton(text="Rebel Apple", callback_data="rebel_semisweet"),
         types.InlineKeyboardButton(text="Птицы", callback_data="bird_semisweet")],
        [types.InlineKeyboardButton(text="Абрау Дюрсо", callback_data="abra_semisweet"),
         types.InlineKeyboardButton(text="Русская Нормандия", callback_data="r_normand_semisweet")],
        [types.InlineKeyboardButton(text="Токсовская Сидрерия", callback_data="toksovo_semisweet"),
        types.InlineKeyboardButton(text="La maiзon verte", callback_data="verte_semisweet")],

        [types.InlineKeyboardButton(text="Назад", callback_data="back_to_sour_sweet")],
    ]
    manufacture_keyboard = types.InlineKeyboardMarkup(inline_keyboard=manufacture_btn)
    return manufacture_keyboard


async def send_manufactor_semisweet(callback: types.CallbackQuery, manufacture: str, sour="Полусладкий"):
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

        [types.InlineKeyboardButton(text="Назад к Сидроделу", callback_data="semisweet")],
    ]
    list_btn = types.InlineKeyboardMarkup(inline_keyboard=list_btn)
    return list_btn


@router.callback_query(F.data == "andreev_semisweet")
async def andreev_semisweet(callback: types.CallbackQuery):
    await send_manufactor_semisweet(callback, "Andreev Ciderworks")


@router.callback_query(F.data == "gravity_semisweet")
async def gravity_semisweet(callback: types.CallbackQuery):
    await send_manufactor_semisweet(callback, "Gravity Project")


@router.callback_query(F.data == "brodilka_semisweet")
async def brodilka_semisweet(callback: types.CallbackQuery):
    await send_manufactor_semisweet(callback, "Brodilka")


@router.callback_query(F.data == "bullevie_semisweet")
async def bullevie_semisweet(callback: types.CallbackQuery):
    await send_manufactor_semisweet(callback, "Bullevie")


@router.callback_query(F.data == "lik_semisweet")
async def lik_semisweet(callback: types.CallbackQuery):
    await send_manufactor_semisweet(callback, "Лось и Кедр")


@router.callback_query(F.data == "rebel_semisweet")
async def rebel_semisweet(callback: types.CallbackQuery):
    await send_manufactor_semisweet(callback, "Rebel Apple")


@router.callback_query(F.data == "bird_semisweet")
async def bird_semisweet(callback: types.CallbackQuery):
    await send_manufactor_semisweet(callback, "Птицы")


@router.callback_query(F.data == "abra_semisweet")
async def abra_semisweet(callback: types.CallbackQuery):
    await send_manufactor_semisweet(callback, "Абрау Дюрсо")


@router.callback_query(F.data == "r_normand_semisweet")
async def r_normand_semisweet(callback: types.CallbackQuery):
    await send_manufactor_semisweet(callback, "Русская Нормандия")


@router.callback_query(F.data == "toksovo_semisweet")
async def toksovo_semisweet(callback: types.CallbackQuery):
    await send_manufactor_semisweet(callback, "Токсовская Сидрерия")


@router.callback_query(F.data == "verte_semisweet")
async def toksovo_semidry(callback: types.CallbackQuery):
    await send_manufactor_semisweet(callback, 'La maiзon verte')
