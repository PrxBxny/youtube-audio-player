from PyQt6.QtCore import QThread, pyqtSignal
import yt_dlp

class YouTubeExtractor(QThread):
    audio_url_ready = pyqtSignal(str)  # Сигнал с URL
    error = pyqtSignal(str)

    def __init__(self, youtube_url: str):
        super().__init__()
        self.youtube_url = youtube_url

    def run(self):
        try:
            ydl_opts = {
                'format': 'bestaudio',
                'quiet': True,
                'socket_timeout': 30,

                # Оптимизация
                'extract_flat': False, # Полные данные
                'skip_download': True, # Не скачиваем, только метаданные
            }

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(self.youtube_url, download=False)
                audio_url = info['url']
                self.audio_url_ready.emit(audio_url)

        except Exception as e:
            self.error.emit(str(e))