import random
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, InputMedia
from aiogram.dispatcher.filters import Text
from aiogram.utils.exceptions import MessageNotModified
from aiogram.dispatcher import FSMContext
from contextlib import suppress
from dotenv import load
from datetime import time, timedelta, date, datetime

from utils import *
from keyboards import *
import mysql
import os


load()


storage = MemoryStorage()
bot = Bot(token=os.getenv('TOKEN'), parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot=bot, storage=storage)


async def update_media(message: types.Message, photo, page_all, page_now, description):
    with suppress(MessageNotModified):
        media_ = InputMedia(type='photo', media=photo, caption=description)
        await message.edit_media(media_, reply_markup=get_pagination(page_now, page_all))


async def update_message(message: types.Message, text: str, keyboard: InlineKeyboardMarkup):
    with suppress(MessageNotModified):
        await message.edit_text(text, reply_markup=keyboard())


@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    if not mysql.get_user(message.from_user.id):
        mysql.add_user(message.from_user.id)
    await message.answer("Рады приветствовать тебя в CAROHOLICS!\n\nCAROHOLICS-это карточная игра для любителей автоиндустрии\n\nСобирай коллекцию любимых машин, копи очки и соревнуйся с друзьями!\n\nНачнём?",
                         reply_markup=get_general_keyboard())


@dp.message_handler(Text(equals='🚙 Получить карту'))
async def command_get_card(message: types.Message):
    user_info = mysql.get_user(message.from_user.id)
    print(user_info)
    if user_info.get('attemp', 0) > 0:
        mysql.un_attemp(message.from_user.id)
        card_id = random.randint(1, 138)
        mysql.add_card(card_id, message.from_user.id)
        all_cards = mysql.get_cards_user(message.from_user.id)
        count_cards = sum([i['get_point'] for i in all_cards])
        card = [i for i in all_cards if i['id'] == card_id][0]
        await message.answer_photo(photo=open(card['url'], 'rb'), caption=f"🚙 Забирай свою новую тачку!\n\n💎 Редкость: {convert_type(card['type_card'])} +{card['get_point']} pts\n🏠 Всего у тебя: {count_cards} pts")
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
            card_id = random.randint(1, 138)
            mysql.add_card(card_id, message.from_user.id)
            all_cards = mysql.get_cards_user(message.from_user.id)
            count_cards = sum([i['get_point'] for i in all_cards])
            card = [i for i in all_cards if i['id'] == card_id][0]
            await message.answer_photo(photo=open(card['url'], 'rb'), caption=f"🚙 Забирай свою новую тачку!\n\n💎 Редкость: {convert_type(card['type_card'])} +{card['get_point']} pts\n🏠 Всего у тебя: {count_cards} pts")
            mysql.add_date_attemp(message.from_user.id, (date_now + timedelta(hours=4)).strftime('%Y-%m-%d %H:%M:%S'))





@dp.message_handler(Text(equals="🏠 Мой гараж"))
async def command_my_garazhe(message: types.Message, state: FSMContext):
    result = mysql.get_cards_user(message.from_user.id)
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


@dp.message_handler(Text(equals="🏟 Universe"))
async def command_menu(message: types.Message):
    await message.answer('💬 Выберите действие по кнопкам ниже', reply_markup=get_universe_keyboard())


@dp.callback_query_handler(Text(equals='games'))
async def callback_games(callback: types.CallbackQuery):
    await callback.answer('Игры')
    text = "💬 Выберете игру из списка"
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
    result = await bot.send_dice(chat_id=callback.from_user.id, emoji="🎲")
    number = result.dice.value
    await callback.message.answer(f'На 🎲 кубике число <b>{number}</b>\n\nВы получаете <b>{number}</b> бесплатных попыток на открытие карт')
    # запрос к базе данных на пополнение попыток - количство на кубике


@dp.callback_query_handler(Text(equals='game_kazino'))
async def command_kazino(callback: types.CallbackQuery):
    text = f"🎰 Ты получишь <b>10</b> попыток, если автомат выдаст <b>3</b> одинаковых символа.\n\n\n💸 Стоимость одной попытки - <b>50 рублей</b>\n\nМаксимум в день игр: <b>14</b>\n\n💰 Бро, у тебя на балансе: <b>0 руб</b>"
    await update_message(callback.message, text, get_kazino_keyboard)


@dp.callback_query_handler(Text(equals='game_kazino_play'))
async def command_play_kazino(callback: types.CallbackQuery):
    result = await bot.send_dice(chat_id=callback.from_user.id, emoji="🎰") # 43-(lime), 64-(777), 1-(bar bar bar), 22-(sliva)
    # запрос к базе данных на списание 50 рублей
    if result.dice.value in [1, 43, 64, 22]:
        await callback.message.answer(f'Вы выигали 10 попыток\nСыграть еще раз', reply_markup=get_kazino_keyboard())
        # запрос в базу данных пополнить на 10 попыток пользователю
    else:
        await callback.message.answer(f'Не повезло\nПопробуйте в другой раз', reply_markup=get_kazino_keyboard())


