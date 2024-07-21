from PySide2.QtWidgets import QApplication, QWidget
from PySide2.QtUiTools import QUiLoader
from PySide2.QtGui import QIcon

import Random
from list_themes import *


class Stats:
    def __init__(self):
        # 从ui文件中加载UI定义,从UI定义中动态创建一个相应的窗口对象
        # 注意：里面的控件对象也成为窗口对象的属性了.比如 self.ui.button , self.ui.textEdit
        self.ui = QUiLoader().load('Random.ui')
        self.ui.toolButton.clicked.connect(self.handleCalc)
        self.ui.lineEdit_1.returnPressed.connect(self.handleCalc)  # 单行文本框回车消息
        self.ui.lineEdit_2.returnPressed.connect(self.handleCalc)  # 单行文本框回车消息
        self.ui.lineEdit_3.returnPressed.connect(self.handleCalc)  # 单行文本框回车消息

    def handleCalc(self):
        self.ui.textBrowser.clear()
        start = int(self.ui.lineEdit_1.text())
        end = int(self.ui.lineEdit_2.text())
        length = int(self.ui.lineEdit_3.text())
        itemText = self.ui.buttonGroup.checkedButton().text()
        if itemText == 'YES':
            repeat = 1
        else:
            repeat = 0
        list = Random.main(start, end, length, repeat)
        str = "\n".join('%s' % id for id in list)  # int转str再拼接，%id转%s
        self.ui.textBrowser.append(str)


if __name__ == '__main__':
    app = QApplication([])
    app.setWindowIcon(QIcon('image.png'))
    apply_stylesheet(app, theme[23], extra=extra, invert_secondary=True)  # 默认dark-False
    w = QWidget()
    w.setWindowIcon(QIcon('image.png'))
    stats = Stats()
    stats.ui.show()
    app.exec_()
