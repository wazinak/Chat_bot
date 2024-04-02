import cider_info_func
import config
import asyncio
import logging
from aiogram import Bot, Dispatcher
import cider_commands
from france_direc import french_cider, french_bretagne, french_normandy, french_savoi, french_champange, french_alzas, french_poire
from russia_direc import rus_buttons,dry_button, semidry_button, semisweet_button, sweet_button
from spain_direc import spain_cider, dulce, brut_spain, extra_dry
from england_direc import uk_cider, uk_dry, uk_semidry, uk_semisweet, uk_sweet
from Database.models import async_main
import user_commands

dp = Dispatcher()


async def main():
    await async_main()

    logging.basicConfig(level=logging.INFO)
    bot = Bot(token=config.BOT_TOKEN)
    dp.include_routers(cider_commands.router,
                       user_commands.router,
                       rus_buttons.router,
                       dry_button.router,
                       semidry_button.router,
                       semisweet_button.router,
                       sweet_button.router,
                       french_bretagne.router,
                       french_cider.router,
                       french_normandy.router,
                       french_champange.router,
                       french_alzas.router,
                       french_savoi.router,
                       french_poire.router,
                       spain_cider.router,
                       extra_dry.router,
                       dulce.router,
                       brut_spain.router,
                       uk_cider.router,
                       uk_dry.router,
                       uk_semidry.router,
                       uk_semisweet.router,
                       uk_sweet.router,
                       cider_info_func.router,

                       )
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
