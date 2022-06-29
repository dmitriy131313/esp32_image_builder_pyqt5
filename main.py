from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QPlainTextEdit
from m_ui import Ui_MainWindow
import sys
from PartitionManager import *

class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setFixedSize(454, 180)
        self.prt = PartitionManager()

        self.ui.button_proj_dir.clicked.connect(self.setProjDir)
        self.ui.button_make.clicked.connect(self.__make)

        self.ui.text_bl_offset.textChanged.connect(self.__checkBL_offset_input)
        self.ui.text_bl_size.textChanged.connect(self.__checkBL_size_input)
        self.ui.text_pt_offset.textChanged.connect(self.__checkPT_offset_input)

        self.prt.setBootloaderOffset(self.ui.text_bl_offset.toPlainText())
        self.prt.setBootloaderSize(self.ui.text_bl_size.toPlainText())
        self.prt.setPartitionTableOffset(self.ui.text_pt_offset.toPlainText())

    def setProjDir(self):
        try:
            self.file = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
            self.prt.setProjDir(self.file)
            self.prt.setBootloaderOffset(self.ui.text_bl_offset.toPlainText())
            self.prt.setBootloaderSize(self.ui.text_bl_size.toPlainText())
            self.prt.setPartitionTableOffset(self.ui.text_pt_offset.toPlainText())
            self.prt.findPartitions()
            self.ui.button_make.setEnabled(True)
        except OSError as error :
            QMessageBox.warning(self, "Warning", str(error))
            self.ui.button_make.setEnabled(False)
        except PartitionManagerException as error:
            QMessageBox.warning(self, "Warning", str(error))
            self.ui.button_make.setEnabled(False)
        except ValueError as error:
            QMessageBox.warning(self, "Warning", str(error))
            self.ui.button_make.setEnabled(False)
        except TypeError:
            QMessageBox.warning(self, "Warning", 'Project name in CMakeLists.txt is not found')
            self.ui.button_make.setEnabled(False)
        except Exception as error:
            QMessageBox.warning(self, "Warning", 'Unhandled error: ' + str(error))
            self.ui.button_make.setEnabled(False)

    def __make(self):
        try:
            name = QFileDialog.getSaveFileName(self, 'Save File')
            self.prt.makeBinary(name)
        except Exception as error:
            QMessageBox.warning(self, "Warning", 'Error while making binary: ' + str(error))  

    def __input_check(self, obj : QPlainTextEdit):
        color = '255, 0, 0' if re.search(r'^0[xX][0-9a-fA-F]+$', obj.toPlainText()) == None else '255, 255, 255'
        obj.setStyleSheet(f"background-color: rgb({color});")
        return True if color == '255, 255, 255' else False

    def __checkBL_offset_input(self):
        self.__input_check(self.ui.text_bl_offset)

    def __checkBL_size_input(self):
        self.__input_check(self.ui.text_bl_size)

    def __checkPT_offset_input(self):
        self.__input_check(self.ui.text_pt_offset)

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    application = mywindow()
    application.show()
 
    sys.exit(app.exec())