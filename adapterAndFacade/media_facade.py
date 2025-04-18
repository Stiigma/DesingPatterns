from media_adapter import MediaAdapter

# Patrón Fachada: oculta la complejidad del sistema
class MediaFacade:
    def play_media(self, media_type, filename):
        adapter = MediaAdapter(media_type)
        adapter.play(filename)
