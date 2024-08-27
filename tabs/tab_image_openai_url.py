import streamlit as st
import requests
from PIL import Image
from io import BytesIO
from openaiApi.image import analyze_image

def show_image_openai_url():
    """
    Streamlitアプリケーションで画像URLを入力し、
    OpenAI APIを使用して画像を解析する関数。
    """
    st.subheader("画像解析サンプル_OPENAI(URLから取得)")

    # 画像URLの入力
    image_url = st.text_input("解析する画像のURLを入力してください", placeholder="https://example.com/image.png")

    if image_url:
        try:
            # URLから画像を取得
            response = requests.get(image_url)
            if response.status_code == 200:
                # 画像データを取得しPILで開く
                image_data = response.content
                image = Image.open(BytesIO(image_data))
                st.image(image, caption='入力された画像', use_column_width=True)

                # 画像を解析して結果を表示
                with st.spinner("解析中..."):
                    # OpenAI APIを使用して画像を解析
                    analysis_response = analyze_image(image_url)
                    
                    if analysis_response.choices:
                        # 解析結果を表示
                        result_text = analysis_response.choices[0].message.content
                        st.success("解析完了！")
                        st.write(result_text)
                    else:
                        # 解析結果がない場合のエラーメッセージ
                        st.error("解析結果の取得に失敗しました")
            else:
                # 画像取得に失敗した場合のエラーメッセージ
                st.error("画像の取得に失敗しました。URLを確認してください。")
        except Exception as e:
            # エラーハンドリング
            st.error(f"エラーが発生しました: {e}")
