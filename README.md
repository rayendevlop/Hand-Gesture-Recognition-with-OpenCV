# Hand-Gesture-Recognition-with-OpenCV
A real-time hand gesture detection system using OpenCV, HSV skin detection, convexity defects, and contour analysis.
This app detects gestures such as:
✊ Fist
👍 Thumb Up
👌 OK
✌️ Peace
🖐 Open Hand
🚀 Features
✔ Real-time hand detection
✔ Convexity defects–based finger counting
✔ Angle-based gesture classification
✔ HSV skin detection
✔ Gesture name overlay
✔ Smooth performance (20–60 FPS)
🧠 How It Works
Extract ROI inside a fixed 400×400 box
Convert to HSV + apply skin mask
Find largest contour (the hand)
Compute convex hull & convexity defects
Count valid defects → number of fingers
Apply logic rules to identify gesture
🖥️ Installation
1. Clone repo
git clone https://github.com/rayendevlop/gesture-recognition
cd gesture-recognition
2. Install dependencies
pip install opencv-python numpy
▶️ Run the Program
python3 gesture.py
Press Q to quit.
📸 Supported Gestures
Gesture	Meaning
✊	Fist
👍	Thumb Up
👌	OK
✌️	Peace
🖐	Open Hand
📂 File Structure
gesture-recognition/
│── gesture.py
│── README.md
🧑‍💻 Author
Rayen Gharbi
Computer Vision Developer
📍 Tunisia
