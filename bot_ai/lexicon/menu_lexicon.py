from typing import Dict, Callable, Any, Union

from bot_ai.lexicon.commands_lexicon import COMMANDS
from bot_ai.utils.correct_profile_info import get_current_tokens_info, get_counter_days_info
from bot_ai.utils.user_requsts import ProfileInfo


def get_main_menu(*args) -> str:
    main_menu_msg: str = f'<b>📂 Меню 📂</b>\n\n' \
                         f'<b>Быстрое использование всех команд бота</b>'
    return main_menu_msg


def get_profile(profile: ProfileInfo) -> str:
    max_tokens: Dict[str, str] = {
        'standard': '50,000',
        'default_sub': '1,500,000',
        'premium_sub': '10,000,000',
        'unlimited_sub': 'unlimited',
    }

    profile_msg: str = f'<b>📊 Ваш профиль:</b>\n\n' \
                       f'<b>👤 Имя:</b> {profile.nickname}\n' \
                       f'<b>👁‍🗨 Задано вопросов:</b> {profile.question_count}\n' \
                       f'<b>🎟 Токенов осталось:</b> {get_current_tokens_info(profile)}' \
                       f'/{max_tokens.get(profile.status)}\n' \
                       f'<b>🕑 {get_counter_days_info(profile)}</b> {profile.days_left} дней\n\n' \
                       f'<b>🗝 Статус:</b> {profile.status.split("_")[0]}\n\n' \
                       f'<em>❓Подробнее про токены! - /help</em>'
    return profile_msg


def get_referral(referral_count=None, *args) -> str:
    referral_msg: str = f'<b>📊Реферальная система:</b>\n\n' \
                        f'<b>👥Рефералов:</b> {referral_count}\n\n' \
                        f'<em>🔥За каждого приведенного пользователя вы получите 50₽</em>\n\n' \
                        f'<em>⚡Чтобы пригласить пользователя: нажмите кнопку <b>"ПРИГЛАСИТЬ"</b></em>'
    return referral_msg


def get_models_info(current_model: str) -> str:
    models_info: Dict[str, str] = {
        'set_standard': 'Cтандартная модель',
        'set_artist': 'Художник',
        'set_coder': 'Кодер',
        'set_companion': 'Собеседник',
        'set_translator': 'Переводчик',
    }
    print('get_models_info!', current_model)
    models_msg: str = f'<b>⚙️ВЫБОР МОДЕЛИ⚙️</b>\n\n' \
                      f'<b>Доступные:</b>\n' \
                      f'<em>Cтандартная модель</em>\n\n' \
                      f'<b>Будут доступны в скором времени:</b>\n' \
                      f'<em>Художник</em>\n' \
                      f'<em>Кодер</em>\n' \
                      f'<em>Собеседник</em>\n' \
                      f'<em>Переводчик</em>\n\n' \
                      f'<b>Подробнее о моделях можно узнать, вызвав команду /help</b>\n\n' \
                      f'<b>🌐Текущая модель:</b>\n' \
                      f'<em>{models_info.get(current_model, "Модель еще не установлена")}</em>\n\n'
    return models_msg


