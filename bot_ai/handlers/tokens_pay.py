import logging

from aiogram import F, Router, Bot
from aiogram.enums import ContentType
from aiogram.types import CallbackQuery, LabeledPrice, PreCheckoutQuery, Message

from bot_ai import config
from bot_ai.lexicon.tokens_pay_lexicon import TokenPay, TOKEN_PAY_INFO, TokenLabel, TOKEN_PAY_LABELS, TOKENS
from bot_ai.utils.user_requsts import UserRequest

router: Router = Router()
logger: logging.Logger = logging.getLogger(__name__)


@router.callback_query(F.data.startswith('tokens'))
async def tokens_order(callback: CallbackQuery, bot: Bot) -> None:
    token_info: TokenPay = TOKEN_PAY_INFO.get(callback.data, False)
    token_label: TokenLabel = TOKEN_PAY_LABELS.get(callback.data, False)
    print(token_label)
    print(token_info)
    await bot.send_invoice(
        chat_id=callback.message.chat.id,
        title=token_info.title,
        description=token_info.description,
        payload=token_info.payload,
        provider_token=config.UKASSA_TOKEN,
        currency='rub',
        prices=[
            LabeledPrice(
                label=token_label.label,
                amount=token_label.amount
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
async def tokens_checkout_query(pre_checkout_query: PreCheckoutQuery, bot: Bot) -> None:
    # if request.check_user_status == 'unlimited_sub':
    #     await bot.answer_pre_checkout_query(
    #         pre_checkout_query.id,
    #         ok=False,
    #         error_message='У вас безлимитная подписка, вам не нужно покупать токены'
    #     )
    #     return
    # else:
    await bot.answer_pre_checkout_query(
        pre_checkout_query_id=pre_checkout_query.id,
        ok=True,
        error_message=None
    )


@router.message(F.content_type == ContentType.SUCCESSFUL_PAYMENT)
async def successful_payment(message: Message, request: UserRequest) -> None:
    logger.info(f'Successful payment from {message.chat.id}')
    print('invoice', message.successful_payment.invoice_payload)

    purchased_tokens: int = TOKENS.get(message.successful_payment.invoice_payload, False)
    try:
        await request.set_tokens(
            user_id=message.from_user.id,
            purchased_tokens=purchased_tokens
        )
        msg = f'Вы оплатили {message.successful_payment.total_amount // 100} {message.successful_payment.currency}'
        await message.answer(msg)
    except Exception as exc:
        logger.error(exc)
        await message.answer(
            'Что-то пошло не так. Сообщите, пожалуйста, об ошибке администратору.'
            'Контакты можно найти, вызвав команду /help'
        )