from typing import Union, Dict, List, Tuple

MAIN_MENU: Dict[str, List[Union[Tuple[str, str], Tuple[int]]]] = {
    'main_menu': [
        ('ПРОФИЛЬ', 'cat_profile'),
        ('МАГАЗИН', 'cat_shop'),
        ('ПОПОЛНИТЬ БАЛАНС', 'cat_balance'),
        ('ПОМОЩЬ', 'cat_help'),
        ('РЕЖИМ ПОИСКА', 'cat_search'),
        (2, 1, 2)
    ],
    'profile': [
        ('РЕФЕРАЛЬНАЯ СИСТЕМА', ''),
        ('НАЗАД', ''),
    ],
    'referal': [
        ('ПРИГЛАСИТЬ', ''),
        ('НАЗАД', ''),
    ],

}
