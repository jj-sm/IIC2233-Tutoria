from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import QTimer, QTime

class Clock(QLabel):
    def __init__(self, parent=None, color="blue"):
        super().__init__(parent)
        self.color = color
        self.initialize()

    def initialize(self):
        self.setMinimumSize(150, 50)
        self.setStyleSheet(self.custom_style())
        self.setText("00:00:00")
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000) 
        self.update_time()

    def update_time(self):
        current_time = QTime.currentTime().toString("hh:mm:ss")
        self.setText(current_time)

    def custom_style(self):
        return f"""
        QLabel {{
            font-family: 'Arial';
            font-weight: bold;
            color: {self.color};
            font-size: 24px;
            padding: 10px;
        }}
        """


if __name__ == "__main__":
    from PyQt5.QtWidgets import QApplication
    import sys

    app = QApplication(sys.argv)
    clock = Clock()
    clock.show()
    sys.exit(app.exec_())