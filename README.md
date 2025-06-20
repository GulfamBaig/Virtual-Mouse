
# 🖱️ AI Virtual Mouse using Hand Gestures (OpenCV + MediaPipe + Streamlit)

Control your computer's mouse cursor **without touching it!**  
This AI-powered **Virtual Mouse** uses your **hand gestures via webcam** to move the cursor and perform clicks — all using **Python, OpenCV, MediaPipe, and PyAutoGUI**.

---

## 👋 Features

✅ Tracks your hand in real-time via webcam  
✅ Moves the mouse cursor using your **index finger**  
✅ Performs **left click** when you **pinch (thumb + index)**  
✅ Gesture-based control — no external device needed  
✅ Clean, interactive **Streamlit UI**  
✅ Runs 100% locally — **No Internet or API required**

---

## 🧠 How It Works

- **MediaPipe** detects 21 landmarks on your hand (palm, fingers).
- Based on the position of the **index finger tip**, the system moves the mouse.
- A **pinch gesture** (thumb tip + index tip close together) triggers a click.
- **PyAutoGUI** performs actual mouse movement and click events.
- **Streamlit** provides the UI to view webcam feed and gesture status.

---

## 🛠️ Built With

| Library      | Purpose |
|--------------|---------|
| `Python`     | Core programming logic |
| `OpenCV`     | Webcam feed and frame processing |
| `MediaPipe`  | Hand detection & tracking |
| `PyAutoGUI`  | Mouse control |
| `NumPy`      | Coordinate processing |
| `Streamlit`  | UI for running and visualizing |

---

## 📂 Folder Structure

```
virtual_mouse_streamlit/
├── app.py               # Streamlit frontend
├── virtual_mouse.py     # Gesture detection & control logic
├── requirements.txt     # All necessary libraries
├── README.md            # GitHub documentation
└── demo.gif / demo.mp4  # Optional demo preview
```

---

## 🚀 How to Run

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Launch the App

```bash
streamlit run app.py
```

> ⚠️ Allow webcam permissions when prompted.

---

## 🎥 Demo

![Demo](demo.gif)  
_(Add your own screen recording here showing hand control + cursor movement)_

---

## 💡 Use Cases

- Touchless computer control  
- Accessibility tools for differently abled users  
- Gesture-based automation  
- Fun AI + Computer Vision projects for students

---

## 📌 Notes

- Works on **Windows, Linux, Mac**
- No internet connection required — runs fully on your device
- Requires a working **webcam**

---

## ✨ Author

**Gulfam Baig**  
Self-taught AI/ML Developer | Passionate about building AI for real-world impact  
📧 [gulfambaig30@gmail.com](mailto:gulfambaig30@gmail.com)

---

## ⭐ Show Your Support

If you like this project, please ⭐ the repo and share it!  
Feel free to fork, improve, or contribute.
