import math
import random
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, InputMedia
from aiogram.dispatcher.filters import Text
from aiogram.utils.exceptions import MessageNotModified
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from contextlib import suppress
from dotenv import load
from datetime import time, timedelta, date, datetime

from utils import *
from keyboards import *
import mysql
import os

from yandex import sucsess_pay


load()


storage = MemoryStorage()
bot = Bot(token=os.getenv('TOKEN'), parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot=bot, storage=storage)


class ClientStatesGroup(StatesGroup):
    summa_payment = State()


async def update_media(message: types.Message, photo, page_all, page_now, description):
    with suppress(MessageNotModified):
        media_ = InputMedia(type='photo', media=photo, caption=description)
        await message.edit_media(media_, reply_markup=get_pagination(page_now, page_all))


async def update_message(message: types.Message, text: str, keyboard: InlineKeyboardMarkup):
    if keyboard == None:
        with suppress(MessageNotModified):
            await message.edit_text(text)
    else:
        with suppress(MessageNotModified):
            await message.edit_text(text, reply_markup=keyboard())


async def edit_text_and_keyboard(message: types.Message, new_text: str, func: InlineKeyboardMarkup, label: int):
    with suppress(MessageNotModified):
        if label:
            await message.edit_text(new_text, reply_markup=func(label))
        else:
            await message.edit_text(new_text, reply_markup=func())


async def edit_text_and_keyboard2(message: types.Message, new_text: str, func: InlineKeyboardMarkup, label: int, summa):
    with suppress(MessageNotModified):
        if label:
            await message.edit_text(new_text, reply_markup=func(label, summa))
        else:
            await message.edit_text(new_text, reply_markup=func())


@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    if not mysql.get_user(message.from_user.id):
        mysql.add_user(message.from_user.id, message.from_user.username)
    await message.answer("""🚘 Рады приветствовать тебя в CAROHOLICS!

👥 CAROHOLICS-это карточная игра для любителей автоиндустрии

🃏 Собирай коллекцию любимых машин, копи очки и соревнуйся с друзьями!

🔸В игре есть карты следующих редкостей:
⚪️ Basic (+250)
🟢 Civil (+500)
🔵 Rare (+1000)
🟣 Extra (+2500)
🟡 Exclusive (+5000)

🏁 Начнём?""", reply_markup=get_general_keyboard())


@dp.message_handler(Text(equals='🚙 Получить карту'))
async def command_get_card(message: types.Message):
    user_info = mysql.get_user(message.from_user.id)
    print(user_info)
    if user_info.get('attemp', 0) > 0:
        if user_info.get('spot_pass', 0):
            type_card = random_card(True)
        else:
            type_card = random_card(False)
        card_user = mysql.get_random_card(type_card)
        mysql.add_card(card_user['id'], message.from_user.id)
        all_cards = mysql.get_cards_user(message.from_user.id)
        count_cards = sum([i['get_point'] for i in all_cards])
        # card = [i for i in all_cards if i['id'] == card_id][0]
        await message.answer_photo(photo=open(card_user['url'], 'rb'), caption=f"🚙 Забирай свою новую тачку!\n\n💎 Редкость: {convert_type(card_user['type_card'])} (+{card_user['get_point']} pts)\n🏠 Всего у тебя: ({count_cards} pts)")
    else:
        date_now = datetime.now()
        formatted_date_now = date_now.strftime('%Y-%m-%d %H:%M:%S')
        print(formatted_date_now)
        if user_info['date_attemp'] > date_now:
            delta = user_info['date_attemp'] - date_now
            s = delta.seconds
            h, s = divmod(s, 3600)
            m, s = divmod(s, 60)
            if delta < timedelta(hours=1):
                await message.answer(f'Следующая попытка будет доступна\n через {m} мин')
            else:
                await message.answer(f'Следующая попытка будет доступна\nчерез {h} ч {m} минут')
        else:
            # механизм получения карты 
            if user_info.get('spot_pass', 0):
                type_card = random_card(True)
            else:
                type_card = random_card(False)
                card_user = mysql.get_random_card(type_card)
                mysql.add_card(card_user['id'], message.from_user.id)
                all_cards = mysql.get_cards_user(message.from_user.id)
                count_cards = sum([i['get_point'] for i in all_cards])
            await message.answer_photo(photo=open(card_user['url'], 'rb'), caption=f"🚙 Забирай свою новую тачку!\n\n💎 Редкость: {convert_type(card_user['type_card'])} (+{card_user['get_point']} pts)\n🏠 Всего у тебя: ({count_cards} pts)")
            mysql.add_date_attemp(message.from_user.id, (date_now + timedelta(hours=4)).strftime('%Y-%m-%d %H:%M:%S'))


