import pymysql
from pymysql.cursors import DictCursor
from dotenv import load

import os


load()

def connect():
    return pymysql.connect(host=os.getenv('HOST_DB'),
                                          user=os.getenv('USER_DB'),
                                          password=os.getenv('PASSWORD_DB'),
                                          db=os.getenv('DATABASE_DB'),
                                          charset='utf8mb4',
                                          cursorclass=DictCursor)


def add_user(user_id, user_name):
    connection = connect()
    with connection.cursor() as cursor:
        query = "INSERT INTO `users` (`user_id`, `user_name`) VALUES(%s, %s)"
        cursor.execute(query, (user_id, user_name))
        connection.commit()
    connection.close()


def add_card(id_card: int, user_id: str):
    connection = connect()
    with connection.cursor() as cursor:
        query = "INSERT INTO `users_cards` (`id_card`, `id_user_id`) VALUES(%s, %s)"
        cursor.execute(query, (id_card, user_id))
        connection.commit()
    connection.close()


def add_date_attemp(user_id: str, date_time):
    connection = connect()
    with connection.cursor() as cursor:
        query = f"UPDATE users SET date_attemp = '{date_time}' WHERE user_id = {user_id}"
        cursor.execute(query)
        connection.commit()
    connection.close()


def un_attemp(user_id: str):
    connection = connect()
    with connection.cursor() as cursor:
        query = f"UPDATE users SET attemp = attemp - 1 WHERE user_id = {user_id}"
        cursor.execute(query)
        connection.commit()
    connection.close()


def up_attemp(user_id: str, attemp):
    connection = connect()
    with connection.cursor() as cursor:
        query = f"UPDATE users SET attemp = attemp + {attemp} WHERE user_id = {user_id}"
        cursor.execute(query)
        connection.commit()
    connection.close()


def up_balance(user_id: str, summa):
    connection = connect()
    with connection.cursor() as cursor:
        query = f"UPDATE users SET balance = balance + {summa} WHERE user_id = {user_id}"
        cursor.execute(query)
        connection.commit()
    connection.close()


def un_balance(user_id: str, summa):
    connection = connect()
    with connection.cursor() as cursor:
        query = f"UPDATE users SET balance = balance - {summa} WHERE user_id = {user_id}"
        cursor.execute(query)
        connection.commit()
    connection.close()


def up_spot_pass(user_id):
    connection = connect()
    with connection.cursor() as cursor:
        query = f"UPDATE users SET spot_pass = True WHERE user_id = {user_id}"
        cursor.execute(query)
        connection.commit()
    connection.close()


def set_date_cube(user_id, date_cube):
    connection = connect()
    with connection.cursor() as cursor:
        query = f"UPDATE users SET date_cube = '{date_cube}' WHERE user_id = {user_id}"
        cursor.execute(query)
        connection.commit()
    connection.close()


def set_date_darts(user_id, date_darts):
    connection = connect()
    with connection.cursor() as cursor:
        query = f"UPDATE users SET date_darts = '{date_darts}' WHERE user_id = {user_id}"
        cursor.execute(query)
        connection.commit()
    connection.close()


def set_date_bouling(user_id, date_bouling):
    connection = connect()
    with connection.cursor() as cursor:
        query = f"UPDATE users SET date_bouling = '{date_bouling}' WHERE user_id = {user_id}"
        cursor.execute(query)
        connection.commit()
    connection.close()


def set_date_basketball(user_id, date_basketball):
    connection = connect()
    with connection.cursor() as cursor:
        query = f"UPDATE users SET date_basketball = '{date_basketball}' WHERE user_id = {user_id}"
        cursor.execute(query)
        connection.commit()
    connection.close()


def get_balance(user_id: str):
    connection = connect()
    with connection.cursor() as cursor:
        query = f"SELECT balance FROM users WHERE user_id = {user_id}"
        cursor.execute(query)
    data = cursor.fetchone()
    connection.close()
    return data


def get_date_cube(user_id: str):
    connection = connect()
    with connection.cursor() as cursor:
        query = f"SELECT date_cube FROM users WHERE user_id = {user_id}"
        cursor.execute(query)
    data = cursor.fetchone()
    connection.close()
    return data


def get_date_darts(user_id: str):
    connection = connect()
    with connection.cursor() as cursor:
        query = f"SELECT date_darts FROM users WHERE user_id = {user_id}"
        cursor.execute(query)
    data = cursor.fetchone()
    connection.close()
    return data


