from PyQt5.QtWidgets import *
import sys, os
app = QApplication(sys.argv)
w = QWidget(); w.show(); l = QLabel("This is a Python App!", w); b = QPushButton("Exit", w); b.clicked.connect(lambda: os.kill(os.getpid(), 9)); sys.exit(app.exec_())
