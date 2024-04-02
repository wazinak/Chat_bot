from aiogram import F, types, Router

from Database.requests import get_ciders_fr_sv

router = Router()


@router.callback_query(F.data == "alzas")
async def alzas_cider_btn(callback: types.CallbackQuery, region='Эльзас'):
    ciders = await get_ciders_fr_sv(f"{region}")
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

        [types.InlineKeyboardButton(text="Назад", callback_data="back_to_extra_doux")],
    ]
    list_btn = types.InlineKeyboardMarkup(inline_keyboard=list_btn)
    return list_btn
