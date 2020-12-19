import streamlit as st
import pandas as pd
import requests
import cv2

# device = st.text_input("input your video/camera device", "0")

cap = cv2.VideoCapture(0)
image_loc = st.empty()

while cap.isOpened():
    _, frame = cap.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    image_loc.image(frame, width=960)
    if cv2.waitKey() & 0xFF == ord("q"):
        break
cap.release()
