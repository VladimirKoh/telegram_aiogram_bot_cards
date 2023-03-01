from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

from yandex import payment_yandex


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
    ib1 = InlineKeyboardButton('🪪 Caroholics Membership', callback_data='pay_spot_pass')      # pay
    ib2 = InlineKeyboardButton('🎮 Игры', callback_data='games')                               # games
    ib3 = InlineKeyboardButton('🛠️ Tuning', callback_data='tuning')                                  # craft cards
    ib4 = InlineKeyboardButton('🏆 Топ 10 Игроков Сезона', callback_data='top_10_players_seasone') # top month
    ib5 = InlineKeyboardButton('🏆 Топ 10 Игроков за все время', callback_data='top_10_players')   # top all
    ikb.add(ib1, ib2, ib3, ib4, ib5)
    return ikb


def get_games_keyboard() -> InlineKeyboardMarkup:
    ikb = InlineKeyboardMarkup(row_width=1)
    ib1 = InlineKeyboardButton('🎰 Казино', callback_data='game_kazino')
    ib2 = InlineKeyboardButton('🎲 Кубик', callback_data='game_cube')
    ib3 = InlineKeyboardButton('🎳 Боулинг', callback_data='game_bouling')
    ib4 = InlineKeyboardButton('🏀 Баскетбол', callback_data='game_basketball')
    ib5 = InlineKeyboardButton('🎯 Дартс', callback_data='game_darts')
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
    # ib2 = InlineKeyboardButton('💵 Купить 5 бросков', callback_data='pay_5_bouling')
    ib3 = InlineKeyboardButton('💰 Пополнить баланс', callback_data='up_pay')
    ikb.add(ib1, ib3)
    return ikb


def get_basketball_keyboard() -> InlineKeyboardMarkup:
    ikb = InlineKeyboardMarkup(row_width=1)
    ib1 = InlineKeyboardButton('🏀 Сыграть', callback_data='game_basketball_play')
    # ib2 = InlineKeyboardButton('💵 Купить 6 бросков', callback_data='pay_6_basketball')
    ib3 = InlineKeyboardButton('💰 Пополнить баланс', callback_data='up_pay')
    ikb.add(ib1, ib3)
    return ikb


def get_darts_keyboard() -> InlineKeyboardMarkup:
    ikb = InlineKeyboardMarkup(row_width=1)
    ib1 = InlineKeyboardButton('🎯 Сыграть', callback_data='game_darts_play')
    # ib2 = InlineKeyboardButton('💵 Купить 5 бросков', callback_data='pay_5_darts')
    ib3 = InlineKeyboardButton('💰 Пополнить баланс', callback_data='up_pay')
    ikb.add(ib1, ib3)
    return ikb


def get_spot_pass_keyboard() -> InlineKeyboardMarkup:
    ikb = InlineKeyboardMarkup(row_width=1)
    ib1 = InlineKeyboardButton('💵 Купить Caroholics Membership', callback_data='pay_balance_spot_pass')
    ikb.add(ib1)
    return ikb


def get_url_pay_169(label) -> InlineKeyboardMarkup:
    ikb = InlineKeyboardMarkup(row_width=1)
    ib1 = InlineKeyboardButton('Перейти к оплате', url=payment_yandex(169, label))
    ib2 = InlineKeyboardButton('✅ Я оплатил(а)', callback_data=f'check_pay_spot_pass_{label}')
    ikb.add(ib1, ib2)
    return ikb


def get_url_pay_summa(label, summa) -> InlineKeyboardMarkup:
    ikb = InlineKeyboardMarkup(row_width=1)
    ib1 = InlineKeyboardButton('Перейти к оплате', url=payment_yandex(int(summa), label))
    ib2 = InlineKeyboardButton('✅ Я оплатил(а)', callback_data=f'check_pay_{label}')
    ikb.add(ib1, ib2)
    return ikb


def cancel_keyboard() -> InlineKeyboardMarkup:
    ikb = InlineKeyboardMarkup(row_width=1)
    ib1 = InlineKeyboardButton('🚫 Отменить', callback_data='cancel_pay')
    ikb.add(ib1)
    return ikb


def tuning_keyboard() -> InlineKeyboardMarkup:
    ikb = InlineKeyboardMarkup(row_width=1)
    ib1 = InlineKeyboardButton('Скрафтить из 10 Basic', callback_data='basic_tuning')
    ib2 = InlineKeyboardButton('Скрафтить из 10 Civil', callback_data='basic_tuning')
    ib3 = InlineKeyboardButton('Скрафтить из 5 Rare', callback_data='basic_tuning')
    ib4 = InlineKeyboardButton('Скрафтить из 5 Extra', callback_data='basic_tuning')
    ikb.add(ib1, ib2, ib3, ib4)
    return ikb