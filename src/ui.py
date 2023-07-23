from datetime import date

from PySide6 import QtUiTools
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QPushButton, QLineEdit, QComboBox, QCheckBox, QDateEdit, QMessageBox

from frmMain import Ui_frmMain
from webController import webControllerOption, webController


def show_messagebox(message):
    msgbox = QMessageBox(text=message)
    msgbox.setWindowTitle('SRT 예약 매크로')
    msgbox.setWindowFlag(Qt.WindowStaysOnTopHint, True)
    msgbox.exec()


class frmMain(QWidget, Ui_frmMain):
    # type hint
    txtID: QLineEdit
    txtPassword: QLineEdit
    dtDeparture: QDateEdit
    cboDeparture: QComboBox
    cboArrival: QComboBox
    cboTime: QComboBox
    chkSuite: QCheckBox
    btnRunMacro: QPushButton

    def __init__(self):
        super().__init__()

        # setup Ui
        self.setupUi(self)

        # set window title
        self.setWindowTitle('SRT 예약 매크로')

        # set window size
        self.setFixedSize(240, 310)

        # set window flags
        self.setWindowFlags(Qt.Window |
                            Qt.CustomizeWindowHint |
                            Qt.WindowTitleHint |
                            Qt.WindowCloseButtonHint |
                            Qt.WindowStaysOnTopHint)

        # set controls
        self.txtID = self.findChild(QLineEdit, 'txtID')
        self.txtPassword = self.findChild(QLineEdit, 'txtPassword')
        self.dtDeparture = self.findChild(QDateEdit, 'dtDeparture')
        self.cboDeparture = self.findChild(QComboBox, 'cboDeparture')
        self.cboArrival = self.findChild(QComboBox, 'cboArrival')
        self.cboTime = self.findChild(QComboBox, 'cboTime')
        self.chkSuite = self.findChild(QCheckBox, 'chkSuite')
        self.btnRunMacro = self.findChild(QPushButton, 'btnRunMacro')

        # set default value
        self.dtDeparture.setDate(date.today())
        self.cboDeparture.setCurrentText('수서')
        self.cboArrival.setCurrentText('부산')

        # connect slot
        self.btnRunMacro.clicked.connect(self.onClicked_btnRunMacro)

        # focus control
        self.txtID.setFocus()

    # on clicked run macro button
    def onClicked_btnRunMacro(self):
        user_id = self.txtID.text()
        user_password = self.txtPassword.text()
        date = self.dtDeparture.date().toString('yyyyMMdd')
        departure = self.cboDeparture.currentText()
        arrival = self.cboArrival.currentText()
        time = f'{self.cboTime.currentText()[:2]}0000'
        check_suite = self.chkSuite.isChecked()

        # webController 옵션 설정
        op = webControllerOption(date, time, departure, arrival)
        op.set_check_suite(check_suite)

        # webController 실행
        wc = webController(op)

        try:
            # 로그인
            if not wc.login(user_id, user_password):
                raise Exception('로그인에 실패하였습니다.')

            # 매크로 실행
            wc.run_macro()

            # 매크로 성공 시 메시지 띄우기
            show_messagebox(f'예약 잡기 성공!\n'
                            f'띄워진 창에서 결제를 진행해 주시기 바랍니다.\n'
                            f'(잔여석이 없다고 뜰경우 다시 매크로를 실행하여 주시기 바랍니다.')

            # 창 닫기
            self.close()
        except Exception as e:
            # 오류 발생 시 메시지 띄우고 실패
            show_messagebox(f'매크로 실행 실패\n오류내용:\n{e}')

            # webController 종료
            wc.close()
