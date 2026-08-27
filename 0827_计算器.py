from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QLineEdit
import sys

class Calc(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("苹果计算器复刻")
        self.resize(320,480)
        layout = QGridLayout()
        self.display = QLineEdit()
        self.display.setReadOnly(True)
        layout.addWidget(self.display,0,0,1,4)

        btns = [
            ["AC","±","%","÷"],
            ["7","8","9","×"],
            ["4","5","6","−"],
            ["1","2","3","+"],
            ["0",".","="]
        ]
        for row_idx,row in enumerate(btns,1):
            col_idx=0
            for text in row:
                btn = QPushButton(text)
                if text == "0":
                    layout.addWidget(btn,row_idx,col_idx,1,2)
                    col_idx +=2
                else:
                    layout.addWidget(btn,row_idx,col_idx)
                    col_idx +=1
        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Calc()
    win.show()
    sys.exit(app.exec())