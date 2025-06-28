import sys
import cv2
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel, QPushButton, 
                            QVBoxLayout, QWidget)
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import QTimer
from virtual_mouse import HandMouseController

class VirtualMouseApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("🖱️ AI Virtual Mouse using Hand Gestures")
        self.setGeometry(100, 100, 800, 600)
        
        # Central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()
        
        # Title label
        self.title_label = QLabel("Control your mouse with just your hand using webcam + AI!")
        layout.addWidget(self.title_label)
        
        # Start button
        self.start_button = QPushButton("Start Virtual Mouse")
        self.start_button.clicked.connect(self.toggle_camera)
        layout.addWidget(self.start_button)
        
        # Video display
        self.video_label = QLabel()
        layout.addWidget(self.video_label)
        
        central_widget.setLayout(layout)
        
        # Camera and controller setup
        self.cap = None
        self.controller = HandMouseController()
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_frame)
        self.is_running = False

    def toggle_camera(self):
        if not self.is_running:
            self.cap = cv2.VideoCapture(0)
            if not self.cap.isOpened():
                self.title_label.setText("Error: Webcam not detected.")
                return
            self.timer.start(20)  # Update ~50 fps
            self.start_button.setText("Stop Virtual Mouse")
            self.is_running = True
        else:
            self.timer.stop()
            if self.cap:
                self.cap.release()
            self.start_button.setText("Start Virtual Mouse")
            self.is_running = False
            self.video_label.clear()

    def update_frame(self):
        ret, frame = self.cap.read()
        if not ret:
            self.title_label.setText("Error: Could not read frame.")
            self.timer.stop()
            return
        
        # Process frame
        frame = self.controller.process_frame(frame)
        
        # Convert to QImage
        rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        qt_image = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format_RGB888)
        
        # Display
        self.video_label.setPixmap(QPixmap.fromImage(qt_image).scaled(
            640, 480, aspectRatioMode=1))  # Keep aspect ratio

    def closeEvent(self, event):
        if self.cap and self.cap.isOpened():
            self.cap.release()
        self.timer.stop()
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = VirtualMouseApp()
    window.show()
    sys.exit(app.exec_())
