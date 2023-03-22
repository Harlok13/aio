import logging

from aiogram import Bot, Router, F
from aiogram.enums import ContentType
from aiogram.filters import Text, Command
from aiogram.types import Message, LabeledPrice, PreCheckoutQuery, CallbackQuery

from bot_ai import config
from bot_ai.lexicon.pay_lexicon import (
    payment, SUB_PAY_INFO, Pay, SUB_PAY_LABELS, Label
)
from bot_ai.utils.user_requsts import UserRequest

router = Router()
logger = logging.getLogger(__name__)


# @router.message(Command(commands='pay'))
@router.callback_query(F.data.endswith('sub'))
async def order(callback: CallbackQuery, bot: Bot) -> None:
    pay_info: Pay = SUB_PAY_INFO.get(callback.data, False)
    print(callback.data)
    print(pay_info)
    pay_label: Label = SUB_PAY_LABELS.get(callback.data, False)
    await bot.send_invoice(
        chat_id=callback.message.chat.id,
        title=pay_info.title,
        description=pay_info.description,
        payload=pay_info.payload,
        provider_token=config.UKASSA_TOKEN,
        currency='rub',
        prices=[
            LabeledPrice(
                label=pay_label.label,
                amount=pay_label.amount
            )
        ],
        max_tip_amount=1000,
        suggested_tip_amounts=[100, 200, 300, 500],
        start_parameter=None,
        provider_data=None,
        # photo_url='',
        # photo_size=0,
        # photo_width=0,
        # photo_height=0,
        need_name=True,
        need_phone_number=True,
        need_email=True,
        need_shipping_address=False,
        send_phone_number_to_provider=False,
        send_email_to_provider=False,
        is_flexible=False,
        disable_notification=False,
        protect_content=False,
        reply_to_message_id=None,
        allow_sending_without_reply=True,
        reply_markup=None,
        request_timeout=15
    )


@router.pre_checkout_query()
async def pre_checkout_query(pre_checkout_query: PreCheckoutQuery, bot: Bot) -> None:
    await bot.answer_pre_checkout_query(
        pre_checkout_query_id=pre_checkout_query.id,
        ok=True,
    )


@router.message(F.content_type == ContentType.SUCCESSFUL_PAYMENT)
async def successful_payment(message: Message, request: UserRequest) -> None:
    logger.info(message.successful_payment)
    print('invoice', message.successful_payment.invoice_payload)
    await request.set_default_sub(user_id=message.from_user.id, status=message.successful_payment.invoice_payload)
    msg = payment.answer + \
          f'Вы оплатили {message.successful_payment.total_amount // 100} {message.successful_payment.currency}'
    await message.answer(msg)
