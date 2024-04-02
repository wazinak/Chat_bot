from aiogram import types, Router
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder
from buttons import get_cider_counrty_kb, info_btn, random_btn

router = Router()


@router.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(text=f"Привет, {message.from_user.full_name}!")


@router.message(Command("cider"))
async def cmd_cider(message: types.Message):
    await message.answer("Какую страну ты выберешь?",
                         reply_markup=get_cider_counrty_kb())


@router.message(Command("help"))
async def cmd_help(message: types.Message):
    await message.answer("Это информационный бот. Он должен помочь тебе просмотреть сидры и какие они бывают. "
                         "Бот должен вывести список команд, которыми можно воспользоваться. По любым вопросам можно "
                         "написать создателю @wazinak")


@router.message(Command("info"))
async def cmd_info(message: types.Message):
    await message.answer("Здесь должна быть краткая информация о сидрах",
                         reply_markup=info_btn())


@router.message(Command("random"))
async def cmd_random(message: types.Message):
    await message.answer(text="Нажмите на кнопку, чтобы бот отправил любой сидр", reply_markup=random_btn())



