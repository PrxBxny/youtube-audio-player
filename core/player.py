from PyQt6.QtCore import QObject, pyqtSignal
import vlc

class Player(QObject):
    state_changed = pyqtSignal(str)

    STATE_STOPPED = 'stopped'
    STATE_PLAYING = 'playing'
    STATE_PAUSED = 'paused'

    def __init__(self):
        super().__init__()
        self.vlc_instance = vlc.Instance('--no-video')
        self.player = self.vlc_instance.media_player_new() # Создаем плеер
        self.list_player = self.vlc_instance.media_list_player_new() # Создаем лист плеер
        self.list_player.set_media_player(self.player) # Подключаем плеер к лист плееру

        self.playlist = self.vlc_instance.media_list_new() # Создаем плейлист
        self.list_player.set_media_list(self.playlist) # Подключаем лист плеер к плейлисту

        self.player.audio_set_volume(50)

        self._state = self.STATE_STOPPED

        self._setup_vlc_events()

    def _setup_vlc_events(self):
        event_manager = self.player.event_manager()

        event_manager.event_attach(
            vlc.EventType.MediaPlayerPlaying,
            lambda e: self._set_state(self.STATE_PLAYING)
        )

        event_manager.event_attach(
            vlc.EventType.MediaPlayerPaused,
            lambda e: self._set_state(self.STATE_PAUSED)
        )

        event_manager.event_attach(
            vlc.EventType.MediaPlayerStopped,
            lambda e: self._set_state(self.STATE_STOPPED)
        )

    def _set_state(self, new_state: str):
        print(f'_set_state меняет состояние с {self._state} на {new_state}')
        if self._state != new_state:
            self._state = new_state

            self.state_changed.emit(new_state) # emit - отправление сигнала всем слушателям
            print(f"сигнал отправлен: state_changed('{new_state}')")

    @property
    def state(self):
        return self._state

    def play_url(self, url: str):
        media = self.vlc_instance.media_new(url)
        self.playlist.add_media(media)

        if self.player.get_state() == vlc.State.NothingSpecial:
            self.list_player.play()

    def play(self):
        self.list_player.play()

    def pause(self):
        self.list_player.pause()

    def toggle_play_pause(self):
        if self.state == self.STATE_PAUSED:
            self.play()
        elif self.state == self.STATE_PLAYING:
            self.pause()

    def stop(self):
        self.list_player.stop()

    def next(self):
        self.list_player.next()

    def previous(self):
        self.list_player.previous()

    def repeat(self):
        self.list_player.set_playback_mode(vlc.PlaybackMode.loop)

    def volume_changed(self, volume: int):
        self.player.audio_set_volume(volume)

    def clear_playlist(self):
        self.stop()
        new_playlist = self.vlc_instance.media_list_new()
        self.list_player.set_media_list(new_playlist)

        self.playlist = new_playlist