
import streamlit as st
import cv2
from virtual_mouse import HandMouseController

st.set_page_config(page_title="Virtual Mouse", layout="wide")
st.title("🖱️ AI Virtual Mouse using Hand Gestures")

st.markdown("Control your mouse with just your hand using webcam + AI!")

run_app = st.button("Start Virtual Mouse")

FRAME_WINDOW = st.image([])

if run_app:
    controller = HandMouseController()
    cap = cv2.VideoCapture(0)

    while cap.isOpened():
        success, frame = cap.read()
        if not success:
            st.error("Webcam not detected.")
            break
        frame = controller.process_frame(frame)
        FRAME_WINDOW.image(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

    cap.release()
