import streamlit as st
import pandas as pd
import requests
import cv2
import numpy as np
import datetime
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, __version__, PublicAccess
import os, uuid, sys


# local
from seacret import KEY
# from ditectemotion import ditectemotion
# from upload import upload
from uptoblob import uptoblob

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

weight_list = {
    "anger": anger_weight,
    "contempt": contempt_weight,
    "disgust": disgust_weight,
    "fear": fear_weight,
    "happiness": happiness_weight,
    "neutral": neutral_weight,
    "sadness": sadness_weight,
    "surprise": surprise_weight
    }


# main
col1, col2 = st.beta_columns(2)
isAnalytics = False

with col1:
    if st.button('採点開始'):
        if not isAnalytics:
            connect_str = os.getenv('AZURE_STORAGE_CONNECTION_STRING')
            # Create the BlobServiceClient object which will be used to create a container client
            blob_service_client = BlobServiceClient.from_connection_string(connect_str)

            # Create a unique name for the container
            container_name = "faceimages"

            # Create the container
            container_client = blob_service_client.create_container(container_name, public_access="blob")

        isAnalytics = True

with col2:
    if st.button('採点終了'):
        isAnalytics = False

cap = cv2.VideoCapture(0)
image_loc = st.empty()

file_cnt = 0
while cap.isOpened():
    _, frame = cap.read()
    view_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    view_frame = cv2.flip(view_frame, 1)
    image_loc.image(view_frame, width=640)
    if isAnalytics:
        img_path = f'data/{file_cnt}.jpg'
        frame = cv2.flip(view_frame, 1)
        cv2.imwrite(img_path, frame)
        uptoblob(container_name, img_path, file_cnt)

        file_cnt += 1
    else:
        file_cnt = 0
    if cv2.waitKey() & 0xFF == ord("q"):
        break
cap.release()

# グラフ
label_index = ['anger', 'contempt', 'disgust', 'fear', 'happiness', 'neutral', 'sadness', 'surprise']
data = {'additional_properties': {}, 'anger': 0.0, 'contempt': 0.0, 'disgust': 0.4, 'fear': 0.0, 'happiness': 1.0, 'neutral': 0.0, 'sadness': 0.0, 'surprise': 0.0}
del data["additional_properties"]

df = pd.DataFrame(columns=label_index)

chart = st.empty()

for i in range(100):
    calc_data = list(map(lambda l: data[l]*weight_list[l], label_index))
    calc_sum = sum(calc_data)
    addRow = pd.DataFrame(list(map(lambda c: c / calc_sum if calc_sum else 0, calc_data)), index=data.keys()).T
    df = df.append(addRow, ignore_index=True)

    chart.line_chart(df)
