# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Documents/netusage/netusage.ui'
#
# Created: Sun Jan  1 22:44:22 2012
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(294, 484)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "NetUsage", None, QtGui.QApplication.UnicodeUTF8))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.layoutWidget = QtGui.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(9, 97, 281, 68))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.layoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_2 = QtGui.QLabel(self.layoutWidget)
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Ipv4 :", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.ip4_label = QtGui.QLabel(self.layoutWidget)
        self.ip4_label.setText(_fromUtf8(""))
        self.ip4_label.setObjectName(_fromUtf8("ip4_label"))
        self.gridLayout.addWidget(self.ip4_label, 0, 1, 1, 1)
        self.mac_label = QtGui.QLabel(self.layoutWidget)
        self.mac_label.setText(_fromUtf8(""))
        self.mac_label.setObjectName(_fromUtf8("mac_label"))
        self.gridLayout.addWidget(self.mac_label, 1, 1, 1, 1)
        self.ip6_label_2 = QtGui.QLabel(self.layoutWidget)
        self.ip6_label_2.setText(QtGui.QApplication.translate("MainWindow", "MAC :", None, QtGui.QApplication.UnicodeUTF8))
        self.ip6_label_2.setObjectName(_fromUtf8("ip6_label_2"))
        self.gridLayout.addWidget(self.ip6_label_2, 1, 0, 1, 1)
        self.layoutWidget1 = QtGui.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 370, 281, 62))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.gridLayout_3 = QtGui.QGridLayout(self.layoutWidget1)
        self.gridLayout_3.setMargin(0)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.label_12 = QtGui.QLabel(self.layoutWidget1)
        self.label_12.setText(QtGui.QApplication.translate("MainWindow", "Bill factor :", None, QtGui.QApplication.UnicodeUTF8))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.gridLayout_3.addWidget(self.label_12, 0, 0, 1, 1)
        self.bill_factor = QtGui.QDoubleSpinBox(self.layoutWidget1)
        self.bill_factor.setObjectName(_fromUtf8("bill_factor"))
        self.gridLayout_3.addWidget(self.bill_factor, 0, 1, 1, 1)
        self.label_13 = QtGui.QLabel(self.layoutWidget1)
        self.label_13.setText(QtGui.QApplication.translate("MainWindow", "value on :", None, QtGui.QApplication.UnicodeUTF8))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.gridLayout_3.addWidget(self.label_13, 1, 0, 1, 1)
        self.comboBox = QtGui.QComboBox(self.layoutWidget1)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.setItemText(0, QtGui.QApplication.translate("MainWindow", "Today", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.setItemText(1, QtGui.QApplication.translate("MainWindow", "Month", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.setItemText(2, QtGui.QApplication.translate("MainWindow", "Year", None, QtGui.QApplication.UnicodeUTF8))
        self.gridLayout_3.addWidget(self.comboBox, 1, 1, 1, 1)
        self.bill_value = QtGui.QLabel(self.layoutWidget1)
        self.bill_value.setText(_fromUtf8(""))
        self.bill_value.setObjectName(_fromUtf8("bill_value"))
        self.gridLayout_3.addWidget(self.bill_value, 1, 2, 1, 1)
        self.layoutWidget2 = QtGui.QWidget(self.centralwidget)
        self.layoutWidget2.setGeometry(QtCore.QRect(289, 100, 141, 331))
        self.layoutWidget2.setObjectName(_fromUtf8("layoutWidget2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        spacerItem = QtGui.QSpacerItem(148, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem)
        spacerItem1 = QtGui.QSpacerItem(148, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem1)
        spacerItem2 = QtGui.QSpacerItem(148, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem2)
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 170, 271, 191))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.widget)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_6 = QtGui.QLabel(self.widget)
        self.label_6.setText(QtGui.QApplication.translate("MainWindow", "usage :", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout_2.addWidget(self.label_6, 0, 0, 1, 1)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_7 = QtGui.QLabel(self.widget)
        self.label_7.setText(QtGui.QApplication.translate("MainWindow", "upload :", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout_3.addWidget(self.label_7)
        self.upload_label = QtGui.QLabel(self.widget)
        self.upload_label.setText(_fromUtf8(""))
        self.upload_label.setObjectName(_fromUtf8("upload_label"))
        self.horizontalLayout_3.addWidget(self.upload_label)
        self.gridLayout_2.addLayout(self.horizontalLayout_3, 1, 0, 1, 1)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_8 = QtGui.QLabel(self.widget)
        self.label_8.setText(QtGui.QApplication.translate("MainWindow", "download :", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.horizontalLayout_4.addWidget(self.label_8)
        self.download_label = QtGui.QLabel(self.widget)
        self.download_label.setText(_fromUtf8(""))
        self.download_label.setObjectName(_fromUtf8("download_label"))
        self.horizontalLayout_4.addWidget(self.download_label)
        self.gridLayout_2.addLayout(self.horizontalLayout_4, 2, 0, 1, 1)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_9 = QtGui.QLabel(self.widget)
        self.label_9.setText(QtGui.QApplication.translate("MainWindow", "Today:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.horizontalLayout_5.addWidget(self.label_9)
        self.Today_label = QtGui.QLabel(self.widget)
        self.Today_label.setText(_fromUtf8(""))
        self.Today_label.setObjectName(_fromUtf8("Today_label"))
        self.horizontalLayout_5.addWidget(self.Today_label)
        self.gridLayout_2.addLayout(self.horizontalLayout_5, 3, 0, 1, 1)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.label_10 = QtGui.QLabel(self.widget)
        self.label_10.setText(QtGui.QApplication.translate("MainWindow", "Month :", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.horizontalLayout_6.addWidget(self.label_10)
        self.Month_label = QtGui.QLabel(self.widget)
        self.Month_label.setText(_fromUtf8(""))
        self.Month_label.setObjectName(_fromUtf8("Month_label"))
        self.horizontalLayout_6.addWidget(self.Month_label)
        self.gridLayout_2.addLayout(self.horizontalLayout_6, 4, 0, 1, 1)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.label_11 = QtGui.QLabel(self.widget)
        self.label_11.setText(QtGui.QApplication.translate("MainWindow", "year:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.horizontalLayout_7.addWidget(self.label_11)
        self.Year_label = QtGui.QLabel(self.widget)
        self.Year_label.setText(_fromUtf8(""))
        self.Year_label.setObjectName(_fromUtf8("Year_label"))
        self.horizontalLayout_7.addWidget(self.Year_label)
        self.gridLayout_2.addLayout(self.horizontalLayout_7, 5, 0, 1, 1)
        self.widget1 = QtGui.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(10, 10, 171, 71))
        self.widget1.setObjectName(_fromUtf8("widget1"))
        self.verticalLayout = QtGui.QVBoxLayout(self.widget1)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.widget1)
        self.label.setText(QtGui.QApplication.translate("MainWindow", "interface :", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.interfaces = QtGui.QComboBox(self.widget1)
        self.interfaces.setObjectName(_fromUtf8("interfaces"))
        self.verticalLayout.addWidget(self.interfaces)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 294, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.interfaces, self.bill_factor)
        MainWindow.setTabOrder(self.bill_factor, self.comboBox)

    def retranslateUi(self, MainWindow):
        pass

