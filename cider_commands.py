
from aiogram import F, types, Router

from england_direc.uk_cider import england_cider
from france_direc.french_cider import french_cider
from german_direc.german_cider import german_cider
from italy_direc.italy_cider import get_italy_cider
from russia_direc.rus_buttons import russia_cider
from spain_direc.spain_cider import spain_cider
from user_commands import cmd_cider

router = Router()


@router.message(F.text.lower() == 'франция')
async def france(message: types.Message):
    await french_cider(message)


@router.message(F.text.lower() == 'россия')
async def russia(message: types.Message):
    await russia_cider(message)


@router.message(F.text.lower() == 'испания')
async def spain(message: types.Message):
    await spain_cider(message)


@router.message(F.text.lower() == 'англия')
async def england(message: types.Message):
    await england_cider(message)


@router.message(F.text.lower() == 'италия')
async def italy(message: types.Message):
    await get_italy_cider(message)


@router.message(F.text.lower() == 'германия')
async def germany(message: types.Message):
    await german_cider(message)


# Возвращаемся к выбору стран
@router.callback_query(F.data == "back_to_country")
async def send_back_to_country(callback: types.CallbackQuery):
    await cmd_cider(callback.message)
