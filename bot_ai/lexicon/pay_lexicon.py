from collections import namedtuple

Pay = namedtuple('Pay', 'title description payload')

Label = namedtuple('Label', 'label amount')

SuccessfulPayment = namedtuple('SuccessfulPayment', 'answer')

SUB_PAY = {
    'default_sub': {
        'title': 'Обычная подписка',
        'description': 'Обычная подписка включает в себя 1,500,000 токенов каждую неделю',
        'payload': 'default_sub',
    },
    'premium_sub': {
        'title': 'Премиум подписка',
        'description': 'Премиум подписка включает в себя 10,000,000 токенов каждую неделю',
        'payload': 'premium_sub',
    },
    'unlimited_sub': {
        'title': 'Безлимитная подписка',
        'description': 'Безлимитная подписка включает в себя бесконечное количество токенов',
        'payload': 'unlimited_sub',
    }
}

# sub_info
SUB_PAY_INFO = {
    'pay_default_sub': Pay(**SUB_PAY['default_sub']),
    'pay_premium_sub': Pay(**SUB_PAY['premium_sub']),
    'pay_unlimited_sub': Pay(**SUB_PAY['unlimited_sub'])

}
# sub_labels
SUB_PAY_LABELS = {
    'pay_default_sub': Label(
        label='Обычная подписка',
        amount=25_000
    ),
    'pay_premium_sub': Label(
        label='Премиум подписка',
        amount=112_500
    ),
    'pay_unlimited_sub': Label(
        label='Безлимитная подписка',
        amount=225_000
    )
}


payment = SuccessfulPayment(f'Спасибо за покупку! Ваш заказ отправлен на обработку. Пожалуйста, подождите немного.\n')

print(payment.answer)
