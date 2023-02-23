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


def add_user(user_id):
    connection = connect()
    with connection.cursor() as cursor:
        query = "INSERT INTO `users` (`user_id`) VALUES(%s)"
        cursor.execute(query, user_id)
        connection.commit()
    connection.close()


def add_card(id_card: int, user_id: str):
    connection = connect()
    with connection.cursor() as cursor:
        query = "INSERT INTO `users_cards` (`id_card`, `id_user_id`) VALUES(%s, %s)"
        cursor.execute(query, (id_card, user_id))
        connection.commit()
    connection.close()


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


def get_user(user_id: str):
    connection = connect()
    with connection.cursor() as cursor:
        query = f"SELECT * FROM `users` WHERE `user_id` = {user_id}"
        cursor.execute(query)
    data = cursor.fetchone()
    connection.close()
    print(data)
    return data


def get_cards_user(user_id: str):
    connection = connect()
    with connection.cursor() as cursor:
        query = f"SELECT c.url AS url, c.id as id, c.get_point as get_point, c.type_card as type_card FROM users_cards AS uc JOIN cards AS c ON c.id = uc.id_card WHERE uc.id_user_id = {user_id}"
        cursor.execute(query)
    data = cursor.fetchall()
    connection.close()
    return data
        
    
# def insert_cards(type: int, point: int, path: str):
#     connection = connect()
#     with connection.cursor() as cursor:
#         query = "INSERT INTO `cards` (`type_card`, `get_point`, `url`) VALUES (%s, %s, %s)"
#         cursor.execute(query, (type, point, path))
#         connection.commit()
#     connection.close()