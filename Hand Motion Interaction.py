import cv2
import time
import random
import mediapipe as mp
import math
import numpy as np

# ---------------- Mediapipe Setup ----------------
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=2,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.5
)

# ---------------- Game Variables ----------------
def reset_game():
    global fruit, score, lives, game_over
    fruit = None
    score = 0
    lives = 10
    game_over = False

reset_game()

# ---------------- Camera ----------------
cap = cv2.VideoCapture(0)

# ---------------- Utility ----------------
def distance(p1, p2):
    return int(math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2))

def spawn_fruit():
    return {
        "pos": [random.randint(50, 590), 440],
        "speed": random.randint(4, 7),
        "color": (0, 255, 255)   # YELLOW fruit (BGR)
    }

# Spawn first fruit
fruit = spawn_fruit()

# ---------------- Main Loop ----------------
while cap.isOpened():
    success, img = cap.read()
    if not success:
        continue

    img = cv2.flip(img, 1)
    h, w, _ = img.shape

    # Hand detection
    rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb)

    index_tip = None

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:

            # WHITE hand landmarks & connections
            mp_drawing.draw_landmarks(
                img,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS,
                mp_drawing.DrawingSpec(color=(255,255,255), thickness=2, circle_radius=2),
                mp_drawing.DrawingSpec(color=(255,255,255), thickness=2)
            )

            index_tip = (
                int(hand_landmarks.landmark[8].x * w),
                int(hand_landmarks.landmark[8].y * h)
            )

            # 🔴 RED fingertip (busting point)
            cv2.circle(img, index_tip, 12, (0, 0, 255), -1)

    # ---------------- Fruit Logic ----------------
    if fruit and not game_over:
        fruit["pos"][1] -= fruit["speed"]

        # Draw YELLOW fruit
        cv2.circle(img, tuple(fruit["pos"]), 30, fruit["color"], -1)

        # Missed fruit
        if fruit["pos"][1] < 0:
            lives -= 1
            fruit = spawn_fruit()

        # Touch detection
        if index_tip and distance(index_tip, fruit["pos"]) < 30:
            score += 100
            fruit = spawn_fruit()

    # ---------------- Game Over ----------------
    if lives <= 0:
        game_over = True
        cv2.putText(img, "GAME OVER", (200, 300),
                    cv2.FONT_HERSHEY_SIMPLEX, 2, (0,0,255), 4)

    # ---------------- UI ----------------
    cv2.putText(img, f"Score: {score}", (20,40),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)
    cv2.putText(img, f"Lives: {lives}", (20,80),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)

    cv2.imshow("Gesture Bubble Game", img)

    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
