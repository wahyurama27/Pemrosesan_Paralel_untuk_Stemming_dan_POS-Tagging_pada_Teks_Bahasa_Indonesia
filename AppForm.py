import sys
import os
from PemrosesanSerial import PemrosesanSerial
from PemrosesanParalel import PemrosesanParalel
from PraPengolahan import PraPengolahan
from PraPengolahanLanjut import PraPengolahanLanjut
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QFileDialog
from PyQt5.QtCore import QCoreApplication
from pathlib import Path

class AppForm(QWidget):
    result_prapengolahan = []
    result_split = []
    processor = int()

    def setup_ui(self, MainWindow):
        MainWindow.setObjectName("Pemrosesan Paralel Stemming dan POS-Tagging")
        MainWindow.resize(500, 460)
        MainWindow.setAutoFillBackground(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.dialog_filename = ""

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(440, 210, 39, 31))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(440, 260, 39, 21))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(11)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")

        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(440, 300, 39, 31))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(11)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")

        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(440, 350, 39, 21))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(11)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")

        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(250, 220, 21, 21))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(11)
        self.label_18.setFont(font)
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName("label_18")

        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(250, 260, 21, 21))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(11)
        self.label_19.setFont(font)
        self.label_19.setAlignment(QtCore.Qt.AlignCenter)
        self.label_19.setObjectName("label_19")

        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        self.label_20.setGeometry(QtCore.QRect(250, 310, 21, 21))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(11)
        self.label_20.setFont(font)
        self.label_20.setAlignment(QtCore.Qt.AlignCenter)
        self.label_20.setObjectName("label_20")

        self.label_21 = QtWidgets.QLabel(self.centralwidget)
        self.label_21.setGeometry(QtCore.QRect(250, 350, 21, 21))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(11)
        self.label_21.setFont(font)
        self.label_21.setAlignment(QtCore.Qt.AlignCenter)
        self.label_21.setObjectName("label_21")

        self.label_judul = QtWidgets.QLabel(self.centralwidget)
        self.label_judul.setGeometry(QtCore.QRect(50, 20, 401, 31))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_judul.setFont(font)
        self.label_judul.setAlignment(QtCore.Qt.AlignCenter)
        self.label_judul.setWordWrap(True)
        self.label_judul.setObjectName("label_judul")

        self.field_path_dokumen = QtWidgets.QLineEdit(self.centralwidget)
        self.field_path_dokumen.setGeometry(QtCore.QRect(20, 70, 461, 28))

        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)

        self.field_path_dokumen.setPalette(palette)
        self.field_path_dokumen.setAutoFillBackground(False)
        self.field_path_dokumen.setObjectName("field_path_dokumen")

        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 110, 461, 31))
        self.layoutWidget.setObjectName("layoutWidget")

        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")

        self.tombol_browse_file = QtWidgets.QPushButton(self.layoutWidget)
        self.tombol_browse_file.setObjectName("tombol_browse_file")
        self.horizontalLayout_3.addWidget(self.tombol_browse_file)

        self.tombol_preprocess_file = QtWidgets.QPushButton(self.layoutWidget)
        self.tombol_preprocess_file.setObjectName("tombol_preprocess_file")
        self.horizontalLayout_3.addWidget(self.tombol_preprocess_file)

        self.tombol_split_file = QtWidgets.QPushButton(self.layoutWidget)
        self.tombol_split_file.setObjectName("tombol_split_file")
        self.horizontalLayout_3.addWidget(self.tombol_split_file)

        self.label_jumlah_prosesor = QtWidgets.QLabel(self.centralwidget)
        self.label_jumlah_prosesor.setGeometry(QtCore.QRect(20, 150, 461, 31))

        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(11)
        self.label_jumlah_prosesor.setFont(font)
        self.label_jumlah_prosesor.setAlignment(QtCore.Qt.AlignCenter)
        self.label_jumlah_prosesor.setObjectName("label_jumlah_prosesor")

        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(270, 200, 161, 191))
        self.layoutWidget1.setObjectName("layoutWidget1")

        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.akumulasi_serial_postagging = QtWidgets.QLineEdit(self.layoutWidget1)
        self.akumulasi_serial_postagging.setAlignment(QtCore.Qt.AlignCenter)
        self.akumulasi_serial_postagging.setClearButtonEnabled(False)
        self.akumulasi_serial_postagging.setObjectName("akumulasi_serial_postagging")
        self.verticalLayout_2.addWidget(self.akumulasi_serial_postagging)

        self.akumulasi_serial_stemming = QtWidgets.QLineEdit(self.layoutWidget1)
        self.akumulasi_serial_stemming.setAlignment(QtCore.Qt.AlignCenter)
        self.akumulasi_serial_stemming.setObjectName("akumulasi_serial_stemming")
        self.verticalLayout_2.addWidget(self.akumulasi_serial_stemming)

        self.akumulasi_multiproses_postagging = QtWidgets.QLineEdit(self.layoutWidget1)
        self.akumulasi_multiproses_postagging.setAlignment(QtCore.Qt.AlignCenter)
        self.akumulasi_multiproses_postagging.setObjectName("akumulasi_multiproses_postagging")
        self.verticalLayout_2.addWidget(self.akumulasi_multiproses_postagging)

        self.akumulasi_multiproses_stemming = QtWidgets.QLineEdit(self.layoutWidget1)
        self.akumulasi_multiproses_stemming.setAlignment(QtCore.Qt.AlignCenter)
        self.akumulasi_multiproses_stemming.setObjectName("akumulasi_multiproses_stemming")
        self.verticalLayout_2.addWidget(self.akumulasi_multiproses_stemming)

        self.layoutWidget2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget2.setGeometry(QtCore.QRect(20, 200, 231, 191))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(11)
        self.layoutWidget2.setFont(font)
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.tombol_serial_postagging = QtWidgets.QPushButton(self.layoutWidget2)
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(11)
        self.tombol_serial_postagging.setFont(font)
        self.tombol_serial_postagging.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.tombol_serial_postagging.setAutoFillBackground(False)
        self.tombol_serial_postagging.setStyleSheet("background-color:rgb(170, 255, 127)")
        self.tombol_serial_postagging.setObjectName("tombol_serial_postagging")
        self.verticalLayout.addWidget(self.tombol_serial_postagging)

        self.tombol_serial_stemming = QtWidgets.QPushButton(self.layoutWidget2)
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(11)
        self.tombol_serial_stemming.setFont(font)
        self.tombol_serial_stemming.setStyleSheet("background-color:rgb(170, 255, 127)")
        self.tombol_serial_stemming.setObjectName("tombol_serial_stemming")
        self.verticalLayout.addWidget(self.tombol_serial_stemming)

        self.tombol_multiproses_postagging = QtWidgets.QPushButton(self.layoutWidget2)
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(11)
        self.tombol_multiproses_postagging.setFont(font)
        self.tombol_multiproses_postagging.setStyleSheet("background-color:rgb(170, 255, 127)")
        self.tombol_multiproses_postagging.setObjectName("tombol_multiproses_postagging")
        self.verticalLayout.addWidget(self.tombol_multiproses_postagging)

        self.tombol_multiproses_stemming = QtWidgets.QPushButton(self.layoutWidget2)
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(11)
        self.tombol_multiproses_stemming.setFont(font)
        self.tombol_multiproses_stemming.setStyleSheet("background-color:rgb(170, 255, 127)")
        self.tombol_multiproses_stemming.setObjectName("tombol_multiproses_stemming")
        self.verticalLayout.addWidget(self.tombol_multiproses_stemming)

        self.layoutWidget3 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget3.setGeometry(QtCore.QRect(190, 180, 128, 23))
        self.layoutWidget3.setObjectName("layoutWidget3")

        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.radio_2_prosesor = QtWidgets.QRadioButton(self.layoutWidget3)
        self.radio_2_prosesor.setObjectName("radio_2_prosesor")

        self.horizontalLayout.addWidget(self.radio_2_prosesor)

        self.radio_4_prosesor = QtWidgets.QRadioButton(self.layoutWidget3)
        self.radio_4_prosesor.setObjectName("radio_4_prosesor")

        self.horizontalLayout.addWidget(self.radio_4_prosesor)

        self.radio_6_prosesor = QtWidgets.QRadioButton(self.layoutWidget3)
        self.radio_6_prosesor.setObjectName("radio_6_prosesor")

        self.horizontalLayout.addWidget(self.radio_6_prosesor)

        self.layoutWidget4 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget4.setGeometry(QtCore.QRect(20, 410, 461, 29))
        self.layoutWidget4.setObjectName("layoutWidget4")

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget4)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(8)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.tombol_reset = QtWidgets.QPushButton(self.layoutWidget4)
        self.tombol_reset.setObjectName("tombol_reset")

        self.horizontalLayout_2.addWidget(self.tombol_reset)

        self.tombol_manual = QtWidgets.QPushButton(self.layoutWidget4)
        self.tombol_manual.setObjectName("tombol_manual")

        self.horizontalLayout_2.addWidget(self.tombol_manual)

        self.tombol_exit = QtWidgets.QPushButton(self.layoutWidget4)
        self.tombol_exit.setStyleSheet("")
        self.tombol_exit.setObjectName("tombol_exit")

        self.horizontalLayout_2.addWidget(self.tombol_exit)


        self.label_4.raise_()
        self.label_15.raise_()
        self.label_16.raise_()
        self.label_17.raise_()
        self.label_18.raise_()
        self.label_19.raise_()
        self.label_20.raise_()
        self.label_21.raise_()
        self.label_judul.raise_()
        self.field_path_dokumen.raise_()
        self.layoutWidget.raise_()
        self.label_jumlah_prosesor.raise_()
        self.layoutWidget.raise_()
        self.layoutWidget.raise_()
        self.layoutWidget.raise_()
        self.layoutWidget.raise_()

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def pra_pengolahan(self):
        self.result_prapengolahan = PraPengolahan(self.dialog_filename).prepro()

    def data_split(self):
        self.result_split = PraPengolahanLanjut(self.result_prapengolahan).split_file(self.processor)

    def serial_stem(self):
        result = PemrosesanSerial(self.result_prapengolahan).serial_stemming()
        self.akumulasi_serial_stemming.setText(f"{result}")

    def serial_pos(self):
        result = PemrosesanSerial(self.result_prapengolahan).serial_pos_tagging()
        self.akumulasi_serial_postagging.setText(f"{result}")

    def multi_stem(self):
        result = PemrosesanParalel(self.result_split).multi_stem()
        self.akumulasi_multiproses_stemming.setText(f"{result}")

    def multi_pos(self):
        result = PemrosesanParalel(self.result_split).multi_tagging()
        self.akumulasi_multiproses_postagging.setText(f"{result}")

    def browseFile_handler(self):
        self.open_dialog_box()

    def open_dialog_box(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Text files (*.txt)", options=options)
        print(fileName)
        self.field_path_dokumen.setText(fileName)
        self.dialog_filename = fileName

    def two_processor_clicked(self, selected):
        if selected:
            self.processor = int(2)

    def four_processor_clicked(self, selected):
        if selected:
            self.processor = int(4)

    def six_processor_clicked(self, selected):
        if selected:
            self.processor = int(6)

    def reset(self):
        self.akumulasi_multiproses_stemming.clear()
        self.akumulasi_multiproses_postagging.clear()
        self.akumulasi_serial_postagging.clear()
        self.akumulasi_serial_stemming.clear()
        self.field_path_dokumen.clear()
        return

    def manual(self):
        path = os.path.realpath(__file__)
        p = Path(path)
        path_dir = str(p.parent)
        path_info = path_dir + '/manual.pdf'
        os.system("xdg-open " + path_info)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

        self.label_4.setText(_translate("MainWindow", "second"))
        self.label_15.setText(_translate("MainWindow", "second"))
        self.label_16.setText(_translate("MainWindow", "second"))
        self.label_17.setText(_translate("MainWindow", "second"))

        self.label_18.setText(_translate("MainWindow", "="))
        self.label_19.setText(_translate("MainWindow", "="))
        self.label_20.setText(_translate("MainWindow", "="))
        self.label_21.setText(_translate("MainWindow", "="))

        self.label_judul.setText(_translate("MainWindow", "PEMROSESAN PARALEL UNTUK STEMMING DAN POS-TAGGING PADA TEKS BAHASA INDONESIA"))

        self.field_path_dokumen.setPlaceholderText(_translate("MainWindow", "input file here ..."))

        #browse file
        self.tombol_browse_file.setText(_translate("MainWindow", "Browse File..."))
        self.tombol_browse_file.clicked.connect(self.browseFile_handler)

        #preprocess file
        self.tombol_preprocess_file.setText(_translate("MainWindow", "Preprocess"))
        self.tombol_preprocess_file.clicked.connect(lambda : self.pra_pengolahan())

        #split file
        self.tombol_split_file.setText(_translate("MainWindow", "Split File"))
        self.tombol_split_file.clicked.connect(lambda : self.data_split())

        self.label_jumlah_prosesor.setText(_translate("MainWindow", "before split the document for multiprocessing, please choose number of processor"))

        #processor allocation
        self.radio_2_prosesor.setText(_translate("MainWindow", "2"))
        self.radio_2_prosesor.toggled.connect(self.two_processor_clicked)

        self.radio_4_prosesor.setText(_translate("MainWindow", "4"))
        self.radio_4_prosesor.toggled.connect(self.four_processor_clicked)

        self.radio_6_prosesor.setText(_translate("MainWindow", "6"))
        self.radio_6_prosesor.toggled.connect(self.six_processor_clicked)

        self.akumulasi_serial_postagging.setPlaceholderText(_translate("MainWindow", "time accumulation"))
        self.akumulasi_serial_stemming.setPlaceholderText(_translate("MainWindow", "time accumulation"))
        self.akumulasi_multiproses_postagging.setPlaceholderText(_translate("MainWindow", "time accumulation"))
        self.akumulasi_multiproses_stemming.setPlaceholderText(_translate("MainWindow", "time accumulation"))

        #main processing
        self.tombol_serial_postagging.setText(_translate("MainWindow", "Serial POS-Tagging"))
        self.tombol_serial_postagging.clicked.connect(lambda: self.serial_pos())

        self.tombol_serial_stemming.setText(_translate("MainWindow", "Serial Stemming"))
        self.tombol_serial_stemming.clicked.connect(lambda: self.serial_stem())

        self.tombol_multiproses_postagging.setText(_translate("MainWindow", "Multiprocessing POS-Tagging"))
        self.tombol_multiproses_postagging.clicked.connect(lambda: self.multi_pos())

        self.tombol_multiproses_stemming.setText(_translate("MainWindow", "Multiprocessing Stemming"))
        self.tombol_multiproses_stemming.clicked.connect(lambda: self.multi_stem())

        #Standard Button
        self.tombol_reset.setText(_translate("MainWindow", "Reset"))
        self.tombol_reset.clicked.connect(lambda :self.reset())

        self.tombol_manual.setText(_translate("MainWindow", "Manual"))
        self.tombol_manual.clicked.connect(lambda : self.manual())

        self.tombol_exit.setText(_translate("MainWindow", "Exit"))
        self.tombol_exit.clicked.connect(QCoreApplication.instance().quit)



if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = AppForm()
    ui.setup_ui(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())