import streamlit as st
from openaiApi.database import get_logs

def show_logs():
    """
    履歴を表示する関数。
    データベースからログを取得し、Streamlitを使用して表示する。
    """
    st.subheader("履歴")

    # データベースからログを取得
    logs = get_logs()

    # 各ログを表示
    for log in logs:
        log_id, log_text, log_type = log
        log_title = f"∴∵∴∵∴∵∴∵∴∵ 履歴{log_id:05d} {'質問' if log_type == 'Q' else '回答'} ∴∵∴∵∴∵∴∵∴∵"
        
        # ログのタイトルを表示
        st.markdown(log_title)
        
        # ログの内容を表示
        st.markdown(log_text)
        
        # 区切り線を表示
        st.markdown("---")
