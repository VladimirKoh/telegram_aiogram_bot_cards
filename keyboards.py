from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove


def get_pagination(page_now, page_all) -> InlineKeyboardMarkup:
    ikb = InlineKeyboardMarkup(row_width=3)
    ib1 = InlineKeyboardButton('<<', callback_data='back')
    ib2 = InlineKeyboardButton(f'{page_now + 1}/{page_all}', callback_data='xyu')
    ib3 = InlineKeyboardButton('>>', callback_data='next')
    ikb.add(ib1, ib2, ib3)
    return ikb


def get_general_keyboard() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    b1 = KeyboardButton('🚙 Получить карту')
    b2 = KeyboardButton('🏠 Мой гараж')
    b3 = KeyboardButton('🏟 Universe')
    kb.add(b1, b2, b3)
    return kb


def get_universe_keyboard() -> InlineKeyboardMarkup:
    ikb = InlineKeyboardMarkup(row_width=1)
    ib1 = InlineKeyboardButton('Caroholics Membership', callback_data='1')      # pay
    ib2 = InlineKeyboardButton('Игры', callback_data='games')                       # games
    ib3 = InlineKeyboardButton('Tuning', callback_data='3')                     # craft cards
    ib4 = InlineKeyboardButton('Топ 10 Игроков Сезона', callback_data='4')      # top month
    ib5 = InlineKeyboardButton('Топ 10 Игроков за все время', callback_data='5')# top all
    ikb.add(ib1, ib2, ib3, ib4, ib5)
    return ikb


def get_games_keyboard() -> InlineKeyboardMarkup:
    ikb = InlineKeyboardMarkup(row_width=1)
    ib1 = InlineKeyboardButton('🎰 Казик', callback_data='game_kazino')
    ib2 = InlineKeyboardButton('🎲 Кубик', callback_data='game_cube')
    ib3 = InlineKeyboardButton('🎳 Спотбоул', callback_data='game_bouling')
    ib4 = InlineKeyboardButton('🏀 3х3', callback_data='game_basketball')
    ib5 = InlineKeyboardButton('🎯 Битва за чекушку', callback_data='game_darts')
    ikb.add(ib1, ib2, ib3, ib4, ib5)
    return ikb


def get_kazino_keyboard() -> InlineKeyboardMarkup:
    ikb = InlineKeyboardMarkup(row_width=1)
    ib1 = InlineKeyboardButton('🎰 Сыграть', callback_data='game_kazino_play')
    ib2 = InlineKeyboardButton('💰 Пополнить баланс', callback_data='up_pay')
    ikb.add(ib1, ib2)
    return ikb


def get_bouling_keyboard() -> InlineKeyboardMarkup:
    ikb = InlineKeyboardMarkup(row_width=1)
    ib1 = InlineKeyboardButton('🎳 Сыграть', callback_data='game_bouling_play')
    ib2 = InlineKeyboardButton('💵 Купить 5 бросков', callback_data='pay_5_bouling')
    ib3 = InlineKeyboardButton('💰 Пополнить баланс', callback_data='up_pay')
    ikb.add(ib1, ib2, ib3)
    return ikb