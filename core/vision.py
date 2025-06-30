import cv2
import mediapipe as mp
import numpy as np
import face_recognition
import os

# Load saved face encoding
face_path = os.path.join("assets", "faces", "zaid_face.npy")
known_encoding = np.load(face_path)

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1)
mp_draw = mp.solutions.drawing_utils

video = cv2.VideoCapture(0)
print("🧠 Show your face + ✌️ to unlock assistant")

def detect_peace_gesture(hand_landmarks):
    finger_tips = [8, 12]  # Index and middle
    finger_folded = 0

    for tip in finger_tips:
        if hand_landmarks.landmark[tip].y > hand_landmarks.landmark[tip - 2].y:
            finger_folded += 1

    return finger_folded == 0  # Both fingers up

while True:
    ret, frame = video.read()
    if not ret:
        break

    flipped = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(flipped, cv2.COLOR_BGR2RGB)

    # Face detection
    face_locations = face_recognition.face_locations(rgb)
    encodings = face_recognition.face_encodings(rgb, face_locations)
    face_match = False

    for encoding in encodings:
        match = face_recognition.compare_faces([known_encoding], encoding)[0]
        face_match = match
        break

    # Hand gesture detection
    result = hands.process(rgb)
    gesture_match = False

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp_draw.draw_landmarks(flipped, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            gesture_match = detect_peace_gesture(hand_landmarks)

    # Check both conditions
    if face_match and gesture_match:
        print("✅ Access Granted (Face + Peace)")
        video.release()
        cv2.destroyAllWindows()
        break

    cv2.imshow("Login: Face + Gesture", flipped)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

video.release()
cv2.destroyAllWindows()
