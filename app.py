import streamlit as st
import pandas as pd
import requests
import cv2

# sidebar
st.sidebar.markdown(
  "# Paramator"
)
st.sidebar.select_slider("anger", options=list(range(101)))
st.sidebar.select_slider("contempt", options=list(range(101)))
st.sidebar.select_slider("disgust", options=list(range(101)))
st.sidebar.select_slider("fear", options=list(range(101)))
st.sidebar.select_slider("happiness", options=list(range(101)))
st.sidebar.select_slider("neutral", options=list(range(101)))
st.sidebar.select_slider("sadness", options=list(range(101)))
st.sidebar.select_slider("surprise", options=list(range(101)))

cap = cv2.VideoCapture(0)
image_loc = st.empty()

while cap.isOpened():
    _, frame = cap.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    image_loc.image(frame, width=640)
    if cv2.waitKey() & 0xFF == ord("q"):
        break
cap.release()
