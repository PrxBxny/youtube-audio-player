from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QPushButton, QLineEdit
from core.player import SimplePlayer
from core.youtube import YouTubeExtractor

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.player = SimplePlayer()
        self.extractor = None

        self.setWindowTitle("Music Player MVP")
        self.setGeometry(100, 100, 400, 200)

        central = QWidget()
        self.setCentralWidget(central)
        layout = QVBoxLayout(central)

        # Поле ввода URL
        self.url_input = QLineEdit()
        self.url_input.setPlaceholderText("Вставь YouTube URL...")
        layout.addWidget(self.url_input)

        # Кнопка Play
        self.play_btn = QPushButton("▶ Play")
        self.play_btn.clicked.connect(self.on_play)
        layout.addWidget(self.play_btn)

        # Кнопка Stop
        self.stop_btn = QPushButton("⏹ Stop")
        self.stop_btn.clicked.connect(self.player.stop)
        layout.addWidget(self.stop_btn)

    def on_play(self):
        url = self.url_input.text()
        if url:
            self.play_btn.setEnabled(False)
            self.play_btn.setText("Загрузка...")
            # Создаем экстрактор
            self.extractor = YouTubeExtractor(url)
            self.extractor.audio_url_ready.connect(self.on_audio_ready)
            self.extractor.error.connect(self.on_error)
            self.extractor.start()


    def on_audio_ready(self, audio_url: str):
        self.player.play_url(audio_url)
        self.play_btn.setEnabled(True)
        self.play_btn.setText("▶ Play")

    def on_error(self, error: str):
        print(f"Ошибка: {error}")
        self.play_btn.setEnabled(True)
        self.play_btn.setText("▶ Play (Ошибка!)")