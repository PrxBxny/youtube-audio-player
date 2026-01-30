from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QSlider
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
from core.player import Player
from core.youtube import YouTubeExtractor

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.player = Player()
        self.extractor = None

        self.setWindowTitle("YT Audio Player")
        self.setGeometry(300, 300, 400, 150)
        self.setWindowIcon(QIcon("resources/icon.ico"))

        central = QWidget()
        self.setCentralWidget(central)
        layout = QVBoxLayout(central)

        # Поле ввода URL
        self.url_input = QLineEdit()
        self.url_input.setPlaceholderText("Вставь YouTube URL...")
        layout.addWidget(self.url_input)

        # Кнопка Add URL
        self.add_url_btn = QPushButton("▶ Add URL")
        self.add_url_btn.clicked.connect(self.on_play)
        layout.addWidget(self.add_url_btn)

        # Кнопка Play
        self.play_btn = QPushButton("▶ Play")
        self.play_btn.clicked.connect(self.player.play)
        layout.addWidget(self.play_btn)

        # Кнопка Pause
        self.pause_btn = QPushButton("⏸ Pause")
        self.pause_btn.clicked.connect(self.player.pause)
        layout.addWidget(self.pause_btn)

        # Кнопка Stop
        self.stop_btn = QPushButton("⏹ Stop")
        self.stop_btn.clicked.connect(self.player.stop)
        layout.addWidget(self.stop_btn)

        # Кнопка следующий трек
        self.next_btn = QPushButton("⏩ Next")
        self.next_btn.clicked.connect(self.player.next)
        layout.addWidget(self.next_btn)

        # Кнопка предыдущий трек
        self.previous_btn = QPushButton("⏪ Previous")
        self.previous_btn.clicked.connect(self.player.previous)
        layout.addWidget(self.previous_btn)

        # Кнопка Repeat
        self.repeat_btn = QPushButton("🔂 Repeat")
        self.repeat_btn.clicked.connect(self.player.repeat)
        layout.addWidget(self.repeat_btn)

        # Кнопка очистки плейлиста
        self.clear_playlist_btn = QPushButton("🆓 Clear PlayList")
        self.clear_playlist_btn.clicked.connect(self.player.clear_playlist)
        layout.addWidget(self.clear_playlist_btn)

        # Ползунок громкости
        self.volume_slider = QSlider(Qt.Orientation.Horizontal)
        self.volume_slider.setRange(0, 100)
        self.volume_slider.setValue(60)
        self.volume_slider.valueChanged.connect(lambda val: self.player.volume_changed(val))
        layout.addWidget(self.volume_slider)

    def on_play(self):
        url = self.url_input.text()
        if url:
            self.add_url_btn.setEnabled(False)
            self.add_url_btn.setText("Загрузка...")
            # Создаем экстрактор
            self.extractor = YouTubeExtractor(url)
            self.extractor.audio_url_ready.connect(self.on_audio_ready)
            self.extractor.error.connect(self.on_error)
            self.extractor.start()

    def on_audio_ready(self, audio_url: str):
        self.player.play_url(audio_url)
        self.add_url_btn.setEnabled(True)
        self.add_url_btn.setText("▶ Add URL")

    def on_error(self, error: str):
        print(f"Ошибка: {error}")
        self.add_url_btn.setEnabled(True)
        self.add_url_btn.setText("▶ Play (Ошибка!)")