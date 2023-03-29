from typing import Tuple

from aiogram.fsm.state import StatesGroup, State


class FSMOpenaiModel(StatesGroup):
    set_standard: State = State()
    set_companion: State = State()
    set_artist: State = State()
    set_translator: State = State()
    set_coder: State = State()

    @classmethod
    def get_all_models(cls) -> Tuple[State, ...]:
        """
        Returns all models for the FSMOpenaiModel state filter
        :return: Tuple[State, ...]
        """
        return (
            cls.set_standard,
            cls.set_companion,
            cls.set_artist,
            cls.set_translator,
            cls.set_coder
        )


class FSMOpenaiModelSettings(StatesGroup):
    ...
