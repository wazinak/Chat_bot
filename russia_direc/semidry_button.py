from aiogram import F, types, Router
from Database.requests import get_ciders_rus

router = Router()


def manufacture_btn_semidry():
    manufacture_btn = [
        [types.InlineKeyboardButton(text='Andreev Ciderworks', callback_data="andreev_semidry"),
         types.InlineKeyboardButton(text="Gravity Project", callback_data="gravity_semidry")],
        [types.InlineKeyboardButton(text='Brodilka', callback_data="brodilka_semidry"),
         types.InlineKeyboardButton(text="Bullevie", callback_data="bullevie_semidry"),
         types.InlineKeyboardButton(text="Лось и Кедр", callback_data="lik_semidry")],
        [types.InlineKeyboardButton(text="Rebel Apple", callback_data="rebel_semidry"),
         types.InlineKeyboardButton(text="Абрау Дюрсо", callback_data="abra_semidry")],
        [types.InlineKeyboardButton(text="Русская Нормандия", callback_data="r_normand_semidry"),
         types.InlineKeyboardButton(text="Заповедник", callback_data="zapad_semidry")],
        [types.InlineKeyboardButton(text="Октябрь", callback_data="october_semidry"),
         types.InlineKeyboardButton(text="Птицы", callback_data="bird_semidry")],
        [types.InlineKeyboardButton(text="Токсовская Сидрерия", callback_data="toksovo_semidry"),
         types.InlineKeyboardButton(text="La maiзon verte", callback_data="verte_semidry")],

        [types.InlineKeyboardButton(text="Назад", callback_data="back_to_sour_sweet")],
    ]
    manufacture_keyboard = types.InlineKeyboardMarkup(inline_keyboard=manufacture_btn)
    return manufacture_keyboard


@router.callback_query(F.data == "semidry")
async def send_manufactor(callback: types.CallbackQuery):
    await callback.message.edit_text(text='От какого производителя интересен сидр? ',
                                     reply_markup=manufacture_btn_semidry())


async def send_manufactor_semidry(callback: types.CallbackQuery, manufacture: str, sour="Полусухой"):
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

        [types.InlineKeyboardButton(text="Назад к Сидроделу", callback_data="semidry")],
    ]
    list_btn = types.InlineKeyboardMarkup(inline_keyboard=list_btn)
    return list_btn


@router.callback_query(F.data == "andreev_semidry")
async def andreev_semidry(callback: types.CallbackQuery):
    await send_manufactor_semidry(callback, 'Andreev Ciderworks')


@router.callback_query(F.data == "gravity_semidry")
async def gravity_semidry(callback: types.CallbackQuery):
    await send_manufactor_semidry(callback, 'Gravity Project')


@router.callback_query(F.data == "brodilka_semidry")
async def brodilka_semidry(callback: types.CallbackQuery):
    await send_manufactor_semidry(callback, 'Brodilka')


@router.callback_query(F.data == "bullevie_semidry")
async def bullevie_semidry(callback: types.CallbackQuery):
    await send_manufactor_semidry(callback, 'Bullevie')


@router.callback_query(F.data == "lik_semidry")
async def lik_semidry(callback: types.CallbackQuery):
    await send_manufactor_semidry(callback, 'Лось и Кедр')


@router.callback_query(F.data == "rebel_semidry")
async def rebel_semidry(callback: types.CallbackQuery):
    await send_manufactor_semidry(callback, 'Rebel Apple')


@router.callback_query(F.data == "abra_semidry")
async def abra_dry(callback: types.CallbackQuery):
    await send_manufactor_semidry(callback, 'Абрау Дюрсо')


@router.callback_query(F.data == "r_normand_semidry")
async def r_normand_semidry(callback: types.CallbackQuery):
    await send_manufactor_semidry(callback, 'Русская Нормандия')


@router.callback_query(F.data == "zapad_semidry")
async def zapad_semidry(callback: types.CallbackQuery):
    await send_manufactor_semidry(callback, 'Заповедник')


@router.callback_query(F.data == "october_semidry")
async def october_semidry(callback: types.CallbackQuery):
    await send_manufactor_semidry(callback, 'Октябрь')


@router.callback_query(F.data == "bird_semidry")
async def bird_semidry(callback: types.CallbackQuery):
    await send_manufactor_semidry(callback, 'Птицы')


@router.callback_query(F.data == "toksovo_semidry")
async def toksovo_semidry(callback: types.CallbackQuery):
    await send_manufactor_semidry(callback, 'Токсовская Сидрерия')


@router.callback_query(F.data == "verte_semidry")
async def toksovo_semidry(callback: types.CallbackQuery):
    await send_manufactor_semidry(callback, 'La maiзon verte')
