from media_facade import MediaFacade

def main():
    facade = MediaFacade()

    # Comentarios explicativos
    print("Prueba con audio:")
    facade.play_media("audio", "cancion.mp3")

    print("\nPrueba con video:")
    facade.play_media("video", "pelicula.mp4")

    print("\nPrueba con formato no soportado:")
    facade.play_media("imagen", "foto.png")

if __name__ == "__main__":
    main()
