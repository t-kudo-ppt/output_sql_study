import streamlit as st
import openai
from PIL import Image
import requests
from io import BytesIO
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from config import openai_api_key

# OpenAI APIキーを設定
openai.api_key = openai_api_key

def analyze_image_from_url(image_url):
    # 画像を取得
    response = requests.get(image_url)
    image = Image.open(BytesIO(response.content))

    # LLMの初期化
    llm = ChatOpenAI(openai_api_key=openai_api_key, model="gpt-4o-mini", temperature=0)

    # メッセージの作成
    messages = [
        ("system", "以下の画像に基づいてER図を解説します。"),
        ("user", f"このER図を解析してください。URL: {image_url}")
    ]

    # プロンプトの生成
    prompt = ChatPromptTemplate.from_messages(messages)

    # チェーンの構築と実行
    output_parser = StrOutputParser()
    chain = prompt | llm | output_parser
    response = chain.invoke({"input": response.content})

    # 生成されたテキストを取得
    text = response
    return text

def show_image2():
    st.subheader("ER図解説生成2(langchainを利用してWeb上のURLを解析するパターン)")

    # 画像URLの入力
    image_url = st.text_input("ER図のURLを入力してください")

    if image_url:
        # 画像を表示
        response = requests.get(image_url)
        image = Image.open(BytesIO(response.content))
        st.image(image, caption='アップロードされたER図', use_column_width=True)

        # 画像を解析して結果を表示
        with st.spinner("解析中..."):
            result_text = analyze_image_from_url(image_url)
            st.success("解析完了！")
            st.write(result_text)