@dp.message_handler(Text(equals="🏠 Мой гараж"))
async def command_my_garazhe(message: types.Message, state: FSMContext):
    result = mysql.get_cards_user_distinct(message.from_user.id)
    # result2 = mysql.get_cards_user(message.from_user.id)
    # с оптимизировать
    count_points = sum([i['get_point'] for i in result])
    page_all = len(result)
    description = f"🚙 Мои карты\n\n🏠 Всего очков {count_points}"
    async with state.proxy() as data:
        data['page'] = 0
        data['page_all'] = page_all
        data['data'] = result
        data['count_points'] = count_points
    print(data['data'])
    await message.answer_photo(open(result[0]['url'], 'rb'),
                               caption=description,
                               reply_markup=get_pagination(data['page'], data['page_all']))


@dp.callback_query_handler(Text(equals="basic_tuning"))
async def callback_up_pay(callback: types.CallbackQuery):
    await callback.answer('⚠️ У вас недостаточно дубликатов')


@dp.message_handler(Text(equals="🏟 Universe"))
async def command_menu(message: types.Message):
    await message.answer('💬 Выберите действие по кнопкам ниже', reply_markup=get_universe_keyboard())


@dp.callback_query_handler(Text(equals="up_pay"))
async def callback_up_pay(callback: types.CallbackQuery):
    await callback.message.answer('💬 Введите сумму пополнения', reply_markup=cancel_keyboard())
    await ClientStatesGroup.summa_payment.set()


@dp.message_handler(lambda message: not message.text.isdigit(), state=ClientStatesGroup.summa_payment)
async def check_name(message: types.Message):
    await message.reply('Введите число')


@dp.message_handler(lambda message: message.text.isdigit(),state=ClientStatesGroup.summa_payment)
async def message_name(message: types.Message, state: FSMContext):
    summa = message.text
    print(summa)
    label = int(message.from_user.id) + random.randint(10, 99)
    text = "🔑 Оплатите покупку\nиспользуя кнопку ниже\n❗ Посли оплаты нажмите кнопку '✅Я оплатил(а)'"
    await message.answer(text, reply_markup=get_url_pay_summa(label, summa))
    await state.finish()
    # await edit_text_and_keyboard2(message, text, get_url_pay_summa, label, summa)


