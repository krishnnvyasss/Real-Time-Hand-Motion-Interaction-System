# 🎮 Gesture Bubble Game

An interactive computer vision game built with Python where you pop floating fruits using your hand gestures via webcam.

---

## 🚀 Features

- Real-time hand tracking using MediaPipe  
- Pop fruits using your index finger  
- Lives system with game-over condition  
- Score tracking  
- Smooth gameplay with OpenCV  

---

## 🛠️ Tech Stack

- Python 3.x  
- OpenCV  
- MediaPipe  
- NumPy  

---

## 📦 Installation

### 1. Clone the Repository

git clone https://github.com/your-username/gesture-bubble-game.git  
cd gesture-bubble-game  

### 2. Create Virtual Environment (Recommended)

python -m venv venv  

Activate it:

**Windows**  
venv\Scripts\activate  

**macOS/Linux**  
source venv/bin/activate  

### 3. Install Dependencies

pip install opencv-python mediapipe numpy  

---

## ▶️ Run the Project

python main.py  

Make sure your webcam is connected and accessible.

---

## 🎮 How to Play

- Move your index finger in front of the camera  
- A yellow fruit will appear and move upward  
- Touch the fruit with your fingertip to pop it  
- Each hit gives +100 points  
- Missing a fruit costs 1 life  
- Game ends when lives reach 0  

---

## ⌨️ Controls

- Press `Q` to quit the game  

---

## 📂 Project Structure

gesture-bubble-game/  
│  
├── main.py  
└── README.md  

---

## ⚙️ How It Works

- Uses MediaPipe Hands for hand tracking  
- Detects index finger tip (landmark 8)  
- Calculates distance between finger and fruit  
- Collision increases score  
- Fruit respawns after hit or miss  

---

## 🧩 Future Improvements

- Add sound effects  
- Multiple fruits  
- Difficulty levels  
- Save high scores  
- Better UI/graphics  

---

## 🐛 Troubleshooting

**Camera not opening?**  
Ensure no other app is using the webcam  

**Module not found?**  
pip install opencv-python mediapipe numpy  

**Low FPS?**  
Lower camera resolution  
Close background apps  

---

## 📜 License

This project is licensed under the MIT License.
