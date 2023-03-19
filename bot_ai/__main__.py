import asyncio
import logging
import openai

from aiogram import Bot, Dispatcher, F
from aiogram.enums import ContentType
from aiogram.filters import Command

from bot_ai import config
from bot_ai.handlers import msg_handler, pay
from bot_ai.handlers.pay import order, pre_checkout_query
from bot_ai.handlers.pay import successful_payment

logger = logging.getLogger(__name__)

try:
    async def main() -> None:
        logging.basicConfig(
            level="INFO",
            format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )

        bot: Bot = Bot(token=config.BOT_TOKEN)
        openai.api_key = config.AI_TOKEN

        dp: Dispatcher = Dispatcher()

        # register handlers
        dp.message.register(order, Command(commands='pay'))
        dp.pre_checkout_query(pre_checkout_query, F.content_type(ContentType.SUCCESSFUL_PAYMENT))
        # dp.include_router(pay.router)
        dp.message.register(successful_payment)
        dp.include_router(msg_handler.router)

        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot)
except Exception as e:
    logger.error(e)
    raise e

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit) as exc:
        logger.error(exc)
    finally:
        logger.info("Bye!")
