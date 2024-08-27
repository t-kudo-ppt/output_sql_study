import streamlit as st
import pandas as pd
import os
from openaiApi.database import get_table_logical_name, get_table_columns

def get_table_names_from_directory(directory):
    """
    指定されたディレクトリ内のファイル名（拡張子なし）を取得する関数。

    Args:
        directory (str): ディレクトリ名。

    Returns:
        list: ファイル名のリスト（拡張子なし）。
    """
    return [os.path.splitext(f)[0] for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

def show_table_info():
    """
    Streamlitアプリケーションでテーブル情報を表示する関数。
    """
    # `create_table` ディレクトリ内のファイル名（拡張子なし）を取得
    table_names = get_table_names_from_directory('create_table')
    
    # テーブル名の選択ボックスを表示
    table_name = st.selectbox(
        "テーブル名を記載してください:",
        options=table_names,
        index=table_names.index("company_master") if "company_master" in table_names else 0,
        key="table_name_input",
        help="調査したいテーブルの名前を選択してください。"
    )
    
    # テキストボックスにクラスを追加してスタイルを適用
    st.markdown("""
        <style>
        [data-testid="stSelectbox"] select {
            background-color: #f0f0f0;
            border: 1px solid #ccc;
            border-radius: 4px;
            padding: 10px;
            font-size: 16px;
        }
        </style>
        """, unsafe_allow_html=True)

    if table_name:
        try:
            # テーブルの論理名とカラム情報を取得
            table_logical_name = get_table_logical_name(table_name)
            columns = get_table_columns(table_name)

            if columns:
                # テーブル情報を表示
                st.subheader(f"{table_name} ({table_logical_name})")
                df = pd.DataFrame(columns, columns=["物理名", "論理名", "型", "NULL許容", "主キー"])
                st.dataframe(df)
            else:
                st.error(f"Table '{table_name}' does not exist.")
        except Exception as e:
            # エラーハンドリング
            st.error(f"エラーが発生しました: {e}")
