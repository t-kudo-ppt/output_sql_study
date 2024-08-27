from openaiApi.common import process_with_openai

# 定数
TABLE_NAMES = ["company_master", "company_user_master"]
SQL_DIRECTORY = "create_table"

def read_sql_file(file_path):
    """
    SQLファイルを読み込む関数。

    Args:
        file_path (str): 読み込むSQLファイルのパス。

    Returns:
        str: ファイルの内容を文字列として返す。
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def load_sql_contents(question):
    """
    テーブル名に基づいてSQLコンテンツを読み込む関数。

    Args:
        question (str): ユーザーからの質問。

    Returns:
        dict: テーブル名をキー、SQLコンテンツを値とする辞書を返す。
    """
    sql_contents = {}

    # 含まれているテーブル名を格納するリスト
    send_table_info = []
    # 各テーブル名がquestionに含まれているかを確認し、含まれていればsend_table_infoに追加
    for table_name in TABLE_NAMES:
        if table_name in question:
            send_table_info.append(table_name)

    for table_name in send_table_info:
        file_path = f'{SQL_DIRECTORY}/{table_name}.sql'
        sql_contents[table_name] = read_sql_file(file_path)
    return sql_contents

def create_messages(sql_contents):
    """
    SQLコンテンツをメッセージ形式に変換する関数。

    Args:
        sql_contents (dict): テーブル名をキー、SQLコンテンツを値とする辞書。

    Returns:
        list: メッセージ形式の辞書のリスト。
    """
    return "\n".join(sql_contents.values())

def generate_sql_updates(question):
    """
    質問に基づいてSQLアップデートを生成する関数。

    Args:
        question (str): ユーザーからの質問。

    Returns:
        str: OpenAI APIからの応答内容。
    """
    # SQL内容の読み込み
    sql_contents = load_sql_contents(question)
    messages = create_messages(sql_contents)

    # 追加メッセージ
    additional_message = """
    ### SQL作成ルール
    # TODO: SQL作成ルールについて記載してください

    ### 回答時のルール
    # TODO: 回答時のルールについて記載してください
    """

    # TODO: additional_messagesに適切な形式でroleを設定してください
    # additional_messages = [
    #   {"role": "      ", "content": additional_message},
    #   {"role": "      ", "content": messages},
    #   {"role": "      ", "content": question}
    # ]

    # OpenAI APIを使用して応答を生成
    response = process_with_openai("gpt-4o-mini", additional_messages)
    # TODO OpenAI APIのresponseから回答のテキスト部分だけ取得してください
    # return 
