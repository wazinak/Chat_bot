from aiogram import F, types, Router

from Database.requests import get_ciders_uk

router = Router()


@router.callback_query(F.data == "sweet_uk")
async def send_uk_dry(callback: types.CallbackQuery):
    await callback.message.edit_text(text='От какого производителя интересен сидр?', reply_markup=uk_sweet_cider_btn())


def uk_sweet_cider_btn():
    buttons = [
        [types.InlineKeyboardButton(text="Henney's", callback_data="henney_sweet")],
        [types.InlineKeyboardButton(text="Назад", callback_data="back_to_dry_sugar")],
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


async def send_manufactor_semisweet(callback: types.CallbackQuery, manufacture: str, sour="Сладкий"):
    ciders = await get_ciders_uk(f"{manufacture}", f"{sour}")
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

        [types.InlineKeyboardButton(text="Назад к Сидроделу", callback_data="sweet_uk")],
    ]
    list_btn = types.InlineKeyboardMarkup(inline_keyboard=list_btn)
    return list_btn


@router.callback_query(F.data == "henney_sweet")
async def andreev_semidry(callback: types.CallbackQuery):
    await send_manufactor_semisweet(callback, "Henney's")
