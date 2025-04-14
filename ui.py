import ctypes
from PyQt5 import QtWidgets, QtCore
from transcriber import start_transcription
import win32gui
import win32con

WDA_EXCLUDEFROMCAPTURE = 0x11

class CaptionApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("🎙️ Live Caption App")
        self.setWindowFlags(self.windowFlags() | QtCore.Qt.WindowStaysOnTopHint)
        self.setGeometry(100, 100, 500, 150)

        # Hide from screen sharing
        hwnd = self.winId().__int__()
        ctypes.windll.user32.SetWindowDisplayAffinity(hwnd, WDA_EXCLUDEFROMCAPTURE)

        # Layout
        layout = QtWidgets.QVBoxLayout()

        self.caption_label = QtWidgets.QLabel("🎧 Listening...")
        self.caption_label.setWordWrap(True)
        self.caption_label.setStyleSheet("font-size: 16px;")
        layout.addWidget(self.caption_label)

        self.pin_button = QtWidgets.QPushButton("📌 Pin (On Top)")
        self.pin_button.setCheckable(True)
        self.pin_button.setChecked(True)
        self.pin_button.clicked.connect(self.toggle_on_top)
        layout.addWidget(self.pin_button)

        self.setLayout(layout)

        # Start transcription thread
        start_transcription(self.caption_label)

    def toggle_on_top(self):
        flags = self.windowFlags()
        if self.pin_button.isChecked():
            self.setWindowFlags(flags | QtCore.Qt.WindowStaysOnTopHint)
            self.pin_button.setText("📌 Pin (On Top)")
        else:
            self.setWindowFlags(flags & ~QtCore.Qt.WindowStaysOnTopHint)
            self.pin_button.setText("📍 Unpinned")
        self.show()
