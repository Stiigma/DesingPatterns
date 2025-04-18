from media_facade import MediaFacade

class TestMediaFacade:

    def test_audio_playback(self, capsys):
        facade = MediaFacade()
        facade.play_media("audio", "test_audio.mp3")
        captured = capsys.readouterr()
        assert "Reproduciendo archivo de audio: test_audio.mp3" in captured.out

    def test_video_playback(self, capsys):
        facade = MediaFacade()
        facade.play_media("video", "test_video.mp4")
        captured = capsys.readouterr()
        assert "Iniciando video: test_video.mp4" in captured.out

    def test_unsupported_format(self, capsys):
        facade = MediaFacade()
        facade.play_media("otro", "archivo.xyz")
        captured = capsys.readouterr()
        assert "Formato no compatible." in captured.out