def get_help(*args) -> Dict[str, str]:
    help_msg: Dict[str, str] = {
        '1': f'<b>🔹 Что такое токен?</b>\n\n'
             f'<em>Токены нужны, чтобы задавать вопросы боту или создавать изображения</em>'
             f'<b>🔹 Как они тратятся?</b>\n\n'
             f'— 1 токен ≈ 1 символ (Включая ответ) — 1000 токенов = 1 изображение\n\n'
             f'<b>🔹 Что делать если кончились токены?</b>\n\n'
             f'<em>— Раз в неделю происходит восстановление токенов, узнать когда оно произойдет '
             f'можно в профиле (/profile)</em>\n\n'
             f'<em>— Можно восстановить токены с помощью услуги в магазине (/buy)</em>\n\n'
             f'По работе бота писать: @',
        '2': f'<b>🔹 Основные команды</b>\n\n'
             f'<em>/set - позволяет вызвать меню с выбором модели. </em>\n\n'
             f'<em>/ask - сообщить о проблеме. Чтобы сообщить о проблеме,'
             f'нужно нужно начать сообщение с команды /ask, а после нее'
             f'писать сообщение о проблеме. </em>\n\n'
             f'<em>/feedback - оставить отзыв для разработчика. Начав'
             f'сообщение с этой команды, вы можете оставить свое сообщение'
             f'разработчику со своим пожеланием или новой идеей. Так же '
             f'можно использовать сокращенную форму этой команды - /f</em>\n\n',
             # f'<em>/set - позволяет вызвать меню с выбором модели. </em>\n\n'
        '3': f'Настройки модели'
             f'В этом меню вы можете сделать тонкую настройку модели конкретно под свою задачу. '
             f'Есть несколько параметров, которые доступны для изменения. Так же в будущем будут '
             f'добавлены новые. Следите за обновлениями.\n'
             f'Из доступных параметров можно выделить следующие:\n'
             f'Temperature - с помощью него вы может отрегулировать ответы бота. Например, '
             f'если вам нужно придумать названия для своей фирмы или просто подобрать '
             f'кличку для животного, то можете использовать Temperature со значением 1.0,'
             f'это позволит боту генерировать каждый раз разные сообщения. Если выставить'
             f'Temperature в 0, то ответы станут более однообразными, но к тому же точными.'
             f'Это может быть полезно, если вам нужна более точная информация.\n'
             f'Tokens - позволяет контролировать размер сообщения. Это полезно, если вам '
             f'нужно ограничить расход токенов, либо наоборот ни в чем себе не отказывать '
             f'и дать боту возможность генерировать очень длинные сообщения.\n'
             f'В качестве примера длинных сообщений может быть просьба написать резюме,'
             f'сказку, статью или даже код. Так что с помощью этого параметра можно ограничить '
             f'длину текста.'
    }
    return help_msg


def get_settings(*args) -> str:
    settings_msg: str = f'<b>🛠 Настройки 🛠</b>\n\n' \
                        f'<b>В этом меню вы может сделать более тонкую настройку модели.</b>\n\n' \
                        f'<em>Подробнее о том что такое модели можно узнать, вызвав команду /help</em>\n\n' \
                        f'Чтобы приступить к настройке - выберите модель, которую хотите изменить.'
    return settings_msg


def get_upgrades(*args) -> str:
    upgrades_msg: str = f'<b>🔗 Магазин 🔗</b>\n\n' \
                        f'<b>Различные улучшения бота</b>\n\n' \
                        f'<em>Внимание! Все платежи официальные и проходят с помощью <b>ЮКасса</b></em>\n' \
                        f'<em>После подтверждения оплаты, вы получите чек по почте, которую укажите.</em>\n' \
                        f'<em>В случае возникновения спорных ситуаций - вы всегда можете вернуть свой платеж, ' \
                        f'либо обратиться за помощью к администратору.</em>'
    return upgrades_msg


def get_subscription(*args) -> str:
    subscription_msg: str = f'<b>🗝 Подписка 🗝</b>\n\n' \
                            f'<b>Выберите подходящую подписку</b>'
    return subscription_msg


def get_default_sub(*args) -> str:
    subpay_msg: str = f'<b>🗝 Обычная подписка 🗝</b>\n\n' \
                      f'<em>Включает в себя 1,500,000 токенов каждую неделю</em>\n\n' \
                      f'<b>Доступны подписки на:</b>\n' \
                      f'<em>1 месяц - 150 ₽</em>\n' \
                      f'<em>3 месяца - 400 ₽</em>\n' \
                      f'<em>6 месяцев - 750 ₽</em>\n'
    return subpay_msg


