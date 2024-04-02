from aiogram import types, Router, F

router = Router()


async def spain_cider(message: types.Message):
    await message.answer(
        text="Какую сухость/сладость ты выберешь?",
        reply_markup=extra_dulce()
    )


def extra_dulce():
    buttons = [
        [types.InlineKeyboardButton(text='Extra Dry', callback_data="extra-dry")],
        [
            types.InlineKeyboardButton(text='Brut', callback_data="brut_spain"),
            types.InlineKeyboardButton(text='Dulce', callback_data="dulce"),
        ],
        [types.InlineKeyboardButton(text="Вернуться к странам", callback_data="back_to_country")],

    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


# кнопка возврата инлайн кнопки на страницу от сухого к сладкому
@router.callback_query(F.data == "back_to_extra_dulce")
async def back_to_extra_doux_btn(callback: types.CallbackQuery):
    await callback.message.edit_text(text='Начнем сначала: ', reply_markup=extra_dulce())
