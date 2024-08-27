import os

# MySQL接続設定を環境変数から取得
db_config = {
    'user': os.getenv('MYSQL_USER'),
    'password': os.getenv('MYSQL_PASSWORD'),
    'host': os.getenv('MYSQL_HOST'),
    'database': os.getenv('MYSQL_DATABASE'),
    'port': os.getenv('MYSQL_PORT'),
    'charset': 'utf8'
}

# OpenAI APIキーを環境変数から取得
openai_api_key = os.getenv('OPENAI_API_KEY')
