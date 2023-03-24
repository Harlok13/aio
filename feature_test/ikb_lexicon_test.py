from typing import Union, Dict, List, Tuple


MAIN_MENU: Dict[str, List[Union[Tuple[str, str], Tuple[int]]]] = {
    'cat_menu': [
        ('ПРОФИЛЬ', 'cat_profile'),
        ('УЛУЧШЕНИЯ', 'cat_upgrades'),
        ('МОДЕЛИ БОТА', 'cat_models'),
        ('ПОМОЩЬ', 'cat_help'),
        ('НАСТРОЙКИ', 'cat_settings'),
        ('ЗАКРЫТЬ МЕНЮ', 'cat_exit'),
        (2, 1, 2, 1)
    ],
    'cat_profile': [
        ('РЕФЕРАЛЬНАЯ СИСТЕМА', 'cat_referral'),
        ('🔙 НАЗАД', 'cat_menu'),
        (1,)
    ],
    'cat_referral': [
        ('ПРИГЛАСИТЬ', '?'),
        ('🔙 НАЗАД', 'cat_profile'),
        (1,)
    ],
    'cat_models': [
        ('СТАНДАРТНАЯ МОДЕЛЬ', 'set_standard'),
        # ('ХУДОЖНИК', 'set_picture'),
        # ('КОДЕР', 'set_coder'),
        # ('СОБЕСЕДНИК', 'set_coder'),
        # ('ПЕРЕВОДЧИК', 'set_coder'),
        ('🔙 НАЗАД', 'cat_menu'),
        (1,)
    ],
    'cat_help': [
        ('🔙 НАЗАД', 'cat_menu'),
        (1,)
    ],
    'cat_upgrades': [
        ('ПОДПИСКА', 'cat_subscription'),
        # ('СНИЖЕНИЕ ЗАДЕРЖКИ', 'cat_reduction'),
        ('ВОССТАНОВЛЕНИЕ ТОКЕНОВ', 'cat_tokens'),
        ('🔙 НАЗАД', 'cat_menu'),
        (1,)
    ],
    'cat_subscription': [
        ('ОБЫЧНАЯ', 'cat_default_sub'),
        ('ПРЕМИУМ', 'cat_premium_sub'),
        ('БЕЗЛИМИТНАЯ', 'cat_unlimited_sub'),
        ('🔙 НАЗАД', 'cat_upgrades'),
        (1,)
    ],
    'cat_default_sub': [
        ('1 МЕСЯЦ', 'pay_default_sub_1'),
        ('3 МЕСЯЦА', 'pay_default_sub_3'),
        ('6 МЕСЯЦОВ', 'pay_default_sub_6'),
        ('🔙 НАЗАД', 'cat_subscription'),
        (1, 1)
    ],
    'cat_premium_sub': [
        ('1 МЕСЯЦ', 'pay_premium_sub_1'),
        ('3 МЕСЯЦА', 'pay_premium_sub_3'),
        ('6 МЕСЯЦОВ', 'pay_premium_sub_6'),
        ('🔙 НАЗАД', 'cat_subscription'),
        (1, 1)
    ],
    'cat_unlimited_sub': [
        ('1 МЕСЯЦ', 'pay_unlimited_sub_1'),
        ('3 МЕСЯЦА', 'pay_unlimited_sub_3'),
        ('6 МЕСЯЦОВ', 'pay_unlimited_sub_6'),
        ('🔙 НАЗАД', 'cat_subscription'),
        (1, 1)
    ],
    # 'cat_default': [
    #     ('КУПИТЬ', 'pay_default_sub_1'),
    #     ('🔙 НАЗАД', 'cat_default_sub'),
    #     (1,)
    # ],
    # 'cat_premium': [
    #     ('КУПИТЬ', 'pay_premium_sub'),
    #     ('🔙 НАЗАД', 'cat_premium_sub'),
    #     (1,)
    # ],
    # 'cat_unlimited': [
    #     ('КУПИТЬ', 'pay_unlimited_sub'),
    #     ('🔙 НАЗАД', 'cat_unlimited_sub'),
    #     (1,)
    # ],
    'cat_tokens': [
        ('ОПЛАТА КАРТОЙ', 'cat_cardpay'),
        ('ОПЛАТА КРИПТОВАЛЮТОЙ', 'cat_criptopay'),
        ('🔙 НАЗАД', 'cat_menu'),
        (1,)
    ],
    'cat_cardpay': [
        ('100,000 токенов', 'tokens_100k'),
        ('200,000 токенов', 'tokens_200k'),
        ('500,000 токенов', 'tokens_500k'),
        ('1,000,000 токенов', 'tokens_1000k'),
        ('🔙 НАЗАД', 'cat_tokens'),
        (1, 1)
    ],
    'cat_criptopay': [
        # ('Tether', '?'),
        # ('Toncoin', '?'),
        # ('Bitcoin', '?'),
        # ('Etherium', '?'),
        # ('Binance Coin', '?'),
        # ('Binance USD', '?'),
        # ('USD Coin', '?'),
        ('🔙 НАЗАД', 'cat_upgrades'),
        (1,)
    ],
    'cat_settings': [
        ('СТАНДАРТНАЯ МОДЕЛЬ', 'change_standard'),
        # ('ХУДОЖНИК', 'change_artist'),
        # ('КОДЕР', 'change_coder'),
        # ('СОБЕСЕДНИК', 'change_companion'),
        # ('ПЕРЕВОДЧИК', 'change_translator'),
        ('🔙 НАЗАД', 'cat_menu'),
        (1,)
    ]
}
