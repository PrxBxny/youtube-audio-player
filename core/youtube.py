from PyQt6.QtCore import QThread, pyqtSignal
from core.config import YDL_OPTIONS, THUMBNAIL_REQUEST_TIMEOUT
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
            with yt_dlp.YoutubeDL(YDL_OPTIONS) as ydl:
                info = ydl.extract_info(self.youtube_url, download=False)

                # получаем и передаем ссылку на аудио
                audio_url = info['url']
                if not audio_url:
                    raise ValueError("Не удалось получить аудио URL")
                self.audio_url_ready.emit(audio_url)

                # Получаем и передаем ссылку на превью
                thumbnail_url = info.get('thumbnail')
                if thumbnail_url:
                    try:
                        response = requests.get(
                            thumbnail_url,
                            timeout=10,
                            stream=True # Не загружаем сразу все в память
                        )
                        response.raise_for_status()  # Проверка статуса
                        self.thumbnail_bytes_ready.emit(response.content)
                    except Exception as e:
                        self.error.emit(f"YouTube extraction error: {str(e)}")

                # Получаем

        except Exception as e:
            self.error.emit(str(e))