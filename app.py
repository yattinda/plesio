import streamlit as st
import pandas as pd
import requests
import cv2

# sidebar
st.sidebar.markdown(
  "# Mode"
)
analytics_type = st.sidebar.selectbox("", ["normal", "easy", "denger"])
# anger: 憤怒, contempt: 軽蔑, disgust: 嫌気, fear: 恐怖, happiness: 幸福, neutral: 自然, sadness: 悲哀, surprise: 驚き
mode_list = {
  "normal": {"anger": 50,"contempt": 50,"disgust": 50,"fear": 50,"happiness": 50,"neutral": 50,"sadness": 50,"surprise": 50},
  "easy":   {"anger": 10,"contempt": 10,"disgust": 10,"fear": 10,"happiness": 90,"neutral": 50,"sadness": 10,"surprise": 50},
  "denger": {"anger": 90,"contempt": 90,"disgust": 90,"fear": 90,"happiness": 10,"neutral": 50,"sadness": 90,"surprise": 50}
}
st.sidebar.markdown(
  "# Paramator"
)
anger_weight = st.sidebar.slider("憤怒", 0, 100, mode_list[analytics_type]["anger"])
contempt_weight = st.sidebar.slider("軽蔑", 0, 100, mode_list[analytics_type]["contempt"])
disgust_weight = st.sidebar.slider("嫌気", 0, 100, mode_list[analytics_type]["disgust"])
fear_weight = st.sidebar.slider("恐怖", 0, 100, mode_list[analytics_type]["fear"])
happiness_weight = st.sidebar.slider("幸福", 0, 100, mode_list[analytics_type]["happiness"])
neutral_weight = st.sidebar.slider("自然", 0, 100, mode_list[analytics_type]["neutral"])
sadness_weight = st.sidebar.slider("悲哀", 0, 100, mode_list[analytics_type]["sadness"])
surprise_weight = st.sidebar.slider("驚愕", 0, 100, mode_list[analytics_type]["surprise"])


# main

# cap = cv2.VideoCapture(0)
# image_loc = st.empty()

# while cap.isOpened():
#     _, frame = cap.read()
#     frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#     image_loc.image(frame, width=640)
#     if cv2.waitKey() & 0xFF == ord("q"):
#         break
# cap.release()

# data = {'additional_properties': {}, 'anger': 0.0, 'contempt': 0.0, 'disgust': 0.0, 'fear': 0.0, 'happiness': 1.0, 'neutral': 0.0, 'sadness': 0.0, 'surprise': 0.0}
# del data["additional_properties"]

# df = pd.DataFrame(data)

# for _ in range(100):
#     df.append(data)

# st.line_chart(df)

col1, col2 = st.beta_columns(2)
isAnalytics = False

with col1:
  if st.button('採点開始'):
      isAnalytics = True
with col2:
  if st.button('採点終了'):
      isAnalytics = False
