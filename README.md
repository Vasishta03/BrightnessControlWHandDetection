# 🔆 Brightness Control with Hand Detection

A real-time hand gesture-based screen brightness control tool using **MediaPipe Hands** and **OpenCV**. This project uses your webcam to track your hand, specifically the **distance between your thumb and index finger**, to dynamically adjust your system's screen brightness.

---

## 🧠 Features

- ✋ Real-time hand tracking using **MediaPipe**
- 📷 Live webcam input via **OpenCV**
- 📉 Dynamically adjusts brightness based on **finger distance**
- 🖥️ Works with system display brightness
- 🔄 Smooth and intuitive interaction
- ⌨️ Press **'e'** to exit the tool

---

## 🛠️ How It Works

1. The webcam detects your hand using **MediaPipe Hands**.
2. It calculates the distance between your **thumb tip** and **index finger tip**.
3. The screen brightness is adjusted proportionally based on this distance.
   - Closer fingers = lower brightness
   - Further apart = higher brightness
