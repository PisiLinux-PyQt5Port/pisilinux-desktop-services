# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pds/gui.ui'
#
# Created: Wed Nov 10 22:08:17 2010
#      by: PyQt5 UI code generator 4.8.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_PdsTest(object):
    def setupUi(self, PdsTest):
        PdsTest.setObjectName(_fromUtf8("PdsTest"))
        PdsTest.resize(947, 519)
        self.gridLayout_2 = QtWidgets.QGridLayout(PdsTest)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.lineMessage = QtWidgets.QLineEdit(PdsTest)
        self.lineMessage.setObjectName(_fromUtf8("lineMessage"))
        self.horizontalLayout_3.addWidget(self.lineMessage)
        self.enableOverlay = QtWidgets.QCheckBox(PdsTest)
        self.enableOverlay.setObjectName(_fromUtf8("enableOverlay"))
        self.horizontalLayout_3.addWidget(self.enableOverlay)
        self.animatedOverlay = QtWidgets.QCheckBox(PdsTest)
        self.animatedOverlay.setEnabled(False)
        self.animatedOverlay.setObjectName(_fromUtf8("animatedOverlay"))
        self.horizontalLayout_3.addWidget(self.animatedOverlay)
        self.enableBusy = QtWidgets.QCheckBox(PdsTest)
        self.enableBusy.setObjectName(_fromUtf8("enableBusy"))
        self.horizontalLayout_3.addWidget(self.enableBusy)
        self.gridLayout_2.addLayout(self.horizontalLayout_3, 0, 0, 1, 10)
        self.showButton = QtWidgets.QPushButton(PdsTest)
        self.showButton.setObjectName(_fromUtf8("showButton"))
        self.gridLayout_2.addWidget(self.showButton, 0, 10, 1, 1)
        self.label = QtWidgets.QLabel(PdsTest)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 1)
        self.inPos = QtWidgets.QComboBox(PdsTest)
        self.inPos.setObjectName(_fromUtf8("inPos"))
        self.inPos.addItem(_fromUtf8(""))
        self.inPos.addItem(_fromUtf8(""))
        self.inPos.addItem(_fromUtf8(""))
        self.inPos.addItem(_fromUtf8(""))
        self.inPos.addItem(_fromUtf8(""))
        self.inPos.addItem(_fromUtf8(""))
        self.inPos.addItem(_fromUtf8(""))
        self.inPos.addItem(_fromUtf8(""))
        self.inPos.addItem(_fromUtf8(""))
        self.gridLayout_2.addWidget(self.inPos, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(PdsTest)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_2.addWidget(self.label_3, 1, 2, 1, 1)
        self.stopPos = QtWidgets.QComboBox(PdsTest)
        self.stopPos.setObjectName(_fromUtf8("stopPos"))
        self.stopPos.addItem(_fromUtf8(""))
        self.stopPos.addItem(_fromUtf8(""))
        self.stopPos.addItem(_fromUtf8(""))
        self.stopPos.addItem(_fromUtf8(""))
        self.stopPos.addItem(_fromUtf8(""))
        self.stopPos.addItem(_fromUtf8(""))
        self.stopPos.addItem(_fromUtf8(""))
        self.stopPos.addItem(_fromUtf8(""))
        self.stopPos.addItem(_fromUtf8(""))
        self.gridLayout_2.addWidget(self.stopPos, 1, 3, 1, 1)
        self.label_4 = QtWidgets.QLabel(PdsTest)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_2.addWidget(self.label_4, 1, 4, 1, 1)
        self.outPos = QtWidgets.QComboBox(PdsTest)
        self.outPos.setObjectName(_fromUtf8("outPos"))
        self.outPos.addItem(_fromUtf8(""))
        self.outPos.addItem(_fromUtf8(""))
        self.outPos.addItem(_fromUtf8(""))
        self.outPos.addItem(_fromUtf8(""))
        self.outPos.addItem(_fromUtf8(""))
        self.outPos.addItem(_fromUtf8(""))
        self.outPos.addItem(_fromUtf8(""))
        self.outPos.addItem(_fromUtf8(""))
        self.outPos.addItem(_fromUtf8(""))
        self.gridLayout_2.addWidget(self.outPos, 1, 5, 1, 1)
        self.label_5 = QtWidgets.QLabel(PdsTest)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_2.addWidget(self.label_5, 1, 6, 1, 1)
        self.duration = QtWidgets.QSpinBox(PdsTest)
        self.duration.setMinimum(100)
        self.duration.setMaximum(5000)
        self.duration.setSingleStep(100)
        self.duration.setProperty(_fromUtf8("value"), 500)
        self.duration.setObjectName(_fromUtf8("duration"))
        self.gridLayout_2.addWidget(self.duration, 1, 7, 1, 1)
        self.label_2 = QtWidgets.QLabel(PdsTest)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_2.addWidget(self.label_2, 1, 8, 1, 1)
        self.animation = QtWidgets.QSpinBox(PdsTest)
        self.animation.setMinimum(0)
        self.animation.setMaximum(40)
        self.animation.setProperty(_fromUtf8("value"), 38)
        self.animation.setObjectName(_fromUtf8("animation"))
        self.gridLayout_2.addWidget(self.animation, 1, 9, 1, 1)
        self.hideButton = QtWidgets.QPushButton(PdsTest)
        self.hideButton.setObjectName(_fromUtf8("hideButton"))
        self.gridLayout_2.addWidget(self.hideButton, 1, 10, 1, 1)
        self.target = QtWidgets.QGroupBox(PdsTest)
        self.target.setObjectName(_fromUtf8("target"))
        self.gridLayout = QtWidgets.QGridLayout(self.target)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.webView = QtWebKit.QWebView(self.target)
        self.webView.setUrl(QtCore.QUrl(_fromUtf8("http://pisilinux.org")))
        self.webView.setObjectName(_fromUtf8("webView"))
        self.gridLayout.addWidget(self.webView, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.target, 2, 0, 1, 11)

        self.retranslateUi(PdsTest)
        self.inPos.setCurrentIndex(1)
        self.stopPos.setCurrentIndex(4)
        self.outPos.setCurrentIndex(7)
        self.enableOverlay.clicked.connect(self.animatedOverlay.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(PdsTest)

    def retranslateUi(self, PdsTest):
        PdsTest.setWindowTitle(QtWidgets.QApplication.translate("PdsTest", "Pds Test", None, QtWidgets.QApplication.UnicodeUTF8))
        self.lineMessage.setText(QtWidgets.QApplication.translate("PdsTest", "Hello Pardus !", None, QtWidgets.QApplication.UnicodeUTF8))
        self.lineMessage.setPlaceholderText(QtWidgets.QApplication.translate("PdsTest", "Type your message...", None, QtWidgets.QApplication.UnicodeUTF8))
        self.enableOverlay.setText(QtWidgets.QApplication.translate("PdsTest", "Enable Overlay", None, QtWidgets.QApplication.UnicodeUTF8))
        self.animatedOverlay.setText(QtWidgets.QApplication.translate("PdsTest", "Overlay Animated", None, QtWidgets.QApplication.UnicodeUTF8))
        self.enableBusy.setText(QtWidgets.QApplication.translate("PdsTest", "Enable Busy Indicator", None, QtWidgets.QApplication.UnicodeUTF8))
        self.showButton.setText(QtWidgets.QApplication.translate("PdsTest", "Show Message", None, QtWidgets.QApplication.UnicodeUTF8))
        self.label.setText(QtWidgets.QApplication.translate("PdsTest", "In Pos", None, QtWidgets.QApplication.UnicodeUTF8))
        self.inPos.setItemText(0, QtWidgets.QApplication.translate("PdsTest", "TOPLEFT", None, QtWidgets.QApplication.UnicodeUTF8))
        self.inPos.setItemText(1, QtWidgets.QApplication.translate("PdsTest", "TOPCENTER", None, QtWidgets.QApplication.UnicodeUTF8))
        self.inPos.setItemText(2, QtWidgets.QApplication.translate("PdsTest", "TOPRIGHT", None, QtWidgets.QApplication.UnicodeUTF8))
        self.inPos.setItemText(3, QtWidgets.QApplication.translate("PdsTest", "MIDDLELEFT", None, QtWidgets.QApplication.UnicodeUTF8))
        self.inPos.setItemText(4, QtWidgets.QApplication.translate("PdsTest", "MIDDLECENTER", None, QtWidgets.QApplication.UnicodeUTF8))
        self.inPos.setItemText(5, QtWidgets.QApplication.translate("PdsTest", "MIDDLERIGHT", None, QtWidgets.QApplication.UnicodeUTF8))
        self.inPos.setItemText(6, QtWidgets.QApplication.translate("PdsTest", "BOTTOMLEFT", None, QtWidgets.QApplication.UnicodeUTF8))
        self.inPos.setItemText(7, QtWidgets.QApplication.translate("PdsTest", "BOTTOMCENTER", None, QtWidgets.QApplication.UnicodeUTF8))
        self.inPos.setItemText(8, QtWidgets.QApplication.translate("PdsTest", "BOTTOMRIGHT", None, QtWidgets.QApplication.UnicodeUTF8))
        self.label_3.setText(QtWidgets.QApplication.translate("PdsTest", "Stop Pos", None, QtWidgets.QApplication.UnicodeUTF8))
        self.stopPos.setItemText(0, QtWidgets.QApplication.translate("PdsTest", "TOPLEFT", None, QtWidgets.QApplication.UnicodeUTF8))
        self.stopPos.setItemText(1, QtWidgets.QApplication.translate("PdsTest", "TOPCENTER", None, QtWidgets.QApplication.UnicodeUTF8))
        self.stopPos.setItemText(2, QtWidgets.QApplication.translate("PdsTest", "TOPRIGHT", None, QtWidgets.QApplication.UnicodeUTF8))
        self.stopPos.setItemText(3, QtWidgets.QApplication.translate("PdsTest", "MIDDLELEFT", None, QtWidgets.QApplication.UnicodeUTF8))
        self.stopPos.setItemText(4, QtWidgets.QApplication.translate("PdsTest", "MIDDLECENTER", None, QtWidgets.QApplication.UnicodeUTF8))
        self.stopPos.setItemText(5, QtWidgets.QApplication.translate("PdsTest", "MIDDLERIGHT", None, QtWidgets.QApplication.UnicodeUTF8))
        self.stopPos.setItemText(6, QtWidgets.QApplication.translate("PdsTest", "BOTTOMLEFT", None, QtWidgets.QApplication.UnicodeUTF8))
        self.stopPos.setItemText(7, QtWidgets.QApplication.translate("PdsTest", "BOTTOMCENTER", None, QtWidgets.QApplication.UnicodeUTF8))
        self.stopPos.setItemText(8, QtWidgets.QApplication.translate("PdsTest", "BOTTOMRIGHT", None, QtWidgets.QApplication.UnicodeUTF8))
        self.label_4.setText(QtWidgets.QApplication.translate("PdsTest", "Out Pos ", None, QtWidgets.QApplication.UnicodeUTF8))
        self.outPos.setItemText(0, QtWidgets.QApplication.translate("PdsTest", "TOPLEFT", None, QtWidgets.QApplication.UnicodeUTF8))
        self.outPos.setItemText(1, QtWidgets.QApplication.translate("PdsTest", "TOPCENTER", None, QtWidgets.QApplication.UnicodeUTF8))
        self.outPos.setItemText(2, QtWidgets.QApplication.translate("PdsTest", "TOPRIGHT", None, QtWidgets.QApplication.UnicodeUTF8))
        self.outPos.setItemText(3, QtWidgets.QApplication.translate("PdsTest", "MIDDLELEFT", None, QtWidgets.QApplication.UnicodeUTF8))
        self.outPos.setItemText(4, QtWidgets.QApplication.translate("PdsTest", "MIDDLECENTER", None, QtWidgets.QApplication.UnicodeUTF8))
        self.outPos.setItemText(5, QtWidgets.QApplication.translate("PdsTest", "MIDDLERIGHT", None, QtWidgets.QApplication.UnicodeUTF8))
        self.outPos.setItemText(6, QtWidgets.QApplication.translate("PdsTest", "BOTTOMLEFT", None, QtWidgets.QApplication.UnicodeUTF8))
        self.outPos.setItemText(7, QtWidgets.QApplication.translate("PdsTest", "BOTTOMCENTER", None, QtWidgets.QApplication.UnicodeUTF8))
        self.outPos.setItemText(8, QtWidgets.QApplication.translate("PdsTest", "BOTTOMRIGHT", None, QtWidgets.QApplication.UnicodeUTF8))
        self.label_5.setText(QtWidgets.QApplication.translate("PdsTest", "Duration", None, QtWidgets.QApplication.UnicodeUTF8))
        self.label_2.setText(QtWidgets.QApplication.translate("PdsTest", "Animation", None, QtWidgets.QApplication.UnicodeUTF8))
        self.animation.setToolTip(QtWidgets.QApplication.translate("PdsTest", "Look QEasingCurve for meanings of numbers", None, QtWidgets.QApplication.UnicodeUTF8))
        self.hideButton.setText(QtWidgets.QApplication.translate("PdsTest", "Hide Message", None, QtWidgets.QApplication.UnicodeUTF8))
        self.target.setTitle(QtWidgets.QApplication.translate("PdsTest", "PDS Parent Widget", None, QtWidgets.QApplication.UnicodeUTF8))

from PyQt5 import QtWebKit

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PdsTest = QtWidgets.QWidget()
    ui = Ui_PdsTest()
    ui.setupUi(PdsTest)
    PdsTest.show()
    sys.exit(app.exec_())

