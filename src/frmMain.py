# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'frmMain.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateEdit,
    QGroupBox, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QWidget)

class Ui_frmMain(object):
    def setupUi(self, frmMain):
        if not frmMain.objectName():
            frmMain.setObjectName(u"frmMain")
        frmMain.resize(240, 310)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(frmMain.sizePolicy().hasHeightForWidth())
        frmMain.setSizePolicy(sizePolicy)
        self.grpReservationInfo = QGroupBox(frmMain)
        self.grpReservationInfo.setObjectName(u"grpReservationInfo")
        self.grpReservationInfo.setGeometry(QRect(10, 100, 220, 171))
        self.cboDeparture = QComboBox(self.grpReservationInfo)
        self.cboDeparture.addItem("")
        self.cboDeparture.addItem("")
        self.cboDeparture.addItem("")
        self.cboDeparture.addItem("")
        self.cboDeparture.addItem("")
        self.cboDeparture.addItem("")
        self.cboDeparture.addItem("")
        self.cboDeparture.addItem("")
        self.cboDeparture.addItem("")
        self.cboDeparture.addItem("")
        self.cboDeparture.addItem("")
        self.cboDeparture.addItem("")
        self.cboDeparture.addItem("")
        self.cboDeparture.addItem("")
        self.cboDeparture.addItem("")
        self.cboDeparture.addItem("")
        self.cboDeparture.addItem("")
        self.cboDeparture.addItem("")
        self.cboDeparture.setObjectName(u"cboDeparture")
        self.cboDeparture.setGeometry(QRect(80, 50, 120, 22))
        self.cboDeparture.setEditable(False)
        self.lblDeparture = QLabel(self.grpReservationInfo)
        self.lblDeparture.setObjectName(u"lblDeparture")
        self.lblDeparture.setGeometry(QRect(10, 50, 60, 16))
        self.lblDeparture.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lblArrival = QLabel(self.grpReservationInfo)
        self.lblArrival.setObjectName(u"lblArrival")
        self.lblArrival.setGeometry(QRect(10, 80, 60, 16))
        self.lblArrival.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lblTime = QLabel(self.grpReservationInfo)
        self.lblTime.setObjectName(u"lblTime")
        self.lblTime.setGeometry(QRect(10, 110, 60, 16))
        self.lblTime.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.cboTime = QComboBox(self.grpReservationInfo)
        self.cboTime.addItem("")
        self.cboTime.addItem("")
        self.cboTime.addItem("")
        self.cboTime.addItem("")
        self.cboTime.addItem("")
        self.cboTime.addItem("")
        self.cboTime.addItem("")
        self.cboTime.addItem("")
        self.cboTime.addItem("")
        self.cboTime.addItem("")
        self.cboTime.addItem("")
        self.cboTime.addItem("")
        self.cboTime.setObjectName(u"cboTime")
        self.cboTime.setGeometry(QRect(80, 110, 120, 22))
        self.chkSuite = QCheckBox(self.grpReservationInfo)
        self.chkSuite.setObjectName(u"chkSuite")
        self.chkSuite.setGeometry(QRect(120, 140, 76, 20))
        self.chkSuite.setChecked(True)
        self.chkSuite.setTristate(False)
        self.cboArrival = QComboBox(self.grpReservationInfo)
        self.cboArrival.addItem("")
        self.cboArrival.addItem("")
        self.cboArrival.addItem("")
        self.cboArrival.addItem("")
        self.cboArrival.addItem("")
        self.cboArrival.addItem("")
        self.cboArrival.addItem("")
        self.cboArrival.addItem("")
        self.cboArrival.addItem("")
        self.cboArrival.addItem("")
        self.cboArrival.addItem("")
        self.cboArrival.addItem("")
        self.cboArrival.addItem("")
        self.cboArrival.addItem("")
        self.cboArrival.addItem("")
        self.cboArrival.addItem("")
        self.cboArrival.addItem("")
        self.cboArrival.addItem("")
        self.cboArrival.setObjectName(u"cboArrival")
        self.cboArrival.setGeometry(QRect(80, 80, 120, 22))
        self.lblDate = QLabel(self.grpReservationInfo)
        self.lblDate.setObjectName(u"lblDate")
        self.lblDate.setGeometry(QRect(10, 20, 60, 16))
        self.lblDate.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.dtDeparture = QDateEdit(self.grpReservationInfo)
        self.dtDeparture.setObjectName(u"dtDeparture")
        self.dtDeparture.setGeometry(QRect(80, 20, 120, 22))
        self.grpAccount = QGroupBox(frmMain)
        self.grpAccount.setObjectName(u"grpAccount")
        self.grpAccount.setGeometry(QRect(10, 10, 220, 82))
        self.txtID = QLineEdit(self.grpAccount)
        self.txtID.setObjectName(u"txtID")
        self.txtID.setGeometry(QRect(80, 20, 120, 22))
        self.lblID = QLabel(self.grpAccount)
        self.lblID.setObjectName(u"lblID")
        self.lblID.setGeometry(QRect(10, 20, 60, 16))
        self.lblID.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lblPassword = QLabel(self.grpAccount)
        self.lblPassword.setObjectName(u"lblPassword")
        self.lblPassword.setGeometry(QRect(10, 50, 60, 16))
        self.lblPassword.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.txtPassword = QLineEdit(self.grpAccount)
        self.txtPassword.setObjectName(u"txtPassword")
        self.txtPassword.setGeometry(QRect(80, 50, 120, 22))
        self.btnRunMacro = QPushButton(frmMain)
        self.btnRunMacro.setObjectName(u"btnRunMacro")
        self.btnRunMacro.setGeometry(QRect(140, 280, 90, 24))
        QWidget.setTabOrder(self.txtID, self.txtPassword)
        QWidget.setTabOrder(self.txtPassword, self.cboDeparture)
        QWidget.setTabOrder(self.cboDeparture, self.cboArrival)
        QWidget.setTabOrder(self.cboArrival, self.cboTime)
        QWidget.setTabOrder(self.cboTime, self.chkSuite)
        QWidget.setTabOrder(self.chkSuite, self.btnRunMacro)

        self.retranslateUi(frmMain)

        QMetaObject.connectSlotsByName(frmMain)
    # setupUi

    def retranslateUi(self, frmMain):
        frmMain.setWindowTitle(QCoreApplication.translate("frmMain", u"SRT \uc608\uc57d \ub9e4\ud06c\ub85c", None))
        self.grpReservationInfo.setTitle(QCoreApplication.translate("frmMain", u"\uc608\uc57d\uc815\ubcf4", None))
        self.cboDeparture.setItemText(0, QCoreApplication.translate("frmMain", u"\uc218\uc11c", None))
        self.cboDeparture.setItemText(1, QCoreApplication.translate("frmMain", u"\ub3d9\ud0c4", None))
        self.cboDeparture.setItemText(2, QCoreApplication.translate("frmMain", u"\ud3c9\ud0dd\uc9c0\uc81c", None))
        self.cboDeparture.setItemText(3, QCoreApplication.translate("frmMain", u"\ucc9c\uc548\uc544\uc0b0", None))
        self.cboDeparture.setItemText(4, QCoreApplication.translate("frmMain", u"\uc624\uc1a1", None))
        self.cboDeparture.setItemText(5, QCoreApplication.translate("frmMain", u"\ub300\uc804", None))
        self.cboDeparture.setItemText(6, QCoreApplication.translate("frmMain", u"\uae40\ucc9c(\uad6c\ubbf8)", None))
        self.cboDeparture.setItemText(7, QCoreApplication.translate("frmMain", u"\uc11c\ub300\uad6c", None))
        self.cboDeparture.setItemText(8, QCoreApplication.translate("frmMain", u"\ub3d9\ub300\uad6c", None))
        self.cboDeparture.setItemText(9, QCoreApplication.translate("frmMain", u"\uc2e0\uacbd\uc8fc", None))
        self.cboDeparture.setItemText(10, QCoreApplication.translate("frmMain", u"\uc6b8\uc0b0(\ud1b5\ub3c4\uc0ac)", None))
        self.cboDeparture.setItemText(11, QCoreApplication.translate("frmMain", u"\ubd80\uc0b0", None))
        self.cboDeparture.setItemText(12, QCoreApplication.translate("frmMain", u"\uacf5\uc8fc", None))
        self.cboDeparture.setItemText(13, QCoreApplication.translate("frmMain", u"\uc775\uc0b0", None))
        self.cboDeparture.setItemText(14, QCoreApplication.translate("frmMain", u"\uc815\uc74d", None))
        self.cboDeparture.setItemText(15, QCoreApplication.translate("frmMain", u"\uad11\uc8fc\uc1a1\uc815", None))
        self.cboDeparture.setItemText(16, QCoreApplication.translate("frmMain", u"\ub098\uc8fc", None))
        self.cboDeparture.setItemText(17, QCoreApplication.translate("frmMain", u"\ubaa9\ud3ec", None))

        self.lblDeparture.setText(QCoreApplication.translate("frmMain", u"\ucd9c\ubc1c\uc5ed :", None))
        self.lblArrival.setText(QCoreApplication.translate("frmMain", u"\ub3c4\ucc29\uc5ed :", None))
        self.lblTime.setText(QCoreApplication.translate("frmMain", u"\uc2dc\uac04\ub300 :", None))
        self.cboTime.setItemText(0, QCoreApplication.translate("frmMain", u"00\uc2dc \uc774\ud6c4", None))
        self.cboTime.setItemText(1, QCoreApplication.translate("frmMain", u"02\uc2dc \uc774\ud6c4", None))
        self.cboTime.setItemText(2, QCoreApplication.translate("frmMain", u"04\uc2dc \uc774\ud6c4", None))
        self.cboTime.setItemText(3, QCoreApplication.translate("frmMain", u"06\uc2dc \uc774\ud6c4", None))
        self.cboTime.setItemText(4, QCoreApplication.translate("frmMain", u"08\uc2dc \uc774\ud6c4", None))
        self.cboTime.setItemText(5, QCoreApplication.translate("frmMain", u"10\uc2dc \uc774\ud6c4", None))
        self.cboTime.setItemText(6, QCoreApplication.translate("frmMain", u"12\uc2dc \uc774\ud6c4", None))
        self.cboTime.setItemText(7, QCoreApplication.translate("frmMain", u"14\uc2dc \uc774\ud6c4", None))
        self.cboTime.setItemText(8, QCoreApplication.translate("frmMain", u"16\uc2dc \uc774\ud6c4", None))
        self.cboTime.setItemText(9, QCoreApplication.translate("frmMain", u"18\uc2dc \uc774\ud6c4", None))
        self.cboTime.setItemText(10, QCoreApplication.translate("frmMain", u"20\uc2dc \uc774\ud6c4", None))
        self.cboTime.setItemText(11, QCoreApplication.translate("frmMain", u"22\uc2dc \uc774\ud6c4", None))

        self.chkSuite.setText(QCoreApplication.translate("frmMain", u"\ud2b9\uc2e4 \ud3ec\ud568", None))
        self.cboArrival.setItemText(0, QCoreApplication.translate("frmMain", u"\uc218\uc11c", None))
        self.cboArrival.setItemText(1, QCoreApplication.translate("frmMain", u"\ub3d9\ud0c4", None))
        self.cboArrival.setItemText(2, QCoreApplication.translate("frmMain", u"\ud3c9\ud0dd\uc9c0\uc81c", None))
        self.cboArrival.setItemText(3, QCoreApplication.translate("frmMain", u"\ucc9c\uc548\uc544\uc0b0", None))
        self.cboArrival.setItemText(4, QCoreApplication.translate("frmMain", u"\uc624\uc1a1", None))
        self.cboArrival.setItemText(5, QCoreApplication.translate("frmMain", u"\ub300\uc804", None))
        self.cboArrival.setItemText(6, QCoreApplication.translate("frmMain", u"\uae40\ucc9c(\uad6c\ubbf8)", None))
        self.cboArrival.setItemText(7, QCoreApplication.translate("frmMain", u"\uc11c\ub300\uad6c", None))
        self.cboArrival.setItemText(8, QCoreApplication.translate("frmMain", u"\ub3d9\ub300\uad6c", None))
        self.cboArrival.setItemText(9, QCoreApplication.translate("frmMain", u"\uc2e0\uacbd\uc8fc", None))
        self.cboArrival.setItemText(10, QCoreApplication.translate("frmMain", u"\uc6b8\uc0b0(\ud1b5\ub3c4\uc0ac)", None))
        self.cboArrival.setItemText(11, QCoreApplication.translate("frmMain", u"\ubd80\uc0b0", None))
        self.cboArrival.setItemText(12, QCoreApplication.translate("frmMain", u"\uacf5\uc8fc", None))
        self.cboArrival.setItemText(13, QCoreApplication.translate("frmMain", u"\uc775\uc0b0", None))
        self.cboArrival.setItemText(14, QCoreApplication.translate("frmMain", u"\uc815\uc74d", None))
        self.cboArrival.setItemText(15, QCoreApplication.translate("frmMain", u"\uad11\uc8fc\uc1a1\uc815", None))
        self.cboArrival.setItemText(16, QCoreApplication.translate("frmMain", u"\ub098\uc8fc", None))
        self.cboArrival.setItemText(17, QCoreApplication.translate("frmMain", u"\ubaa9\ud3ec", None))

        self.lblDate.setText(QCoreApplication.translate("frmMain", u"\ub0a0\uc9dc :", None))
        self.grpAccount.setTitle(QCoreApplication.translate("frmMain", u"\uacc4\uc815 \uc815\ubcf4", None))
        self.lblID.setText(QCoreApplication.translate("frmMain", u"E-Mail :", None))
        self.lblPassword.setText(QCoreApplication.translate("frmMain", u"\ube44\ubc00\ubc88\ud638 :", None))
        self.btnRunMacro.setText(QCoreApplication.translate("frmMain", u"\ub9e4\ud06c\ub85c \uc2e4\ud589", None))
    # retranslateUi

