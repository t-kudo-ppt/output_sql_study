import streamlit as st
import openai
from PIL import Image
import io
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from config import openai_api_key

# OpenAI APIキーを設定
openai.api_key = openai_api_key

def analyze_image(image):
    # 画像をバイナリに変換
    img_byte_arr = io.BytesIO()
    image.save(img_byte_arr, format='PNG')
    img_byte_arr = img_byte_arr.getvalue()

    # OpenAI APIを使って画像を分析
    # LLMの初期化
    llm = ChatOpenAI(openai_api_key=openai_api_key, model="gpt-4o-mini", temperature=0)

    # メッセージの作成
    messages = [
        ("system", "以下の画像に基づいてER図を解説します。"),
        ("user", "このER図を解析してください。")
    ]

    # プロンプトの生成
    prompt = ChatPromptTemplate.from_messages(messages)

    # チェーンの構築と実行
    output_parser = StrOutputParser()
    chain = prompt | llm | output_parser
    response = chain.invoke({"input": img_byte_arr})

    # 生成されたテキストを取得
    text = response
    return text

def show_image_sample1():
    st.subheader("ER図解説生成1(langchainを利用して画像をバイナリに変換して送信パターン)")

    # ファイルアップロード
    uploaded_file = st.file_uploader("ER図をアップロードしてください", type=["png", "jpg", "jpeg"])

    if uploaded_file is not None:
        # 画像を表示
        image = Image.open(uploaded_file)
        st.image(image, caption='アップロードされたER図', use_column_width=True)

        # 画像を解析して結果を表示
        with st.spinner("解析中..."):
            result_text = analyze_image(image)
            st.success("解析完了！")
            st.write(result_text)
