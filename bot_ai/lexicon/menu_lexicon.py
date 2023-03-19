from typing import Dict, Callable


def get_profile(first_name, count_questions, tokens_count, refresh_time, balance, subscription) -> str:
    profile_msg: str = f'<b>📊Ваш профиль:</b>\n\n' \
                       f'<b>👤Имя:</b> {first_name}\n' \
                       f'<b>🔸Задано вопросов:</b> {count_questions}\n' \
                       f'<b>🔹Токенов осталось:</b> {tokens_count}\n' \
                       f'<b>⏳До восстановления:</b> {refresh_time}\n\n' \
                       f'<b>💰Баланс:</b> {balance}\n' \
                       f'<b>💎Подписка:</b> {subscription}\n\n' \
                       f'<em>❓Подробнее про токены! - /help</em>'
    return profile_msg


def get_referral(referral_count) -> str:
    referral_msg: str = f'<b>📊Реферальная система:</b>\n\n' \
                        f'<b>👤Рефералов:</b> {referral_count}\n\n' \
                        f'<em>🔥За каждого приведенного пользователя вы получите 50₽:</em>\n\n' \
                        f'<em>⚡Чтобы пригласить пользователя: нажмите кнопку <b>"ПРИГЛАСИТЬ"</b>:</em>'
    return referral_msg


def get_search(current_search) -> str:
    search_msg: str = f'<b>⭐РЕЖИМ ПОИСКА⭐</b>\n\n' \
                      f'<b>🔶Активный режим поиска:</b>\n' \
                      f'<b>{current_search}</b>\n\n'

    return search_msg


MENU_LEXICON: Dict[str, Callable[[str], str]] = {
    'cat_profile': get_profile,
    'cat_referral': get_referral,
    'cat_search': get_search,
}
