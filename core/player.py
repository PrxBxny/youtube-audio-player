from PyQt6.QtCore import QObject
import vlc

class SimplePlayer(QObject):
    def __init__(self):
        super().__init__()
        self.vlc_instance = vlc.Instance('--no-video')
        self.player = self.vlc_instance.media_player_new()
        self.player.audio_set_volume(50)

    def play_url(self, url: str):
        media = self.vlc_instance.media_new(url)
        self.player.set_media(media)
        self.player.play()

    def pause(self):
        self.player.pause()

    def stop(self):
        self.player.stop()