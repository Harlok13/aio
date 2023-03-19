import asyncio
import logging
import openai

from aiogram import Bot, Dispatcher, F
from aiogram.enums import ContentType
from aiogram.filters import Command

from bot_ai import config
from bot_ai.handlers import msg_handler, pay


logger = logging.getLogger(__name__)


async def main() -> None:
    logging.basicConfig(
        level="INFO",
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )

    bot: Bot = Bot(token=config.BOT_TOKEN)
    openai.api_key = config.AI_TOKEN

    dp: Dispatcher = Dispatcher()

    # register handlers
    dp.include_router(msg_handler.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit) as exc:
        logger.error(exc)
    finally:
        logger.info("Bye!")
