import streamlit as st
import requests
from PIL import Image
from io import BytesIO
from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

# OpenAI APIキーの設定
from config import openai_api_key

# LLMChainとPromptTemplateの設定
llm = OpenAI(api_key=openai_api_key, model="gpt-4o-mini")

prompt_template = PromptTemplate(
    input_variables=["image_url"],
    template="""
    この画像について説明お願いします。
    画像URL: {image_url}
    """
)

chain = LLMChain(llm=llm, prompt=prompt_template)

def analyze_image(image_url):
    response = chain.run(image_url=image_url)
    return response

def show_image_llmchain():
    st.subheader("画像解析サンプル_LLMChain")

    # 画像URL入力
    image_url = st.text_input("解析する画像のURLを入力してください",key="image_url_input", placeholder="https://example.com/image.png")

    if image_url:
        try:
            # 画像を取得
            response = requests.get(image_url)
            if response.status_code == 200:
                image_data = response.content
                image = Image.open(BytesIO(image_data))
                st.image(image, caption='入力された画像', use_column_width=True)

                # 画像を解析して結果を表示
                with st.spinner("解析中..."):
                    analysis_response = analyze_image(image_url)
                    if analysis_response:
                        st.success("解析完了！")
                        st.write(analysis_response)
                    else:
                        st.error("解析結果の取得に失敗しました")
            else:
                st.error(f"画像を取得できませんでした: ステータスコード {response.status_code}")
        except Exception as e:
            st.error(f"エラーが発生しました: {e}")
