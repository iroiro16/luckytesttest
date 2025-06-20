import streamlit as st
import random

st.title("🔮 今日のラッキー占い")
st.write("「占う！」ボタンを押して、今日のラッキーをチェックしてみよう🎲")

if st.button("占う！"):
    color = random.choice(["赤", "青", "黄", "緑", "白"])
    item = random.choice(["みょうが", "小石", "メモ帳", "ペットボトル", "蓋"])
    number = random.choice(["58", "2", "99", "72", "63"])

    st.write(f"🟥 **ラッキーカラー：{color}**")
    st.write(f"🎒 **ラッキーアイテム：{item}**")
    st.write(f"🔢 **ラッキーナンバー：{number}**")