@dp.callback_query_handler(Text(equals="cancel_pay"), state='*')
async def callback_up_pay(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.delete()
    await state.finish()


@dp.callback_query_handler(Text(equals="pay_balance_spot_pass"))
async def callback_pay_balance_spot_pass(callback: types.CallbackQuery):
    await callback.answer(None)
    label = int(callback.from_user.id) + random.randint(10, 99)
    text = "🔑 Для приобретения Caroholics Membership оплатите покупку\nвоспользовавшись этой ссылкой\nИли используя кнопку ниже\n❗ Посли оплаты нажмите кнопку '✅Я оплатил(а)'"
    await edit_text_and_keyboard(callback.message, text, get_url_pay_169, label)


@dp.callback_query_handler(Text(startswith='check_pay_'))
async def callback_check_balance_pay(callback: types.CallbackQuery):
    label = callback.data.split('_')[-1]
    result = sucsess_pay(label)
    if result[0]:
        next_data = date.today() + timedelta(30)
        summa_pay = math.ceil(result[1]) + 30
        # стуст spot_pass поставить в значение тру и дату окончания проставить на месяц вперед
        mysql.up_balance(callback.from_user.id, summa_pay)
        mysql.up_spot_pass(callback.from_user.id)

        await callback.message.answer('Платеж успешно прошел', reply_markup=get_universe_keyboard())
    else:
        await callback.answer('⚠️ Платеж не найден\nПопробуйте проверить через несколько секунд.', show_alert=True)


@dp.callback_query_handler(Text(equals="pay_spot_pass"))
async def callback_pay_spot_pass(callback: types.CallbackQuery):
    text = """📈 Внеси вклад в развитие проекта и стань частью сообщества Caroholics!

🪪 Владельцы Caroholics Membership наделяются следующими привилегиями:

⏱️ Уменьшенное время ожидание: 3 часа вместо 4 
🔔 Уведомление о том, что время ожидания закончилось
💸 Повышенный процент выпадения редких карт
🚘 Доступ к коллекционным и редким картам
🎲 Возможность бросать кость 2 раза в неделю вместо 1
📌 Срок действия Caroholics Membership - 30 дней с момента покупки

🪪 Caroholics Membership - 169 рублей"""
    await callback.message.answer(text, reply_markup=get_spot_pass_keyboard())


@dp.callback_query_handler(Text(equals="top_10_players"))
# user_id заменить на ЛОГИНЫ
async def callback_top_10_players(callback: types.CallbackQuery):
    data = mysql.get_top_10_players()
    result_list = list()
    result_list.append('🏆 Топ-10 игроков за все время \n\n')
    for i,j in enumerate(data, 1):
        result_list.append(f"{i}. {j['user_name']} - <b>{int(j['sum_point'])} pts</b>\n")
    text = ''.join(result_list)
    await update_message(callback.message, text, None)


@dp.callback_query_handler(Text(equals="top_10_players_seasone"))
# user_id заменить на ЛОГИНЫ
async def callback_top_10_players_seasone(callback: types.CallbackQuery):
    data = mysql.get_top_10_players_seasone()
    result_list = list()
    result_list.append('🏆 Топ-10 игроков сезона\n\n')
    for i,j in enumerate(data, 1):
        result_list.append(f"{i}. {j['user_name']} - <b>{int(j['sum_point'])} pts</b>\n")
    text = ''.join(result_list)
    await update_message(callback.message, text, None)


@dp.callback_query_handler(Text(equals='tuning'))
async def callback_games(callback: types.CallbackQuery):
    data = mysql.get_cards_user_tuning(callback.from_user.id)
    print(data)
    basic, civil, extra, rare = 0, 0, 0, 0 
    if data:
        for i in data:
            if i['type_card'] == 1:
                basic = i['count_card']
            elif i['type_card'] == 2:
                civil = i['count_card']
            elif i['type_card'] == 3:
                extra = i['count_card']
            elif i['type_card'] == 4:
                rare = i['count_card']

    await callback.answer('Tuning')
    text = f"""🛠️Добро пожаловать в Тюнинг!
Здесь ты можешь обменять дубликаты карт на попытки 

Количество повторок:

Basic: {basic}
Civil: {civil}
Extra: {extra}
Rare: {rare}

10 Basic = 3 попытки
10 Сivil = 9 попыток
5 rare = 1 extra
5 extra = 1 exclusive
"""
    await update_message(callback.message, text, tuning_keyboard)


# @dp.callback_query_handler(Text(equals='basic_tuning'))
# async def callback_basic_tuning(callback: types.CallbackQuery):
#     data = mysql.get_cards_user_tuning(callback.from_user.id)
#     for i in data:
#         if i['type_card'] == 1:
#             count_cards = i['count_cards']
#             if count_cards >= 10:
#                 await callback.message.answer('Вы скрафтили из 10 Basic и получили 3 попытки')



@dp.callback_query_handler(Text(equals='games'))
async def callback_games(callback: types.CallbackQuery):
    await callback.answer('Игры')
    text = "💬 Выберите игру из списка"
    await update_message(callback.message, text, get_games_keyboard)


@dp.callback_query_handler(Text(equals='next'))
async def callback_next(callback: types.CallbackQuery, state: FSMContext):
    await callback.answer(None)
    async with state.proxy() as data:
        if data['page_all'] > data['page'] + 1:
            data['page'] += 1
            url_photo = data['data'][data['page']]['url']
            description = f"🚙 Мои карты\n\n🏠 Всего очков {data['count_points']}"
            await update_media(callback.message, photo=open(url_photo, 'rb'), page_all=data['page_all'], page_now=data['page'], description=description)


@dp.callback_query_handler(Text(equals='back'))
async def callback_back(callback: types.CallbackQuery, state: FSMContext):
    await callback.answer(None)
    async with state.proxy() as data:
        if data['page'] > 0:
            data['page'] -= 1
            url_photo = data['data'][data['page']]['url']
            description = f"🚙 Мои карты\n\n🏠 Всего очков {data['count_points']}"
            await update_media(callback.message, photo=open(url_photo, 'rb'), page_all=data['page_all'], page_now=data['page'], description=description)


@dp.callback_query_handler(Text(equals='game_cube'))
async def command_play(callback: types.CallbackQuery):
    date_cube = mysql.get_date_cube(callback.from_user.id)
    print(date_cube)
    if datetime.now() > date_cube['date_cube']:
        result = await bot.send_dice(chat_id=callback.from_user.id, emoji="🎲")
        number = result.dice.value
        await callback.message.answer(f'На 🎲 кубике число <b>{number}</b>\n\nВы получаете <b>{number}</b> бесплатных попыток на открытие карт')
        mysql.set_date_cube(callback.from_user.id, (datetime.now() + timedelta(7)).strftime('%Y-%m-%d %H:%M:%S'))
        mysql.up_attemp(callback.from_user.id, number)

    else:
        await callback.message.answer('⚠️ На этой неделе броски кубика закончились')


@dp.callback_query_handler(Text(equals='game_kazino'))
async def command_kazino(callback: types.CallbackQuery):
    balance = mysql.get_balance(callback.from_user.id)
    text = f"🎰Готов словить джекпот?\nТы получишь <b>10 попыток</b>, если автомат выдаст <b>3</b> одинаковых символа.\n\n\n💸 Стоимость одной попытки - <b>50 рублей</b>\n\nМаксимум в день игр: <b>14</b>\n\n💵 Твой баланс: <b>{balance['balance']} руб</b>"
    await update_message(callback.message, text, get_kazino_keyboard)


@dp.callback_query_handler(Text(equals='game_kazino_play'))
async def command_play_kazino(callback: types.CallbackQuery):
    balance = mysql.get_balance(callback.from_user.id)
    if balance.get('balance', 0) >= 100:
        mysql.un_balance(callback.from_user.id, 100)
        result = await bot.send_dice(chat_id=callback.from_user.id, emoji="🎰") # 43-(lime), 64-(777), 1-(bar bar bar), 22-(sliva)
        # запрос к базе данных на списание 50 рублей
        if result.dice.value in [1, 43, 64, 22]:
            await callback.message.answer(f'🎉 Джекпот! Тебе начислено 10 попыток', reply_markup=get_kazino_keyboard())
            mysql.up_attemp(callback.from_user.id, 10)
            # запрос в базу данных пополнить на 10 попыток пользователю
        else:
            await callback.message.answer(f'Не повезло☹️\nПопробуем еще раз?', reply_markup=get_kazino_keyboard())
    else:
        await callback.answer('⚠️ Не достаточно средств на балансе')


@dp.callback_query_handler(Text(equals='game_bouling'))
async def command_bouling(callback: types.CallbackQuery, state: FSMContext):
    balance = mysql.get_balance(callback.from_user.id)
    date_bouling = mysql.get_date_bouling(callback.from_user.id)
    if datetime.now() > date_bouling['date_bouling']:
        async with state.proxy() as data:
            data['bouling'] = 5
    else:
        async with state.proxy() as data:
            data['bouling'] = -1
    text = f"🎳 Добро пожаловать в боулинг!\nВыбей страйк за 5 игр и получи <b>1 попытку!</b>\n\n\n💸 Стоимость 1 игры (5 бросков) - <b>50 рублей</b>\n\nМаксимум в день покупок: <b>1</b>\n\n💵 Твой баланс: <b>{balance['balance']} руб</b>"
    await update_message(callback.message, text, get_bouling_keyboard)


@dp.callback_query_handler(Text(equals='game_bouling_play'))
# добавить в базу данных что купить это можно только 1 раз в день
async def command_play_bouling(callback: types.CallbackQuery, state: FSMContext):
    # если успешно сняли с баласа 100 рублей -> записываем ему 5 попыток
    balance = mysql.get_balance(callback.from_user.id)
    if balance.get('balance', 0) >= 50:
        async with state.proxy() as data:
            if data['bouling'] == 0:
                await callback.message.delete()
                mysql.un_balance(callback.from_user.id, 50)
                await callback.message.answer('Ты израсходовал лимит игр')
            elif data['bouling'] < 0:
                await callback.message.answer('Ты израсходовал лимит игр на сегодня')
            else:
                data['bouling'] -= 1
                result = await bot.send_dice(chat_id=callback.from_user.id, emoji="🎳")
                number = result.dice.value
                if number == 6:
                    await callback.message.answer('⭐️ Страйк!\nТебе начислена 1 попытка', reply_markup=get_bouling_keyboard())
                    mysql.set_date_bouling(callback.from_user.id, (datetime.now() + timedelta(1)).strftime('%Y-%m-%d %H:%M:%S'))
                    mysql.up_attemp(callback.from_user.id, 1)
                else:
                    await callback.message.answer('Не повезло☹️\nПопробуем еще раз?', reply_markup=get_bouling_keyboard())

    else:
        await callback.answer('⚠️ Не достаточно средств на балансе')


@dp.callback_query_handler(Text(equals='game_basketball'))
async def command_basketball(callback: types.CallbackQuery, state: FSMContext):
    balance = mysql.get_balance(callback.from_user.id)
    date_basketball = mysql.get_date_basketball(callback.from_user.id)
    if datetime.now() > date_basketball['date_basketball']:
        async with state.proxy() as data:
            data['basketball'] = 6
            data['basketball_point'] = 0
    else:
        async with state.proxy() as data:
            data['basketball'] = -1
            data['basketball_point'] = 0
    text = f"🏀 Добро пожаловать в баскетбол!\nПопади в кольцо 3 раза из 6 и получи 5 попыток!\n\n\n💸 Стоимость 1 игры (6 бросков) - <b>100 рублей</b>\n\nМаксимум в день покупок: <b>1</b>\n\n💵 Твой баланс: <b>{balance['balance']} руб</b>"
    await update_message(callback.message, text, get_basketball_keyboard)


@dp.callback_query_handler(Text(equals='game_basketball_play'))
# добавить в базу данных что купить это можно только 1 раз в день
async def command_play_basketball(callback: types.CallbackQuery, state: FSMContext):
    # если успешно сняли с баласа 100 рублей -> записываем ему 5 попыток
    balance = mysql.get_balance(callback.from_user.id)
    if balance.get('balance', 0) >= 100:
        async with state.proxy() as data:
            if data['basketball'] == 0:
                await callback.message.delete()
                mysql.un_balance(callback.from_user.id, 100)
                if data['basketball_point'] > 2:
                    await callback.message.answer('🏆 Ты победил!\nТебе начислено 5 попыток')
                    mysql.set_date_basketball(callback.from_user.id, (datetime.now() + timedelta(1)).strftime('%Y-%m-%d %H:%M:%S'))
                    mysql.up_attemp(callback.from_user.id, 5)
                else:
                    await callback.message.answer('Ты израсходовал лимит игр и ничего не выиграл')
                    mysql.set_date_basketball(callback.from_user.id, (datetime.now() + timedelta(1)).strftime('%Y-%m-%d %H:%M:%S'))
            elif data['basketball'] < 0:
                await callback.message.answer('Ты израсходовал лимит игр на сегодня')
            else:
                data['basketball'] -= 1
                result = await bot.send_dice(chat_id=callback.from_user.id, emoji="🏀")
                number = result.dice.value
                if number > 3:
                    data['basketball_point'] += 1
                    await callback.message.answer('✨ Ты попал!\nПродолжай в том же духе!', reply_markup=get_basketball_keyboard())
                else:
                    await callback.message.answer('Не повезло☹️\nПопробуем еще раз?', reply_markup=get_basketball_keyboard())
    else:
        await callback.answer('⚠️ Не достаточно средств на балансе')


@dp.callback_query_handler(Text(equals='game_darts'))
async def command_darts(callback: types.CallbackQuery, state: FSMContext):
    balance = mysql.get_balance(callback.from_user.id)
    date_darts = mysql.get_date_darts(callback.from_user.id)
    if datetime.now() > date_darts['date_darts']:
        async with state.proxy() as data:
            data['darts'] = 5
            data['darts_point'] = False
    else:
        async with state.proxy() as data:
            data['darts'] = -1
            data['darts_point'] = False
    text = f"🎯 Добро пожаловать в дартс!\nПопади в яблочко за 5 игр и получи 1 попытку!\n\n\n💸 Стоимость 1 игры (5 бросков) - <b>50 рублей</b>\n\nМаксимум в день покупок: <b>1</b>\n\n💵 Твой баланс: <b>{balance['balance']} руб</b>"
    await update_message(callback.message, text, get_darts_keyboard)


@dp.callback_query_handler(Text(equals='game_darts_play'))
# добавить в базу данных что купить это можно только 1 раз в день
async def command_play_darts(callback: types.CallbackQuery, state: FSMContext):
    # если успешно сняли с баласа 100 рублей -> записываем ему 5 попыток
    balance = mysql.get_balance(callback.from_user.id)
    if balance.get('balance', 0) >= 50:
        async with state.proxy() as data:
            if data['darts'] == 0:
                mysql.un_balance(callback.from_user.id, 50)
                await callback.message.delete()
                if data['darts_point'] == True:
                    await callback.message.answer('У тебя заончились броски.')
                    mysql.set_date_darts(callback.from_user.id, (datetime.now() + timedelta(1)).strftime('%Y-%m-%d %H:%M:%S'))
                else:
                    await callback.message.answer('Ты израсходовал лимит игр на сегодня')
                    mysql.set_date_darts(callback.from_user.id, (datetime.now() + timedelta(1)).strftime('%Y-%m-%d %H:%M:%S'))
            elif data['darts'] < 0:
                await callback.message.answer('Ты израсходовал лимит игр на сегодня')
            else:
                data['darts'] -= 1
                result = await bot.send_dice(chat_id=callback.from_user.id, emoji="🎯")
                number = result.dice.value
                if number == 6:
                    data['darts_point'] = True
                    await callback.message.answer('🔴 В яблочко!\nТебе начислена 1 попытка.', reply_markup=get_darts_keyboard())
                    mysql.up_attemp(callback.from_user.id, 1)
                else:
                    await callback.message.answer('Не повезло☹️\nПопробуем еще раз?', reply_markup=get_darts_keyboard())
    else:
        await callback.answer('⚠️ Не достаточно средств на балансе')

        
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)