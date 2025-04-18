from audio_player import AudioPlayer
from video_player import VideoPlayer

# Patrón Adaptador: adaptamos diferentes interfaces a una común
class MediaAdapter:
    def __init__(self, media_type):
        if media_type == "audio":
            self.player = AudioPlayer()
        elif media_type == "video":
            self.player = VideoPlayer()
        else:
            self.player = None

    def play(self, filename):
        if isinstance(self.player, AudioPlayer):
            self.player.play_audio(filename)
        elif isinstance(self.player, VideoPlayer):
            self.player.start_video(filename)
        else:
            print("Formato no compatible.")
