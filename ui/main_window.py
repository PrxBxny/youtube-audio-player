from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QGroupBox, QPushButton, QLabel, QLineEdit, QSlider
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon, QPixmap
from core.player import Player
from core.youtube import YouTubeExtractor

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.player = Player()
        self._connect_player_signals()
        self.extractor = None

        self.setWindowTitle("YT Audio Player")
        self.setGeometry(300, 300, 360, 400)
        self.setWindowIcon(QIcon("resources/icon.ico"))
        # self.setWindowFlags(Qt.WindowType.FramelessWindowHint)

        central = QWidget()
        self.setCentralWidget(central)
        main_layout = QHBoxLayout(central)

        layout = QVBoxLayout()
        main_layout.addLayout(layout)

        # Картинка
        self.image_label = QLabel()
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.image_label)

        self.qpixmap = QPixmap('resources/preview_new.jpg')
        self.image_label.setPixmap(self.qpixmap.scaled(280, 280, Qt.AspectRatioMode.KeepAspectRatio))

        # Поле ввода URL
        self.url_input = QLineEdit()
        self.url_input.setPlaceholderText("Вставь YouTube URL...")
        layout.addWidget(self.url_input)

        # Кнопка Add URL
        self.add_url_btn = QPushButton("▶ Add URL")
        self.add_url_btn.clicked.connect(self.on_play)
        layout.addWidget(self.add_url_btn)

        # Группируем кнопки контроля плеером (предыдущий, стоп/плей, следующий)
        player_controls_group = QGroupBox("controls")
        layout.addWidget(player_controls_group)
        # Лэйаут для группы player_controls_group
        player_controls_layout = QHBoxLayout()
        player_controls_group.setLayout(player_controls_layout)

        # Кнопка предыдущий трек
        self.previous_btn = QPushButton("⏪")
        self.previous_btn.clicked.connect(self.player.previous)
        player_controls_layout.addWidget(self.previous_btn)

        # Кнопка toggle Play/Pause
        self.toggle_play_pause_btn = QPushButton("▶")
        self.toggle_play_pause_btn.clicked.connect(self.player.toggle_play_pause)
        player_controls_layout.addWidget(self.toggle_play_pause_btn)

        # Кнопка следующий трек
        self.next_btn = QPushButton("⏩")
        self.next_btn.clicked.connect(self.player.next)
        player_controls_layout.addWidget(self.next_btn)

        # Кнопка Stop
        self.stop_btn = QPushButton("⏹")
        self.stop_btn.clicked.connect(self.player.stop)
        player_controls_layout.addWidget(self.stop_btn)

        # Кнопка Repeat
        self.repeat_btn = QPushButton("🔂")
        self.repeat_btn.clicked.connect(self.player.repeat)
        player_controls_layout.addWidget(self.repeat_btn)

        # Кнопка очистки плейлиста
        self.clear_playlist_btn = QPushButton("Clear PlayList")
        self.clear_playlist_btn.clicked.connect(self.player.clear_playlist)
        self.clear_playlist_btn.setIcon(QIcon("resources/trash.ico"))
        layout.addWidget(self.clear_playlist_btn)

        # Ползунок громкости
        self.volume_slider = QSlider(Qt.Orientation.Horizontal)
        self.volume_slider.setRange(0, 100)
        self.volume_slider.setValue(60)
        self.volume_slider.valueChanged.connect(lambda val: self.player.volume_changed(val))
        layout.addWidget(self.volume_slider)

    def _connect_player_signals(self):
        self.player.state_changed.connect(self.on_player_state_changed)

    def on_play(self):
        url = self.url_input.text()
        if url:
            self.add_url_btn.setEnabled(False)
            self.add_url_btn.setText("Загрузка...")
            # Создаем экстрактор
            self.extractor = YouTubeExtractor(url)
            self.extractor.audio_url_ready.connect(self.on_audio_ready)
            self.extractor.thumbnail_bytes_ready.connect(self.on_thumbnail_ready)
            self.extractor.error.connect(self.on_error)
            self.extractor.start()

    def on_audio_ready(self, audio_url: str):
        self.player.play_url(audio_url)
        self.add_url_btn.setEnabled(True)
        self.add_url_btn.setText("Add URL")
        self.add_url_btn.setIcon(QIcon("resources/musical-note.ico"))

    def on_error(self, error: str):
        print(f"Ошибка: {error}")
        self.add_url_btn.setEnabled(True)
        self.add_url_btn.setText("▶ Play (Ошибка!)")

    def on_thumbnail_ready(self, thumbnail_bytes: bytes):
        self.qpixmap.loadFromData(thumbnail_bytes)
        self.image_label.setPixmap(self.qpixmap.scaled(280, 280, Qt.AspectRatioMode.KeepAspectRatio))

    def on_player_state_changed(self, new_state: str):
        print(f'получен сигнал со статусом: {new_state}')

        if new_state == Player.STATE_PLAYING:
            self.toggle_play_pause_btn.setText("⏸")
        elif new_state == Player.STATE_PAUSED or new_state == Player.STATE_STOPPED:
            self.toggle_play_pause_btn.setText("▶")
