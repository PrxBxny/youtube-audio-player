from core.player import SimplePlayer

player = SimplePlayer()
# Любая прямая ссылка на аудио для теста
player.play_url("file:///C:/Users/_/Downloads/OrchestralMusic.mp3")
input("Нажми Enter чтобы остановить...")
player.stop()