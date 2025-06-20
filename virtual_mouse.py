
import cv2
import mediapipe as mp
import pyautogui
import numpy as np
import math

class HandMouseController:
    def __init__(self):
        self.hands = mp.solutions.hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)
        self.mp_draw = mp.solutions.drawing_utils
        self.screen_w, self.screen_h = pyautogui.size()

    def process_frame(self, frame):
        frame = cv2.flip(frame, 1)
        h, w, _ = frame.shape
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = self.hands.process(rgb)

        if result.multi_hand_landmarks:
            for hand in result.multi_hand_landmarks:
                lm_list = []
                for id, lm in enumerate(hand.landmark):
                    lm_list.append((int(lm.x * w), int(lm.y * h)))

                if len(lm_list) >= 9:
                    x1, y1 = lm_list[8]  # Index finger tip
                    x2, y2 = lm_list[4]  # Thumb tip

                    # Move mouse
                    mouse_x = np.interp(x1, (0, w), (0, self.screen_w))
                    mouse_y = np.interp(y1, (0, h), (0, self.screen_h))
                    pyautogui.moveTo(mouse_x, mouse_y)

                    # Click if distance between index and thumb is small
                    dist = math.hypot(x2 - x1, y2 - y1)
                    if dist < 40:
                        pyautogui.click()

                self.mp_draw.draw_landmarks(frame, hand, mp.solutions.hands.HAND_CONNECTIONS)
        return frame
