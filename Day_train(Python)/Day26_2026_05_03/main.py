import sys

from PyQt6. QtWidgets import QApplication , QWidget

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("我的第一個 PyQt6 視窗")

window.resize(400,300)

window.show()

sys.exit(app.exec())