from PyQt6.QtCore import QThread, pyqtSignal
import yt_dlp, requests

class YouTubeExtractor(QThread):
    audio_url_ready = pyqtSignal(str)  # Сигнал с URL
    thumbnail_bytes_ready = pyqtSignal(bytes) # Сигнал для превью
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
                # получаем и передаем ссылку на аудио
                audio_url = info['url']
                self.audio_url_ready.emit(audio_url)
                # Получаем и передаем ссылку на превью
                thumbnail_url = info.get('thumbnail')
                response = requests.get(thumbnail_url)
                self.thumbnail_bytes_ready.emit(response.content)


        except Exception as e:
            self.error.emit(str(e))