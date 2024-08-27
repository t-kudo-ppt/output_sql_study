import streamlit as st
import requests
from PIL import Image
from io import BytesIO
import json
import base64
from config import openai_api_key


def analyze_image(image_url):
    # 画像を取得
    response = requests.get(image_url)
    image_data = response.content

    # 画像データをBase64エンコード
    encoded_image = base64.b64encode(image_data).decode('utf-8')
    data_uri = f"data:image/jpeg;base64,{encoded_image}"

    system_prompt = "このシステムは画像の内容を分析して、その説明を生成します。分析結果を日本語で回答します。"
    user_prompt = "画像の中には何が映っていますか？"

    # OpenAI APIエンドポイント
    url = "https://api.openai.com/v1/chat/completions"

    # ヘッダー情報
    headers = {
        "Authorization": f"Bearer {openai_api_key}",
        "Content-Type": "application/json"
    }

    # データを送信
    data = {
        "model": "gpt-4o-mini",
        "messages": [
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": json.dumps([
                    {"type": "text", "text": user_prompt},
                    {"type": "image_url", "image_url": {"url": data_uri}}
                ])
            }
        ],
        "max_tokens": 2000
    }

    # POSTリクエストを送信
    response = requests.post(url, headers=headers, data=json.dumps(data))

    # 結果を表示
    if response.status_code == 200:
        result = response.json()
        return result['choices'][0]['message']['content']
    else:
        return f"エラーが発生しました: {response.status_code}, {response.text}"

def show_image3():
    st.subheader("ER図解説生成")

    # 画像URL入力
    image_url = st.text_input("ER図の画像URLを入力してください", placeholder="https://example.com/er_diagram.png")

    if image_url:
        try:
            # 画像を表示
            response = requests.get(image_url)
            image = Image.open(BytesIO(response.content))
            st.image(image, caption='入力されたER図の画像', use_column_width=True)

            # 画像を解析して結果を表示
            with st.spinner("解析中..."):
                result_text = analyze_image(image_url)
                st.success("解析完了！")
                st.write(result_text)
        except Exception as e:
            st.error(f"エラーが発生しました: {e}")