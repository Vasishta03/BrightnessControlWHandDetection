import cv2
import mediapipe as mp
import numpy as np
from math import hypot
import screen_brightness_control as sbc

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hand_detector = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=2,
    model_complexity=1,
    min_detection_confidence=0.75,
    min_tracking_confidence=0.75
)
mp_draw = mp.solutions.drawing_utils

# Start video capture
video = cv2.VideoCapture(0)

while True:
    ret, img = video.read()
    if not ret:
        break

    img = cv2.flip(img, 1)
    rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hand_detector.process(rgb_img)

    points = []
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            h, w, _ = img.shape
            for idx, lm in enumerate(hand_landmarks.landmark):
                px, py = int(lm.x * w), int(lm.y * h)
                points.append((idx, px, py))
            mp_draw.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    if len(points) >= 9:
        # Thumb tip and index finger tip
        thumb_tip = points[4][1], points[4][2]
        index_tip = points[8][1], points[8][2]

        # Draw markers
        cv2.circle(img, thumb_tip, 8, (255, 0, 255), -1)
        cv2.circle(img, index_tip, 8, (255, 0, 255), -1)
        cv2.line(img, thumb_tip, index_tip, (255, 0, 255), 2)

        # Calc dist
        dist = hypot(index_tip[0] - thumb_tip[0], index_tip[1] - thumb_tip[1])
        brightness = np.interp(dist, [15, 220], [0, 100])
        sbc.set_brightness(int(brightness))

    cv2.imshow("Brightness Control", img)
    if cv2.waitKey(1) & 0xFF == ord('e'):
        break

video.release()
cv2.destroyAllWindows()