@dp.callback_query_handler(Text(equals='game_bouling'))
async def command_bouling(callback: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['bouling'] = 5
    text = f"🎳 Ты получишь 1 попытку, если собъешь все кегли за 5 игр.\n\n\n💸 Стоимость 1 игры (5 бросков) - <b>100 рублей</b>\n\nМаксимум в день покупок: <b>1</b>\n\n💰 Бро, у тебя на балансе: <b>0 руб</b>"
    await update_message(callback.message, text, get_bouling_keyboard)


@dp.callback_query_handler(Text(equals='game_bouling_play'))
# добавить в базу данных что купить это можно только 1 раз в день
async def command_play_bouling(callback: types.CallbackQuery, state: FSMContext):
    # если успешно сняли с баласа 100 рублей -> записываем ему 5 попыток
    async with state.proxy() as data:
        if data['bouling'] == 0:
            await callback.message.delete()
            await callback.message.answer('Ты израсходовал лимит игр', reply_markup=get_bouling_keyboard())
        else:
            data['bouling'] -= 1
            result = await bot.send_dice(chat_id=callback.from_user.id, emoji="🎳")
            number = result.dice.value
            if number == 6:
                await callback.message.answer('Вы выиграли 1 попытку', reply_markup=get_bouling_keyboard())
            else:
                await callback.message.answer('Неудача, попробовать еще раз', reply_markup=get_bouling_keyboard())


@dp.callback_query_handler(Text(equals='game_basketball'))
async def command_basketball(callback: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['basketball'] = 6
        data['basketball_point'] = 0
    text = f"🏀 Ты получишь 5 попыток, если забросишь 3 мяча из 6\n\n\n💸 Стоимость 1 игры (6 бросков) - <b>100 рублей</b>\n\nМаксимум в день покупок: <b>1</b>\n\n💰 Бро, у тебя на балансе: <b>0 руб</b>"
    await update_message(callback.message, text, get_basketball_keyboard)


@dp.callback_query_handler(Text(equals='game_basketball_play'))
# добавить в базу данных что купить это можно только 1 раз в день
async def command_play_basketball(callback: types.CallbackQuery, state: FSMContext):
    # если успешно сняли с баласа 100 рублей -> записываем ему 5 попыток
    async with state.proxy() as data:
        if data['basketball'] == 0:
            await callback.message.delete()
            if data['basketball_point'] > 2:
                await callback.message.answer('Вы выигали 5 попыток', reply_markup=get_basketball_keyboard())
            else:
                await callback.message.answer('Ты израсходовал лимит игр и ничего не выиграл', reply_markup=get_basketball_keyboard())
        else:
            data['basketball'] -= 1
            result = await bot.send_dice(chat_id=callback.from_user.id, emoji="🏀")
            number = result.dice.value
            if number > 3:
                data['basketball_point'] += 1
                await callback.message.answer('Вы попали продолжайте', reply_markup=get_basketball_keyboard())
            else:
                await callback.message.answer('Неудача, попробовать еще раз', reply_markup=get_basketball_keyboard())


@dp.callback_query_handler(Text(equals='game_darts'))
async def command_darts(callback: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['darts'] = 5
        data['darts_point'] = False
    text = f"🎯 Ты получишь 1 попытку, если попадешь в центр за 5 игр.\n\n\n💸 Стоимость 1 игры (5 бросков) - <b>100 рублей</b>\n\nМаксимум в день покупок: <b>1</b>\n\n💰 Бро, у тебя на балансе: <b>0 руб</b>"
    await update_message(callback.message, text, get_darts_keyboard)


@dp.callback_query_handler(Text(equals='game_darts_play'))
# добавить в базу данных что купить это можно только 1 раз в день
async def command_play_darts(callback: types.CallbackQuery, state: FSMContext):
    # если успешно сняли с баласа 100 рублей -> записываем ему 5 попыток
    async with state.proxy() as data:
        if data['darts'] == 0:
            await callback.message.delete()
            if data['darts_point'] == True:
                await callback.message.answer('Вы выигали 1 попытку, так как попали в центр и израсходовали лимит', reply_markup=get_darts_keyboard())
            else:
                await callback.message.answer('Ты израсходовал лимит игр и ничего не выиграл', reply_markup=get_darts_keyboard())
        else:
            data['darts'] -= 1
            result = await bot.send_dice(chat_id=callback.from_user.id, emoji="🎯")
            number = result.dice.value
            if number == 6:
                data['darts_point'] = True
                await callback.message.answer('Вы попали продолжайте', reply_markup=get_darts_keyboard())
            else:
                await callback.message.answer('Неудача, попробовать еще раз', reply_markup=get_darts_keyboard())

        
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)