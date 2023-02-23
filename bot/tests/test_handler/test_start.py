from unittest.mock import AsyncMock
import pytest

from bot import *


@pytest.mark.asyncio
async def test_start_handler():
    message = AsyncMock()
    await start_command(message)

    message.answer.assert_called_with(text='<em><b>Добро</b> пожаловать!</em>', parse_mode='HTML')
