from PyQt6.QtCore import QObject
import vlc

class Player(QObject):
    def __init__(self):
        super().__init__()
        self.vlc_instance = vlc.Instance('--no-video')
        self.player = self.vlc_instance.media_player_new() # Создаем плеер
        self.list_player = self.vlc_instance.media_list_player_new() # Создаем лист плеер
        self.list_player.set_media_player(self.player) # Подключаем плеер к лист плееру

        self.playlist = self.vlc_instance.media_list_new() # Создаем плейлист
        self.list_player.set_media_list(self.playlist) # Подключаем лист плеер к плейлисту

        self.player.audio_set_volume(50)

    def play_url(self, url: str):
        media = self.vlc_instance.media_new(url)
        self.playlist.add_media(media)

        if self.player.get_state() == vlc.State.NothingSpecial:
            self.list_player.play()

    def play(self):
        self.list_player.play()

    def pause(self):
        self.list_player.pause()

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