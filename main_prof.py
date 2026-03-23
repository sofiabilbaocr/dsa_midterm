
from ll import LinkedList
# Importamos la lista hardcoded
from songs_data import canciones 

def cargar_datos_iterativamente(playlist, lista_datos):
    # Carga dinámica/iterativa: inserta cada diccionario a la LinkedList
    for cancion in lista_datos:
        playlist.append(cancion)

if __name__ == "__main__":
    mi_playlist = LinkedList()
    
    print("Playlist creada (vacía)")
    
    # Manda a llamar la función de carga pasándole la data importada
    cargar_datos_iterativamente(mi_playlist, canciones)
    
    print("Se han cargado 100 canciones exitosamente de forma iterativa.")
    
    if mi_playlist.current is not None:
         print(f"Primera canción en el nodo actual: {mi_playlist.current.data['nombre']}")