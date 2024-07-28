import mysql.connector
from mysql.connector import Error

def create_connection():
    connection = None
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='root',
            database='telegram_bot_db'
        )
    except Error as e:
        print(f"The error '{e}' occurred, DATABASE CONNECTION FAILED")
    return connection