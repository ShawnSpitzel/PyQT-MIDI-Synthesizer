from PyQt5.QtWidgets import (
    QPushButton,
    QWidget,
    QHBoxLayout,
)
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QGraphicsDropShadowEffect
from PyQt5.QtGui import QColor
from PyQt5.QtCore import Qt
from synthesizer.synthesizer import sine_wave
class OctaveWidget(QWidget):
    def __init__(self, octave_number=4):
        super().__init__()
        self.octave_number = octave_number
        self.white_keys = []
        self.black_keys = []

        self.setFixedHeight(220)
        self.layout = QHBoxLayout()
        self.layout.setSpacing(0)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.layout)

        white_notes = ["C", "D", "E", "F", "G", "A", "B"]
        black_notes = ["C#", "D#", "F#", "G#", "A#"]
        self.setFocusPolicy(Qt.StrongFocus)
        self.setFocus()

        white_width = 60
        black_width = 40

        for name in white_notes:
            btn = QPushButton(name + str(octave_number))
            btn.setFixedSize(white_width, 200)
            btn.setStyleSheet(
                """
                QPushButton {
                    background-color: white;
                    border: 1px solid black;
                }
                QPushButton:pressed {
                    background-color: lightgray;
                }
            """
            )
            btn.setFont(QFont("Arial", 10, QFont.Bold))
            btn.setFocusPolicy(Qt.NoFocus)
            btn.setStyleSheet(
                """
                QPushButton {
                    background-color: white;
                    border: 1px solid black;
                    qproperty-iconSize: 20px;
                    text-align: bottom center;
                }
                QPushButton:pressed {
                    background-color: lightgray;
                }
            """
            )
            self.layout.addWidget(btn)
            btn.clicked.connect(self.on_key_pressed)
            self.white_keys.append(btn)
        self.black_positions = [0, 1, 3, 4, 5]
        for i, note in zip(self.black_positions, black_notes):
            x = (i + 1) * white_width - black_width // 2
            btn = QPushButton(note + str(octave_number), self)
            btn.setFixedSize(black_width, 120)
            btn.move(x, 0)
            btn.setStyleSheet(
                """
                QPushButton {
                    background-color: black;
                    color: white;
                    border: 1px solid black;
                }
                QPushButton:pressed {
                    background-color: #444444;
                }
            """
            )
            btn.setFont(QFont("Arial", 8, QFont.Bold))
            btn.clicked.connect(self.on_key_pressed)
            shadow = QGraphicsDropShadowEffect(self)
            shadow.setBlurRadius(15)
            shadow.setOffset(0, 4)
            shadow.setColor(QColor(0, 0, 0, 150))
            btn.setGraphicsEffect(shadow)
            btn.setFocusPolicy(Qt.NoFocus)

            self.black_keys.append(btn)
            btn.raise_()
            self.keyboard_mapping = {
                Qt.Key_Q: "C5",
                Qt.Key_2: "C#5",
                Qt.Key_W: "D5",
                Qt.Key_3: "D#5",
                Qt.Key_E: "E5",
                Qt.Key_R: "F5",
                Qt.Key_5: "F#5",
                Qt.Key_T: "G5",
                Qt.Key_6: "G#5",
                Qt.Key_Y: "A5",
                Qt.Key_7: "A#5",
                Qt.Key_U: "B5",
                Qt.Key_Z: "C4",
                Qt.Key_S: "C#4",
                Qt.Key_X: "D4",
                Qt.Key_D: "D#4",
                Qt.Key_C: "E4",
                Qt.Key_V: "F4",
                Qt.Key_G: "F#4",
                Qt.Key_B: "G4",
                Qt.Key_H: "G#4",
                Qt.Key_N: "A4",
                Qt.Key_J: "A#4",
                Qt.Key_M: "B4",
                Qt.Key_Comma: "C5",
                Qt.Key_L: "C#5",
                Qt.Key_Period: "D5",
            }

        self.note_to_button = {}
        for btn in self.white_keys + self.black_keys:
            self.note_to_button[btn.text()] = btn

    def keyPressEvent(self, event):
        key = event.key()
        if key in self.keyboard_mapping:
            note = self.keyboard_mapping[key]
            btn = self.note_to_button.get(note)
            if btn:
                btn.click()
        else:
            super().keyPressEvent(event)

    def on_key_pressed(self):
        sender = self.sender()
        print(f"Key pressed: {sender.text()}")
        sine_wave(sender.text(), duration=0.5, volume=0.3)

