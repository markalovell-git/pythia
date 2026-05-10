from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Astrology App")
        self.setGeometry(100, 100, 800, 600)
        
        label = QLabel("Welcome to the Astrology App", self)
        label.move(300, 250)

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()