from aiogram import types, F, Router

from Database.requests import get_ciders_rus

router = Router()


@router.callback_query(F.data == "sweet")
async def send_sweet(callback: types.CallbackQuery):
    await callback.message.edit_text(text='От какого производителя интересен сидр?', reply_markup=sweet_cider_btn())


def sweet_cider_btn():
    buttons = [
        [types.InlineKeyboardButton(text='Bullevie', callback_data="bullevie_sweet")],
        [types.InlineKeyboardButton(text='Gravity Project', callback_data="gravity_sweet")],
        [types.InlineKeyboardButton(text="Назад", callback_data="back_to_sour_sweet")],
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


async def send_manufactor_semisweet(callback: types.CallbackQuery, manufacture: str, sour="Сладкий"):
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

        [types.InlineKeyboardButton(text="Назад к Сидроделу", callback_data="sweet")],
    ]
    list_btn = types.InlineKeyboardMarkup(inline_keyboard=list_btn)
    return list_btn

@router.callback_query(F.data == "gravity_sweet")
async def gravity_semisweet(callback: types.CallbackQuery):
    await send_manufactor_semisweet(callback, "Gravity Project")


@router.callback_query(F.data == "bullevie_sweet")
async def bullevie_semisweet(callback: types.CallbackQuery):
    await send_manufactor_semisweet(callback, "Bullevie")
