import streamlit as st
from PIL import Image
from openaiApi.image import analyze_image, convert_image_to_binary

def get_image_format(file_name):
    """
    ファイル名から画像の形式を取得する関数。

    Args:
        file_name (str): ファイル名。

    Returns:
        str: 画像の形式 ('PNG', 'JPEG')。
    """
    file_extension = file_name.split('.')[-1].lower()
    if file_extension == 'jpg':
        return 'JPEG'
    elif file_extension == 'jpeg':
        return 'JPEG'
    elif file_extension == 'png':
        return 'PNG'
    else:
        return None

def show_image_openai_file_upload():
    """
    Streamlitアプリケーションで画像ファイルをアップロードし、
    OpenAI APIを使用して画像を解析する関数。
    """
    st.subheader("画像解析サンプル_OPENAI(ファイルアップロード)")

    # ファイルアップロード
    uploaded_file = st.file_uploader("解析する画像をアップロードしてください", type=["png", "jpg", "jpeg"])

    if uploaded_file is not None:
        try:
            # アップロードされた画像をPILで開く
            image = Image.open(uploaded_file)
            st.image(image, caption='アップロードされたER図', use_column_width=True)

            # 画像の形式を取得
            image_format = get_image_format(uploaded_file.name)

            if image_format is None:
                st.error("対応していない画像形式です。PNG, JPG, JPEGのいずれかをアップロードしてください。")
                return

            # 画像を解析して結果を表示
            with st.spinner("解析中..."):
                # 画像をバイナリデータに変換
                binary_image = convert_image_to_binary(image, format=image_format)
                
                # OpenAI APIを使用して画像を解析
                analysis_response = analyze_image(binary_image)
                if analysis_response.choices:
                    # 解析結果を表示
                    result_text = analysis_response.choices[0].message.content
                    st.success("解析完了！")
                    st.write(result_text)
                else:
                    # 解析結果がない場合のエラーメッセージ
                    st.error("解析結果の取得に失敗しました")
        except Exception as e:
            # エラーハンドリング
            st.error(f"エラーが発生しました: {e}")

# 使用例
if __name__ == "__main__":
    show_image_openai_file_upload()
