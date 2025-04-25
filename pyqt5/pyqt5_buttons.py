# PyQt5 Buttons
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 500, 500)
        # Make sure to use self. so button isn't a local variable
        self.button = QPushButton("Click me!", self)
        self.label = QLabel("Hello", self)
        self.counter = 1
        self.initUI()

    def initUI(self):
        self.button.setGeometry(150, 200, 200, 100)
        self.button.setStyleSheet("font-size: 24px;")
        self.button.clicked.connect(self.on_click)

        self.label.setGeometry(150, 300, 200, 100)
        self.label.setStyleSheet("font-size: 50px;")

    def on_click(self):
        print("Button clicked.")
        self.button.setText(f"Clicked {self.counter} times!")
        if self.counter == 10:
            self.button.setDisabled(True)
            self.label.setText("Goodbye")
        self.counter += 1


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