def get_date_basketball(user_id: str):
    connection = connect()
    with connection.cursor() as cursor:
        query = f"SELECT date_basketball FROM users WHERE user_id = {user_id}"
        cursor.execute(query)
    data = cursor.fetchone()
    connection.close()
    return data


def get_date_bouling(user_id: str):
    connection = connect()
    with connection.cursor() as cursor:
        query = f"SELECT date_bouling FROM users WHERE user_id = {user_id}"
        cursor.execute(query)
    data = cursor.fetchone()
    connection.close()
    return data


def get_point(user_id: str):
    connection = connect()
    with connection.cursor() as cursor:
        query = f"SELECT COUNT(*) FROM `users_cards` WHERE `id_user_id` = {user_id}"
        cursor.execute(query)
    data = cursor.fetchone()
    print(data)
    connection.close()
    return data


def get_card(id_card: int):
    connection = connect()
    with connection.cursor() as cursor:
        query = f"SELECT * FROM `cards` WHERE `id` = {id_card}"
        cursor.execute(query)
    data = cursor.fetchone()
    connection.close()
    return data


def get_random_card(type_card: int):
    connection = connect()
    with connection.cursor() as cursor:
        query = f"SELECT * FROM cards WHERE type_card = {type_card} ORDER BY RAND() LIMIT 1"
        cursor.execute(query)
    data = cursor.fetchone()
    connection.close()
    print(data)
    return data


def get_user(user_id: str):
    connection = connect()
    with connection.cursor() as cursor:
        query = f"SELECT * FROM `users` WHERE `user_id` = {user_id}"
        cursor.execute(query)
    data = cursor.fetchone()
    connection.close()
    return data


def get_cards_user_distinct(user_id: str):
    connection = connect()
    with connection.cursor() as cursor:
        query = f"SELECT DISTINCT c.url AS url, c.id as id, c.get_point as get_point, c.type_card as type_card FROM users_cards AS uc JOIN cards AS c ON c.id = uc.id_card WHERE uc.id_user_id = {user_id} ORDER BY type_card DESC"
        cursor.execute(query)
    data = cursor.fetchall()
    connection.close()
    return data


def get_cards_user(user_id: str):
    connection = connect()
    with connection.cursor() as cursor:
        query = f"SELECT c.url AS url, c.id as id, c.get_point as get_point, c.type_card as type_card FROM users_cards AS uc JOIN cards AS c ON c.id = uc.id_card WHERE uc.id_user_id = {user_id} ORDER BY type_card DESC"
        cursor.execute(query)
    data = cursor.fetchall()
    connection.close()
    return data


def get_cards_user_tuning(user_id: str):
    connection = connect()
    with connection.cursor() as cursor:
        query = f"""SELECT type_card, COUNT(id_card) as count_card FROM (SELECT id_card, type_card, COUNT(id_card) as count_cards FROM users_cards AS uc
JOIN users AS u ON u.user_id = uc.id_user_id
JOIN cards AS c ON c.id = uc.id_card
WHERE u.user_id = {user_id}
GROUP BY id_card
HAVING count_cards > 1) as data_cars
GROUP BY type_card"""
        cursor.execute(query)
    data = cursor.fetchall()
    connection.close()
    return data


def get_top_10_players():
    connection = connect()
    with connection.cursor() as cursor:
        query = f"""SELECT u.user_id, u.user_name, sum(c.get_point) as sum_point FROM users_cards AS uc
JOIN users AS u ON u.user_id = uc.id_user_id
JOIN cards AS c ON c.id = uc.id_card
GROUP BY u.user_id
ORDER BY sum_point DESC
LIMIT 10"""
        cursor.execute(query)
    data = cursor.fetchall()
    connection.close()
    print(data)
    return data


def get_top_10_players_seasone():
    connection = connect()
    with connection.cursor() as cursor:
        query = f"""SELECT u.user_id, u.user_name, sum(c.get_point) as sum_point FROM users_cards AS uc
JOIN users AS u ON u.user_id = uc.id_user_id
JOIN cards AS c ON c.id = uc.id_card
WHERE MONTH(date_get) = MONTH(NOW()) 
GROUP BY u.user_id
ORDER BY sum_point DESC
LIMIT 10;"""
        cursor.execute(query)
    data = cursor.fetchall()
    connection.close()
    print(data)
    return data
        
    
# def insert_cards(type: int, point: int, path: str):
#     connection = connect()
#     with connection.cursor() as cursor:
#         query = "INSERT INTO `cards` (`type_card`, `get_point`, `url`) VALUES (%s, %s, %s)"
#         cursor.execute(query, (type, point, path))
#         connection.commit()
#     connection.close()