import os
from dotenv import load_dotenv

load_dotenv()

# Player
DEFAULT_VOLUME = 50
POSITION_POLL_INTERVAL_MS = 100
POSITION_CHANGE_THRESHOLD = 0.001

# YouTube
THUMBNAIL_REQUEST_TIMEOUT = 10


YDL_OPTIONS = {
    'format': 'bestaudio',
    'quiet': True,
    'socket_timeout': 30,
    # 'proxy': os.getenv("PROXY"),

    # Оптимизация
    'extract_flat': False, # Полные данные
    'skip_download': True, # Не скачиваем, только метаданные
}