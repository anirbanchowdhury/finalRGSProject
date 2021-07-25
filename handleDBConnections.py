import mysql.connector

from config import *
from mysql.connector import connect, Error


def insertRow(id, lang_pref):
    try:
        with connect(
                host=DB_HOST,
                database=DB_DATABASE,
                port=DB_PORT,
                user=DB_USERNAME,
                password=DB_PASSWORD
        ) as connection:
            print(connection)
            try:
                mySql_insert_query = """INSERT INTO user_info (Id, lang_preference) 
                                       VALUES 
                                       (%s,%s) """

                cursor = connection.cursor()
                values = (id, lang_pref)
                cursor.execute(mySql_insert_query, values)
                connection.commit()
                print(cursor.rowcount, "Record inserted successfully into User table")
                cursor.close()

            except mysql.connector.Error as error:
                print("Failed to insert record into User table {}".format(error))
    except Error as e:
        print(e)


def readRow(id):
    try:
        with connect(
                host=DB_HOST,
                database=DB_DATABASE,
                port=DB_PORT,
                user=DB_USERNAME,
                password=DB_PASSWORD
        ) as connection:
            print(connection)
            try:
                with connection.cursor() as cursor:
                    cursor.execute("SELECT lang_preference FROM user_info where id = %s", [id])
                    result = cursor.fetchall()
                    for row in result:
                        return (row[0])
            except mysql.connector.Error as error:
                print("Failed to select record from User table {}".format(error))
    except Error as e:
        print(e)


# insertRow(3,4)
print(readRow(3))
