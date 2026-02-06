# test_player.py
from PyQt6.QtWidgets import QApplication
from core.player import Player

app = QApplication([])

player = Player()

# Подключаем слушатель сигнала
def on_state_change(state):
    print(f"✅ UI получил сигнал: {state}")

player.state_changed.connect(on_state_change)
#                    ^^^^^^^ подписываемся на сигнал

# Тестируем
print("Начальное состояние:", player.state)
print("\n--- Играем тестовое аудио ---")
player.play_url("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")

import time
time.sleep(2)

print("\n--- Нажимаем pause ---")
player.pause()  # Должно поставить на паузу

time.sleep(2)

print("\n--- Нажимаем play ---")
player.play()  # Должно продолжить

input("\nНажми Enter для выхода...")