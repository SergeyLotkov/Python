from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton, 
                            InlineKeyboardMarkup, InlineKeyboardButton)


main = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Основное меню')],
        [KeyboardButton(text='Барное меню')],
        [KeyboardButton(text='Основы сервиса')]
    ],
    resize_keyboard=True,
    input_field_placeholder='Выберите раздел'
)

catalog = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Супы', callback_data='soop')],
    [InlineKeyboardButton(text='Горячие блюда', callback_data='Hot')],
    [InlineKeyboardButton(text='Роллы',callback_data='Rolls')]
    ]
)

get_number = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Отпрвить номер', 
                                                        request_contact=True)]],
                                                        resize_keyboard=True)
