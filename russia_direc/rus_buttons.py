from aiogram import types, Router, F

router = Router()


async def russia_cider(message: types.Message):
    await message.answer(
        text="Какую сухость/сладость ты выберешь?",
        reply_markup=sour_sweet()
    )


def sour_sweet():
    buttons = [
        [types.InlineKeyboardButton(text='Сухой', callback_data="dry"),
         types.InlineKeyboardButton(text='Полусухой', callback_data="semidry")],
        [types.InlineKeyboardButton(text='Полусладкий', callback_data="semisweet"),
         types.InlineKeyboardButton(text='Сладкий', callback_data="sweet")],
        [types.InlineKeyboardButton(text="Вернуться к странам", callback_data="back_to_country")],

    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


# кнопка возврата инлайн кнопки на страницу от сухого к сладкому
@router.callback_query(F.data == "back_to_sour_sweet")
async def back_to_sour_sweet_btn(callback: types.CallbackQuery):
    await callback.message.edit_text(text='Начнем сначала: ', reply_markup=sour_sweet())
