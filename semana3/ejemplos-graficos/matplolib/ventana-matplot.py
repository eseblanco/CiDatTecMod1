"""
Valorar

https://www.youtube.com/watch?v=2C5VnE9wPhk

https://www.youtube.com/watch?v=d663N2xTxO0


###############

#  video que si funciono
https://www.youtube.com/watch?v=d663N2xTxO0
"""


from PyQt5 import  QtWidgets
from BIBLIOTECAS.Basicas.matplolib.graf.main import Ui_MainWindow

import sys
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec_())
