import sys
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
    QLabel,
    QFrame,
    QGroupBox,
    QHBoxLayout,
)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QGraphicsDropShadowEffect
from PyQt5.QtGui import QColor
from widgets.piano import PianoWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Sound Synthesizer")
        self.setGeometry(700, 300, 1080, 720)
        main_layout = QVBoxLayout()

        # ---------- HEADER ----------
        header = QFrame()
        header.setFrameShape(QFrame.Box)
        header_layout = QHBoxLayout()
        self.label = QLabel("Sound Synthesizer")
        self.label.setFont(QFont("Arial", 20, QFont.Bold))
        header_layout.addWidget(self.label, alignment=Qt.AlignLeft)
        header.setLayout(header_layout)
        main_layout.addWidget(header)

        # ---------- MAIN CONTENT ----------
        main_content = QHBoxLayout()
        preview = QFrame()
        preview.setFrameShape(QFrame.Box)
        preview_layout = QVBoxLayout()
        piano = PianoWidget()
        preview_layout.addWidget(piano, alignment=Qt.AlignTop | Qt.AlignHCenter)
        preview.setLayout(preview_layout)

        # ---------- SIDE BAR ----------
        sidebar = QFrame()
        sidebar.setFrameShape(QFrame.Box)
        sidebar_layout = QVBoxLayout()
        sidebar_layout.addWidget(QLabel("Sidebar"))
        sidebar.setLayout(sidebar_layout)

        main_content.addWidget(preview, 7)
        main_content.addWidget(sidebar, 3)
        main_layout.addLayout(main_content)

        # ---------- FOOTER ----------
        footer = QFrame()
        footer.setFrameShape(QFrame.Box)
        footer_layout = QVBoxLayout()
        footer_layout.addWidget(QLabel("Footer Area"))
        footer.setLayout(footer_layout)
        main_layout.addWidget(footer, stretch=3)
        main_layout.setStretchFactor(main_content, 7)

        # ---------- SET CENTRAL WIDGET ----------
        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
