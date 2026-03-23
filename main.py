
from ll import LinkedList
from songs_data import obtener_100_canciones

def cargar_playlist(playlist):
    #1. Obtiene la data del archivo separado
    datos = obtener_100_canciones()
    
    #2. Inserta de forma iterativa
    for cancion in datos:
        playlist.append(cancion)

if __name__ == "__main__":
    mi_playlist = LinkedList()
    print("Playlist creada (vacía)")
    
    # Llenamos la playlist
    cargar_playlist(mi_playlist)
    
    print("¡Se han cargado 100 canciones!")
    
    if mi_playlist.current is not None:
        print(f"Primera canción en lista: {mi_playlist.current.data['nombre']}")