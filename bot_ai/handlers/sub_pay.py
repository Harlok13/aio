import logging

from aiogram import Bot, Router, F
from aiogram.enums import ContentType
from aiogram.filters import Text, Command
from aiogram.types import Message, LabeledPrice, PreCheckoutQuery, CallbackQuery

from bot_ai import config
from bot_ai.keyboards.inline_keyboard import main_menu
from bot_ai.lexicon.sub_pay_lexicon import (
    SubPay, SubLabel, SubPayInfo
)
from bot_ai.utils.user_requsts import UserRequest

router: Router = Router()
logger: logging.Logger = logging.getLogger(__name__)

subscription: SubPayInfo = SubPayInfo()


@router.callback_query(F.data.startswith('pay'))
async def subscription_order(callback: CallbackQuery, bot: Bot) -> None:
    data_sub, months = callback.data[:-2], callback.data[-1]
    subscription_info: SubPay = subscription.get_info(data_sub)
    print(callback.data)
    print(subscription_info)
    subscription_label: SubLabel = subscription.get_labels(data_sub, months)
    await bot.send_invoice(
        chat_id=callback.message.chat.id,
        title=subscription_info.title,
        description=subscription_info.description,
        payload=subscription_info.payload,
        provider_token=config.UKASSA_TOKEN,
        currency='rub',
        prices=[
            LabeledPrice(
                label=subscription_label.label,
                amount=subscription_label.amount
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


# ref
@router.pre_checkout_query(F.invoice_payload.startswith('pay'))  # add filter
async def sub_checkout_query(pre_checkout_query: PreCheckoutQuery, bot: Bot, request: UserRequest) -> None:
    user_status: str = await request.get_user_status(pre_checkout_query.from_user.id)
    print('status', user_status)
    if user_status == 'premium_sub' and pre_checkout_query.invoice_payload == 'default_sub' \
            or user_status == 'unlimited_sub' and (pre_checkout_query.invoice_payload == 'premium_sub'
                                                   or pre_checkout_query.invoice_payload == 'default_sub'):
        await bot.answer_pre_checkout_query(
            pre_checkout_query_id=pre_checkout_query.id,
            ok=False,
            error_message=subscription.error_message
        )
        return
    else:
        await bot.answer_pre_checkout_query(
            pre_checkout_query_id=pre_checkout_query.id,
            ok=True,
        )


@router.message(
    F.content_type == ContentType.SUCCESSFUL_PAYMENT,
    F.invoice_payload.endswith('sub')
)
async def successful_payment(message: Message, request: UserRequest) -> None:
    logger.info(message.successful_payment)
    print('payment', message.successful_payment)
    print('invoice', message.successful_payment.invoice_payload)
    data_sub: str = message.successful_payment.invoice_payload
    sub_amount: int = message.successful_payment.total_amount

    days_sub: int = subscription.get_days(data_sub, sub_amount)
    purchased_tokens: int = subscription.get_tokens(data_sub)
    try:
        await request.set_subscription(
            user_id=message.from_user.id,
            purchased_status=message.successful_payment.invoice_payload,
            purchased_tokens=purchased_tokens,
            days_sub=days_sub
        )
        success_msg: str = subscription.get_successful_payment_msg(message)
        await message.answer(success_msg)

    except Exception as exc:
        logger.error(exc)
        await message.answer(
            subscription.something_wrong_message
        )
