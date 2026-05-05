# 匯入 sys，給 PyQt6 建立應用程式時使用
import sys

# 從 PyQt6 匯入 QtWidgets
from PyQt6 import QtWidgets


# 建立 PyQt6 應用程式
app = QtWidgets.QApplication(sys.argv)


# 建立主視窗
window = QtWidgets.QWidget()
window.setWindowTitle("按鈕事件練習")
window.resize(400, 300)


# 建立文字標籤
label = QtWidgets.QLabel("還沒按按鈕")

# 建立按鈕
button = QtWidgets.QPushButton("按我")


# 定義一個函式
# 這個函式會在按鈕被按下時執行
def change_text():
    label.setText("你按下按鈕了！")


# 把按鈕的 clicked 事件連接到 change_text 函式
button.clicked.connect(change_text)


# 建立垂直排版
layout = QtWidgets.QVBoxLayout()
layout.addWidget(label)
layout.addWidget(button)

window.setLayout(layout)


# 顯示視窗
window.show() 

# 啟動事件迴圈
sys.exit(app.exec())