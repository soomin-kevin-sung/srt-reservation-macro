from PySide6.QtWidgets import QApplication
import ui


def main():
    app = QApplication([])

    main_window = ui.frmMain()
    main_window.show()

    app.exec()


if __name__ == '__main__':
    main()
