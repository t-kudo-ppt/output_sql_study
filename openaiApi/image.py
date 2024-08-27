import base64
import io
from openaiApi.common import process_with_openai
from PIL import Image

def convert_image_to_binary(image, format):
    """
    画像をバイナリデータURIに変換する関数。

    Args:
        image (PIL.Image.Image): 変換する画像。
        format (str): 画像のフォーマット ('PNG', 'JPEG', 'JPG')。

    Returns:
        str: 画像のバイナリデータURI。
    """
    
    # 画像データを格納するBytesIOバッファを作成
    img_byte_arr = io.BytesIO()
    
    # 画像を指定された形式でバッファに保存
    image.save(img_byte_arr, format=format)
    
    # バッファからバイナリデータを取得
    img_byte_arr = img_byte_arr.getvalue()
    
    # バイナリデータをbase64エンコード
    encoded_image = base64.b64encode(img_byte_arr).decode('utf-8')
    
    # データURI文字列を作成
    data_uri = f"data:image/{format.lower()};base64,{encoded_image}"
    
    return data_uri

def analyze_image(image):
    """
    OpenAI APIを使用して画像を解析する関数。

    Args:
        image (str): 解析する画像のデータURI。

    Returns:
        dict: OpenAI APIからのレスポンス。
    """
    # OpenAI APIに送信するメッセージを定義
    # TODO: messageに画像を送れるように適切な形式で設定してください
    messages = [""]
    
    # OpenAI APIにメッセージを送信し、レスポンスを取得
    response = process_with_openai("gpt-4o-mini", messages)
    
    return response

# 使用例
if __name__ == "__main__":
    # 画像を開く
    image_path = "path_to_your_image.jpg"
    image = Image.open(image_path)

    # 画像フォーマットを推測
    image_format = image_path.split('.')[-1]

    # バイナリデータURIに変換
    binary_image = convert_image_to_binary(image, format=image_format)

    # 画像解析
    response = analyze_image(binary_image)
    print(response)
