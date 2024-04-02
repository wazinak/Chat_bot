from aiogram import types, Router, F

router = Router()


async def french_cider(message: types.Message):
    await message.answer(
        text="Что ты выберешь?",
        reply_markup=extra_doux()
    )


def extra_doux():
    buttons = [
        [types.InlineKeyboardButton(text='Бретань', callback_data="bretagne"),
         types.InlineKeyboardButton(text='Нормандия', callback_data="normandy")],
        [types.InlineKeyboardButton(text='Савойя', callback_data="savoi"),
         types.InlineKeyboardButton(text='Эльзас', callback_data="alzas")],
        [types.InlineKeyboardButton(text='Шампань-Арденны', callback_data="champange"),
         types.InlineKeyboardButton(text='Poire', callback_data="poire"),
         ],
        [types.InlineKeyboardButton(text="Вернуться к странам", callback_data="back_to_country")],

    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


# кнопка возврата инлайн кнопки на страницу от сухого к сладкому
@router.callback_query(F.data == "back_to_extra_doux")
async def back_to_extra_doux_btn(callback: types.CallbackQuery):
    await callback.message.edit_text(text='Начнем сначала: ', reply_markup=extra_doux())
