import sys
import ctypes
from PyQt6.QtWidgets import QApplication
from ui.main_window import MainWindow
from ui.themes.dark_themes import *

if __name__ == '__main__':
    # Идентификатор для объединения всех процессов py, в одну группу, чтобы подхватить иконку
    myappid = 'prxbxny.youtube_audio_player'
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

    app = QApplication(sys.argv)
    app.setStyleSheet(EXTRA_DARK_THEME)

    window = MainWindow()
    window.show()
    sys.exit(app.exec())