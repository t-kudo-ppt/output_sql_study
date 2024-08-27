import mysql.connector
from mysql.connector import Error
from config import db_config
from contextlib import contextmanager

@contextmanager
def get_db_cursor():
    """
    データベースへの接続とカーソルを取得するコンテキストマネージャ。

    Yields:
        cursor (mysql.connector.cursor.MySQLCursor): データベースカーソル。
        connection (mysql.connector.connection.MySQLConnection): データベース接続。
    """
    connection = None
    cursor = None
    try:
        # データベースへの接続を確立
        connection = mysql.connector.connect(**db_config)
        if connection.is_connected():
            # 接続が成功した場合、カーソルを作成
            cursor = connection.cursor()
            yield cursor, connection
    except Error as e:
        # エラーが発生した場合はエラーメッセージを出力
        print(f"Error: {e}")
    finally:
        # カーソルを閉じる
        if cursor is not None:
            cursor.close()
        # 接続を閉じる
        if connection is not None and connection.is_connected():
            connection.close()
