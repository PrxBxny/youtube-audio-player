from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QGroupBox, QPushButton, QLabel, QLineEdit, QSlider
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QIcon, QPixmap
from core import Player, YouTubeExtractor
import vlc


WINDOW_GEOMETRY = (300, 300, 340, 400)
TIME_SLIDER_SCALE = 1000
THUMBNAIL_SIZE = 280
DEFAULT_VOLUME = 50

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.player = Player()
        self._connect_player_signals()
        self.extractor = None
        self.is_extracting = False

        self.setWindowTitle("YT Audio Player")
        self.setGeometry(*WINDOW_GEOMETRY)
        self.setWindowIcon(QIcon("resources/negative_icon.ico"))

        central = QWidget()
        self.setCentralWidget(central)
        main_layout = QHBoxLayout(central)

        layout = QVBoxLayout()
        main_layout.addLayout(layout)

        # Картинка
        self.image_label = QLabel()
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.image_label)

        self.qpixmap = QPixmap('resources/preview.jpg')
        self.image_label.setPixmap(self.qpixmap.scaled(THUMBNAIL_SIZE, THUMBNAIL_SIZE, Qt.AspectRatioMode.KeepAspectRatio))

        # Отдельный виджет для duration бара
        duration_widget = QWidget()
        layout.addWidget(duration_widget)
        # Лэйаут для таймбара
        duration_layout = QHBoxLayout()
        duration_widget.setLayout(duration_layout)
        duration_widget.setMaximumHeight(50)

        # Слайдер продолжительности трека
        self.time_slider = QSlider(Qt.Orientation.Horizontal)
        self.time_slider.setRange(0, TIME_SLIDER_SCALE)
        self.time_slider.setValue(0)
        self._connect_slider_signals()
        duration_layout.addWidget(self.time_slider)

        # Текст продолжительности трека
        self.time_label = QLabel("00:00/00:00")
        self.time_label.setStyleSheet("font-size: 12px;")
        duration_layout.addWidget(self.time_label)

        # Поле ввода URL
        self.url_input = QLineEdit()
        self.url_input.setPlaceholderText("Enter YouTube URL...")
        self.url_input.setStyleSheet("font-size: 12px;")
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
        self.repeat_btn.clicked.connect(self.player.switch_playback_mode)
        player_controls_layout.addWidget(self.repeat_btn)

        # Кнопка очистки плейлиста
        self.clear_playlist_btn = QPushButton("Clear PlayList")
        self.clear_playlist_btn.clicked.connect(self.player.clear_playlist)
        self.clear_playlist_btn.setIcon(QIcon("resources/negative_trash.ico"))
        layout.addWidget(self.clear_playlist_btn)

        # Ползунок громкости
        self.volume_slider = QSlider(Qt.Orientation.Horizontal)
        self.volume_slider.setRange(0, 100)
        self.volume_slider.setValue(DEFAULT_VOLUME)
        self.volume_slider.valueChanged.connect(lambda val: self.player.volume_changed(val))
        layout.addWidget(self.volume_slider)

    def _connect_player_signals(self):
        self.player.state_changed.connect(self.on_player_state_changed)
        self.player.playback_changed.connect(self.on_playback_mode_changed)
        self.player.position_changed.connect(self.on_position_changed)

    def on_play(self):
        url = self.url_input.text()
        if not url:
            return

        if 'youtube.com' not in url and 'youtu.be' not in url:
            self.on_error("It's not YouTube URL!")
            return

        if self.is_extracting:
            print("Loading, wait...")
            return

        if self.extractor and self.extractor.isRunning():
            self.extractor.quit()  # Просим завершиться
            self.extractor.wait(1000)  # ждем секунду

        self.is_extracting = True
        self.add_url_btn.setEnabled(False)
        self.add_url_btn.setText("Loading...")
        # Создаем экстрактор
        self.extractor = YouTubeExtractor(url)
        self._connect_extractor_signals()
        self.extractor.start()

    def _connect_extractor_signals(self):
        self.extractor.audio_url_ready.connect(self.on_audio_ready)
        self.extractor.thumbnail_bytes_ready.connect(self.on_thumbnail_ready)
        self.extractor.error.connect(self.on_error)
        self.extractor.finished.connect(self.on_extraction_finished)

    def on_extraction_finished(self):
        """Вызывается когда поток завершился"""
        self.is_extracting = False
        self.add_url_btn.setEnabled(True)
        self.add_url_btn.setText("Add URL")

    def on_audio_ready(self, audio_url: str):
        self.player.play_url(audio_url)
        self.add_url_btn.setEnabled(True)
        self.add_url_btn.setText("Add URL")
        self.add_url_btn.setIcon(QIcon("resources/negative_musical-note.ico"))

    def on_error(self, error: str):
        print(f"Error: {error}")
        self.add_url_btn.setEnabled(True)
        self.add_url_btn.setText("▶ Play (Erroe!)")

    def on_thumbnail_ready(self, thumbnail_bytes: bytes):
        self.qpixmap.loadFromData(thumbnail_bytes)
        self.image_label.setPixmap(self.qpixmap.scaled(THUMBNAIL_SIZE, THUMBNAIL_SIZE, Qt.AspectRatioMode.KeepAspectRatio))

    def on_player_state_changed(self, new_state: str):
        print(f'получен сигнал со статусом: {new_state}')

        if new_state == Player.STATE_PLAYING:
            btn_text = "⏸"
        elif new_state == Player.STATE_PAUSED or new_state == Player.STATE_STOPPED:
            btn_text = "▶"
        self.toggle_play_pause_btn.setText(btn_text)

    def on_playback_mode_changed(self, new_mode: vlc.PlaybackMode):
        print(f'получен сигнал с модом: {new_mode}')

        if new_mode == Player.PLAYBACK_DEFAULT:
            btn_text = "🔁"
        elif new_mode == Player.PLAYBACK_LOOP:
            btn_text = "🔂"
        elif new_mode == Player.PLAYBACK_REPEAT:
            btn_text = "↩"

        self.repeat_btn.setText(btn_text)

    def _connect_slider_signals(self):
        self.slider_is_being_dragged = False
        self.time_slider.sliderPressed.connect(self.on_slider_pressed)
        self.time_slider.sliderReleased.connect(self.on_slider_released)

    def on_slider_pressed(self):
        self.slider_is_being_dragged = True

    def on_slider_released(self):
        self.slider_is_being_dragged = False

        new_position = self.time_slider.value() / TIME_SLIDER_SCALE
        self.player.player.set_position(new_position)

    def on_position_changed(self, pos: float):
        if not self.slider_is_being_dragged:
            # Меняем позицию слайдера
            new_value = int(pos * TIME_SLIDER_SCALE)
            self.time_slider.setValue(new_value)

        # # Меняем текст
        end_duration_formated = self.player.get_duration(formated = True) # Конец трека

        duration_secs = self.player.get_duration(formated = False) # Вся продолжительность
        current_duration_secs = int(duration_secs * pos) # Текущяя продолжительность
        mins, secs = divmod(current_duration_secs, 60)
        currnet_duration_formated = f"{mins:02}:{secs:02}" # Текущее время

        new_text = f'{currnet_duration_formated}/{end_duration_formated}'
        self.time_label.setText(new_text)
