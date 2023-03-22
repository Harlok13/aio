import asyncio
import logging

import openai

from aiogram import Bot, Dispatcher, F
from sqlalchemy import URL
from sqlalchemy.ext.asyncio import AsyncEngine
from sqlalchemy.orm import sessionmaker

from bot_ai import config
from bot_ai.data.engine import get_async_engine, get_session_maker
from bot_ai.handlers import pay
from bot_ai.handlers.cb_handler import register_cb_handlers
from bot_ai.handlers.cmd_handler import register_cmd_handlers
from bot_ai.handlers.pay import order, pre_checkout_query, successful_payment

logger = logging.getLogger(__name__)


async def main() -> None:
    logging.basicConfig(
        level="INFO",
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )

    bot: Bot = Bot(token=config.BOT_TOKEN, parse_mode='HTML')
    openai.api_key = config.AI_TOKEN

    dp: Dispatcher = Dispatcher()

    # register handlers
    # dp.include_router(msg_handler.router)
    register_cmd_handlers(dp)
    register_cb_handlers(dp)

    # register payment
    dp.include_router(pay.router)
    # dp.message.register(successful_payment, ContentTypesFilter(content_types=[ContentType.SUCCESSFUL_PAYMENT]))

    # include postgresql
    postgresql_url: URL = URL.create(
        'postgresql+asyncpg',
        username=config.PG_USER,
        host=config.IP,
        password=config.PG_PASSWORD,
        database=config.DATABASE,
        port=int(config.PG_PORT or 0)
    )
    async_engine: AsyncEngine = get_async_engine(postgresql_url)
    async_session_maker: sessionmaker = get_session_maker(async_engine)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit) as exc:
        logger.error(exc)
    finally:
        logger.info("Bye!")
