import sys
from pathlib import Path

# Добавляем корень проекта в путь поиска модулей
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

# test_player.py
from PyQt6.QtWidgets import QApplication
from core.player import Player
import time

app = QApplication([])

player = Player()

# Подключаем слушатель сигнала
def on_state_change(state):
    print(f"✅ UI получил сигнал: {state}")

player.position_changed.connect(on_state_change)
#                    ^^^^^^^ подписываемся на сигнал

# Тестируем
print("\n--- Играем тестовое аудио ---")
player.play_url("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")
