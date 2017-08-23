# coding=utf-8
import sys
from PySide import QtGui
import rc


class Widget(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)

        png_label = QtGui.QLabel()
        svg_label = QtGui.QLabel()

        v_layout = QtGui.QVBoxLayout(self)
        v_layout.addWidget(QtGui.QLabel("png:"))
        v_layout.addWidget(png_label)
        v_layout.addWidget(QtGui.QLabel("svg:"))
        v_layout.addWidget(svg_label)

        png_label.setPixmap(QtGui.QPixmap(":/example1.png").scaled(200, 200))
        svg_label.setPixmap(QtGui.QPixmap(":/example2.svg").scaled(200, 200))


app = QtGui.QApplication(sys.argv)
w = Widget()
w.show()
sys.exit(app.exec_())
