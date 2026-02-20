import sys
import ctypes
import platform
from PyQt6.QtWidgets import QApplication
from ui import MainWindow
from ui.themes import apply_dark_theme

if __name__ == '__main__':
    app = QApplication(sys.argv)

    if platform.system() == 'Windows':
        try:
            # Идентификатор для объединения всех процессов py, в одну группу, чтобы подхватить иконку
            myappid = 'prxbxny.youtube_audio_player'
            ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
        except Exception as e:
            print(f'Не удалось установить AppUserModelID: {e}')

    window = MainWindow()
    apply_dark_theme(window)
    window.show()

    sys.exit(app.exec())