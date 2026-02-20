import sys
from pathlib import Path

# Добавляем корень проекта в путь поиска модулей
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

from PyQt6.QtWidgets import QApplication
from core.youtube import YouTubeExtractor

app = QApplication([])

def on_ready(url):
    print(f"Аудио URL: {url[:50]}...")

def thumbnail_ready(url):
    print(f"Превьюшка: {url}")

def on_error(error):
    print(f"Ошибка: {error}")

extractor = YouTubeExtractor("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
extractor.audio_url_ready.connect(on_ready)
extractor.error.connect(on_error)
extractor.thumbnail_bytes_ready.connect(thumbnail_ready)
extractor.start()

app.exec()