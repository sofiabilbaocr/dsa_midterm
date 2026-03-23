from ll import LinkedList
from songs_data import obtener_100_canciones

def ejecutar_reproductor():
    mi_playlist = LinkedList()
    datos = obtener_100_canciones()
    
    # Carga iterativa
    for cancion in datos:
        mi_playlist.append(cancion)
        
    print("Playlist cargada exitosamente con 100 canciones.")

    continuar = "si"
    while continuar == "si":
        actual = mi_playlist.current
        
        if actual is not None:
            print("\n" + "="*45)
            print(f"REPRODUCIENDO: {actual.data['nombre']}")
            print(f"ARTISTA: {actual.data['artista']}")
            print(f"ALBUM: {actual.data['album']}")
            estado_shuffle = "ON" if mi_playlist.is_shuffle else "OFF"
            print(f"SHUFFLE: [{estado_shuffle}]")
            print("="*45)
        
        print("\n[n] Siguiente | [p] Anterior | [s] Shuffle | [q] Salir")
        opcion = input("Elige una opcion: ").lower()

        if opcion == "n":
            mi_playlist.next_song()
        elif opcion == "p":
            mi_playlist.prev_song()
        elif opcion == "s":
            mi_playlist.toggle_shuffle()
        elif opcion == "q":
            print("Saliendo del reproductor...")
            continuar = "no"
        else:
            print(f"\n'{opcion}' no es una letra valida. Intentalo de nuevo.")

if __name__ == "__main__":
    ejecutar_reproductor()