def get_premium_sub(*args) -> str:
    premium_msg: str = f'<b>🗝 Премиум подписка 🗝</b>\n\n' \
                       f'<em>Включает в себя 10,000,000 токенов каждую неделю</em>\n\n' \
                       f'<b>Доступны подписки на:</b>\n' \
                       f'<em>1 месяц - 300 ₽</em>\n' \
                       f'<em>3 месяца - 780 ₽</em>\n' \
                       f'<em>6 месяцев - 1450 ₽</em>\n'
    return premium_msg


def get_unlimited_sub(*args) -> str:
    unlimited_msg: str = f'<b>🗝 Безлимитная подписка 🗝</b>\n\n' \
                         f'<em>Включает в себя безлимитное количество токенов</em>\n\n' \
                         f'<b>Доступны подписки на:</b>\n' \
                         f'<em>1 месяц - 650 ₽</em>\n' \
                         f'<em>3 месяца - 1750 ₽</em>\n' \
                         f'<em>6 месяцев - 3200 ₽</em>\n'
    return unlimited_msg


def get_pay(*args) -> str:
    pay_msg: str = f'<b>💎Подписка💎</b>\n\n'
    return pay_msg


def get_reduction(*args) -> str:
    reduction_msg: str = f'<b>💎 Снижение задержки 💎</b>\n\n' \
                         f'<b>Преимущества:\n- Снижение задержки</b> между запросами <b>до 5 секунд</b>\n\n' \
                         f'<em>Для перехода к оплате нажмите кнопку</em> <b>«Купить»</b>'
    return reduction_msg


def cat_tokens(*args) -> str:
    tokens_msg: str = f'<b>✅ Выберите способ оплаты</b>\n\n' \
                      f'<em>Внимание! Все платежи официальные и проходят с помощью <b>ЮКасса</b></em>\n' \
                      f'<em>После подтверждения оплаты, вы получите чек по почте, которую укажите.</em>\n' \
                      f'<em>В случае возникновения спорных ситуаций - вы всегда можете вернуть свой платеж,' \
                      f'либо обратиться за помощью к администратору</em>'
    return tokens_msg


def cat_cardpay(*args) -> str:
    cardpay_msg: str = f'<b>♻️  Восстановление токенов</b>\n\n' \
                       f'<em>🎟 100,000 токенов - 60 ₽</em>\n' \
                       f'<em>🎟 200,000 токенов - 95 ₽</em>\n' \
                       f'<em>🎟 500,000 токенов - 200 ₽</em>\n' \
                       f'<em>🎟 1,000,000 токенов - 350 ₽</em>\n'
    return cardpay_msg


def cat_criptopay(*args) -> str:
    criptopay_msg: str = f'<b>Скоро будет добавлено!</b>\n\n'
    return criptopay_msg


def change_models(current_state: str, current_temperature, current_tokens) -> str:
    models_msg: str = f'<b>Выбрана модель {current_state.split(":")[-1]}</b>\n\n' \
                      f'<b>Вы можете изменить следующие параметры:</b>\n' \
                      f'Temperature - чем выше этот параметр, тем разнообразнее ответы.\n\n' \
                      f'<em>Temperature</em>: <b>{current_temperature} / 1.0</b>\n' \
                      f'<em>Tokens</em>: <b>{current_tokens}/ 4000</b>\n'

    return models_msg


MENU_LEXICON: Dict[str, Callable[[str | Any], str]] = {
    'cat_menu': get_main_menu,
    'cat_profile': get_profile,
    'cat_referral': get_referral,
    'cat_models': get_models_info,
    'cat_help': get_help,
    'cat_upgrades': get_upgrades,
    'cat_settings': get_settings,
    'cat_subscription': get_subscription,
    'cat_default_sub': get_default_sub,
    'cat_premium_sub': get_premium_sub,
    'cat_unlimited_sub': get_unlimited_sub,
    'cat_reduction': get_reduction,
    'cat_tokens': cat_tokens,
    'cat_cardpay': cat_cardpay,
    'cat_criptopay': cat_criptopay,
    'change_models': change_models
}
