from datetime import datetime
from util.db_utils import get_db_cursor
from config import db_config

def read_sql_file(file_path):
    """
    SQLファイルを読み込む関数。

    Args:
        file_path (str): 読み込むSQLファイルのパス。

    Returns:
        str: SQLファイルの内容。
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def get_table_logical_name(table_name):
    """
    テーブルの論理名を取得する関数。

    Args:
        table_name (str): テーブル名。

    Returns:
        str: テーブルの論理名。
    """
    sql_query = read_sql_file('sql/get_table_logical_name.sql')
    sql_query = sql_query.format(database=db_config["database"], table_name=table_name)
    with get_db_cursor() as (cursor, connection):
        cursor.execute(sql_query)
        return cursor.fetchone()[0]

def get_table_columns(table_name):
    """
    テーブルのカラム情報を取得する関数。

    Args:
        table_name (str): テーブル名。

    Returns:
        list: カラム情報のリスト。
    """
    sql_query = read_sql_file('sql/get_table_columns.sql')
    sql_query = sql_query.format(database=db_config["database"], table_name=table_name)
    with get_db_cursor() as (cursor, connection):
        cursor.execute(sql_query)
        return cursor.fetchall()

def insert_log(log_text, log_type, created_by=1):
    """
    ログを挿入する関数。

    Args:
        log_text (str): ログのテキスト。
        log_type (str): ログの種類（例： 'Q' - 質問、 'A' - 回答）。
        created_by (int): 作成者のID（デフォルトは1）。

    """
    sql_query = read_sql_file('sql/insert_log.sql')
    with get_db_cursor() as (cursor, connection):
        cursor.execute(sql_query, (log_text, log_type, datetime.now(), created_by))
        connection.commit()  # コミット操作を確実に行う

def get_logs():
    """
    すべてのログを取得する関数。

    Returns:
        list: ログのリスト。
    """
    sql_query = read_sql_file('sql/get_logs.sql')
    with get_db_cursor() as (cursor, connection):
        cursor.execute(sql_query)
        return cursor.fetchall()

def get_all_table_names():
    """
    すべてのテーブル名を取得する関数。

    Returns:
        list: テーブル名のリスト。
    """
    sql_query = read_sql_file('sql/get_all_table_names.sql')
    sql_query = sql_query.format(database=db_config["database"])
    with get_db_cursor() as (cursor, connection):
        cursor.execute(sql_query)
        return [row[0] for row in cursor.fetchall()]
