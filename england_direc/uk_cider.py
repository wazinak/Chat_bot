from aiogram import types, Router, F

router = Router()


async def england_cider(message: types.Message):
    await message.answer(
        text="Какую сухость/сладость ты выберешь?",
        reply_markup=dry_sugar()
    )


def dry_sugar():
    buttons = [
        [types.InlineKeyboardButton(text='Сухой', callback_data="dry_uk"),
         types.InlineKeyboardButton(text='Полусухой', callback_data="semidry_uk")],
        [types.InlineKeyboardButton(text='Полусладкий', callback_data="semisweet_uk"),
         types.InlineKeyboardButton(text='Сладкий', callback_data="sweet_uk")],
        [types.InlineKeyboardButton(text="Вернуться к странам", callback_data="back_to_country")],

    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


# кнопка возврата инлайн кнопки на страницу от сухого к сладкому
@router.callback_query(F.data == "back_to_dry_sugar")
async def back_to_dry_sugar_btn(callback: types.CallbackQuery):
    await callback.message.edit_text(text='Начнем сначала: ', reply_markup=dry_sugar())