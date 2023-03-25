def get_current_state_info(data_state: str) -> str:
    """
    Get readable data of state
    FSMOpenaiModel:set_standard -> ('FSMOpenaiModel', ':', 'set_standard') -> set_standard
    :param: the value from state.get_state()
    """
    return data_state.partition(':')[2]
