from PyQt5 import QtWidgets
from ui import CaptionApp
import sys

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = CaptionApp()
    window.show()
    sys.exit(app.exec_())