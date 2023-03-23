from bot_ai.utils.user_requsts import ProfileInfo


def get_current_tokens_info(profile: ProfileInfo) -> str:
    """
       Set the display of the current number of tokens
       :profiles: ProfileInfo
       :return: current tokens value
       """
    limit: int = 15_000_000  # wtf...
    return 'unlimited' if profile.token_count > limit else profile.token_count


def get_counter_days_info(profile: ProfileInfo) -> str:
    """
    Set the display of the counter days
    :profiles: ProfileInfo
    :return: counter days value
    """
    return '<b>Подписка:</b>' if profile.status != 'standard' else '<b>До восстановления:</b>'
