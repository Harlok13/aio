import os
import pathlib
import logging
import asyncio

from aiogram import Bot, Dispatcher


async def start_bot(logger: logging.Logger = None) -> None:
    logging.basicConfig(level='DEBUG', filename='mylog13.log')

    bot = Bot(token=os.getenv('TOKEN_API'))
    dp = Dispatcher(bot)

    await dp.start_polling(bot)


def setup_env() -> None:
    """Настройка переменных окружения."""
    from dotenv import load_dotenv
    path = pathlib.Path(__file__).parent.parent
    dotenv_path = path.joinpath('.env')
    if dotenv_path.exists():
        load_dotenv(dotenv_path)


def main():
    logger = logging.getLogger(__name__)
    try:
        setup_env()
        asyncio.run(start_bot())
        logger.info('start')
    except (KeyboardInterrupt, SystemExit):
        logger.info('stop')


if __name__ == '__main__':
    main()
