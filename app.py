import streamlit as st
from tabs.tab_table_info import show_table_info
from tabs.tab_chat import show_chat
from tabs.tab_logs import show_logs
from tabs.tab_output_latest_info import show_output_latest_info
from tabs.tab_image_openai_url import show_image_openai_url
from tabs.tab_image_openai_file_upload import show_image_openai_file_upload

# Streamlit アプリケーションのタイトルを設定
st.title('SQL生成ツール')

# カスタムCSSの追加
st.markdown("""
    <style>
    .custom-textbox input {
        background-color: #f0f0f0;
        border: 1px solid #ccc;
        border-radius: 4px;
        padding: 10px;
        font-size: 16px;
    }
    .custom-textarea textarea {
        background-color: #f0f0f0;
        border: 1px solid #ccc;
        border-radius: 4px;
        padding: 10px;
        font-size: 16px;
    }
    </style>
    """, unsafe_allow_html=True)

# タブの作成
tab_table_info, tab_generate_sql, tab_log, tab_output_latest_table_info, tab_image_openai, tab_image_openai_file_upload = st.tabs([
    "Table Information", "Generate SQL", "Logs", "Output Latest Table Info", "Open AI Image URL", "Open AI Image File Upload"
])

# 各タブの表示内容
with tab_table_info:
    # テーブル情報を表示
    show_table_info()

with tab_generate_sql:
    # SQL作成ツール
    show_chat()

with tab_log:
    # SQL作成ツールのログを表示
    show_logs()

with tab_output_latest_table_info:
    # DBの最新のテーブル情報を取得
    show_output_latest_info()

with tab_image_openai:
    # 画像の中身を解説ツール(URL)
    show_image_openai_url()

with tab_image_openai_file_upload:
    # 画像の中身を解説ツール(アップロード)
    show_image_openai_file_upload()
