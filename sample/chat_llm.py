from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from config import openai_api_key

# 定数
TABLE_NAMES = ["company_master", "company_user_master"]
SQL_DIRECTORY = "create_table"

def read_sql_file(file_path):
    """SQLファイルを読み込む"""
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def load_sql_contents(table_names):
    """テーブル名に基づいてSQLコンテンツを読み込む"""
    sql_contents = {}
    for table_name in table_names:
        file_path = f'{SQL_DIRECTORY}/{table_name}.sql'
        sql_contents[table_name] = read_sql_file(file_path)
    return sql_contents

def create_messages(sql_contents):
    """SQLコンテンツをメッセージ形式に変換する"""
    return [("system", sql) for sql in sql_contents.values()]

def generate_sql_updates(question):
    """質問に基づいてSQLアップデートを生成する"""
    # LLMの初期化
    llm = ChatOpenAI(openai_api_key=openai_api_key, model="gpt-4o-mini", temperature=0)

    # SQL内容の読み込み
    sql_contents = load_sql_contents(TABLE_NAMES)
    messages = create_messages(sql_contents)

    # 追加メッセージ
    additional_messages = [
        """結合時にはinner joinかleft joinかをわかりやすく記載してください
        削除フラグは指定がない場合は必ずdelete_flag = '0'を指定してください
        ・SELECT文の場合はSELECT文のみ返してください
        ・INSERT文の場合はINSERT文のみ返してください
        ・UPDATE文、DELETE文を記載するときは下記のように記載してください
        1.SQL実行に更新(削除)対象を確認するSQL
        2.実行する更新(削除)SQL
        3.実行後に更新(削除)を確認するSQL
        回答形式としては下記のようにお願いします
        実行前確認用SQL
        更新(削除)SQL
        実行後確認用SQL""",
    ]
    additional_messages = [("system", msg) for msg in additional_messages]
    additional_messages.append(("user", "{input}"))

    # メッセージの結合とプロンプトの生成
    complete_messages = messages + additional_messages
    prompt = ChatPromptTemplate.from_messages(complete_messages)

    # チェーンの構築と実行
    output_parser = StrOutputParser()
    chain = prompt | llm | output_parser
    response = chain.invoke({"input": question})
    return response

def generate_response(user_input):
    """ユーザー入力に基づいて応答を生成する"""
    # LLMの初期化
    llm = ChatOpenAI(openai_api_key=openai_api_key, model="gpt-4o-mini", temperature=0)

    # プロンプトテンプレートの作成
    prompt_template = ChatPromptTemplate.from_template("補足文言があればここに追加されます\nUser: {input}\nAI:")

    # チェーンの構築と実行
    output_parser = StrOutputParser()
    chain = prompt_template | llm | output_parser
    response = chain.invoke({"input": user_input})
    return response