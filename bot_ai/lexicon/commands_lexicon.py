from collections import namedtuple
from typing import Type

COMMANDS = {
    'menu': 'Меню',
    'help': 'Помощь',
    'set': 'Установить модель',
    'ask': 'Задать вопрос',
    'feedback': 'Обратная связь, через /f тоже работает',
    'reset': 'Сброс модели',
}

HelpMenu: Type['HelpMenu'] = namedtuple('HelpMenu', COMMANDS.keys())

help_menu: HelpMenu = HelpMenu(*COMMANDS.keys())
