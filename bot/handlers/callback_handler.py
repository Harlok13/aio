@dp.callback_query_handler()
async def callback_random_photo(callback: types.CallbackQuery):
    """Обрабатывает колбеки при нажатии на инлайн клавиатуре send_random_photo"""
    if callback.data == 'like':
        await callback.answer('Вам понравилось!')
    elif callback.data == 'dislike':
        await callback.answer('Вам не понравилось!')
    else:
        await send_random(message=callback.message)
        await callback.answer()
