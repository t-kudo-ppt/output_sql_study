import streamlit as st
from openaiApi.database import get_all_table_names, get_table_logical_name, get_table_columns
import os

def write_table_info_to_file(table_name, directory='create_table'):
    """
    テーブル情報を指定されたディレクトリにファイルとして書き出す関数。

    Args:
        table_name (str): テーブル名。
        directory (str): ファイルを書き出すディレクトリ名。

    Returns:
        str: 書き込み結果のメッセージ。
    """
    # ディレクトリが存在しない場合は作成
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    # テーブル情報を取得
    table_logical_name = get_table_logical_name(table_name)
    columns = get_table_columns(table_name)
    
    if not columns:
        return f"Table '{table_name}' does not exist."
    
    # ファイルパスの決定
    file_path = os.path.join(directory, f"{table_name}.sql")

    # ファイルに情報を書き込む
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(f"-- Table: {table_name} ({table_logical_name})\n\n")
        file.write(f"CREATE TABLE {table_name} (\n")
        for column in columns:
            physical_name, logical_name, col_type, nullable, col_key = column
            file.write(f"    {physical_name} {col_type} ")
            if nullable == "NO":
                file.write("NOT NULL ")
            if col_key:
                file.write(f"{col_key} ")
            file.write(f"COMMENT '{logical_name}',\n")
        file.write(") ENGINE=InnoDB DEFAULT CHARSET=utf8;\n")
    
    return f"Table information for '{table_name}' has been written to '{file_path}'."

def show_output_latest_info():
    """
    Streamlitアプリケーションで最新のテーブル情報を取得し、ファイルに出力する関数。
    """
    st.subheader('最新のテーブル情報を取得')

    # ボタンを押したときにすべてのテーブル情報をファイルに出力
    if st.button("Output All Table Info"):
        table_names = get_all_table_names()
        results = [write_table_info_to_file(table_name) for table_name in table_names]
        for result in results:
            st.success(result)
