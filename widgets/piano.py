from PyQt5.QtWidgets import (
    QVBoxLayout,
    QWidget,
)
from PyQt5.QtCore import Qt
from widgets.octave import OctaveWidget
class PianoWidget(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        layout.setSpacing(10)
        layout.setContentsMargins(0, 0, 0, 0)
        octave1 = OctaveWidget(octave_number=4)
        layout.addWidget(octave1, alignment=Qt.AlignHCenter)
        octave2 = OctaveWidget(octave_number=5)
        layout.addWidget(octave2, alignment=Qt.AlignHCenter)

        self.setLayout(layout)