def profile(first_name, count_questions, tokens_count, refresh_time, balance, subscription) -> str:
    msg: str = f'<b>📊Ваш профиль:</b>\n\n' \
               f'<b>👤Имя:</b> {first_name}\n' \
               f'<b>🔸Задано вопросов:</b> {count_questions}\n' \
               f'<b>🔹Токенов осталось:</b> {tokens_count}\n' \
               f'<b>⏳До восстановления:</b> {refresh_time}\n\n' \
               f'<b>💰Баланс:</b> {balance}\n' \
               f'<b>💎Подписка:</b> {subscription}\n\n' \
               f'<em>❓Подробнее про токены! - /help</em>'
    return msg
