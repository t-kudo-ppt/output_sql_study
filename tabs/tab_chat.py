import streamlit as st
from openaiApi.database import insert_log
from openaiApi.create_sql import generate_sql_updates

def show_chat():
    """
    Streamlitアプリケーションのチャットインターフェースを表示する関数。
    ユーザーからのSQL生成リクエストを受け取り、OpenAI APIを使用してSQLを生成し、結果を表示する。
    """
    st.subheader('SQL生成(OpenAI)')

    # フォームの作成
    with st.form(key='my_form'):
        user_input = st.text_area(
            "生成したいSQLについて記載してください",
            key="user_input",
            help="ここにメッセージを入力してください",
            placeholder="company_masterとcompany_user_masterを結合して、企業名、ユーザーの名前、ユーザーのメールアドレスを取得するSQLを作成してください。",
            height=200
        )

        # テキストエリアにクラスを追加してスタイルを適用
        st.markdown("""
            <style>
            [data-testid="stTextArea"] textarea {
                background-color: #f0f0f0;
                border: 1px solid #ccc;
                border-radius: 4px;
                padding: 10px;
                font-size: 16px;
            }
            </style>
            """, unsafe_allow_html=True)

        submit_button = st.form_submit_button(label='Submit (Ctrl+Enter)')

    # フォームが送信された場合の処理
    if submit_button and user_input:
        # 質問ログを挿入
        insert_log(user_input, 'Q')

        with st.spinner('回答生成中...'):
            # OpenAI APIを使用してSQLを生成
            response = generate_sql_updates(user_input)

        # 生成されたSQLを表示
        st.markdown("**回答:**")
        st.markdown(f"{response}")

        # 回答ログを挿入
        insert_log(response, 'A')
