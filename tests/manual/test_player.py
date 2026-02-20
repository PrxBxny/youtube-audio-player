import sys
from pathlib import Path

# Добавляем корень проекта в путь поиска модулей
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

from core.player import Player

player = Player()
# Любая прямая ссылка на аудио для теста
player.play_url("file:///C:/Users/_/Downloads/OrchestralMusic.mp3")
input("Нажми Enter чтобы остановить...")
player.stop()