

#dccionario de canciones actuales
canciones_base = {
    "c1": {"nombre": "Texas Hold 'Em", "artista": "Beyoncé", "album": "Cowboy Carter"},
    "c2": {"nombre": "Beautiful Things", "artista": "Benson Boone", "album": "Fireworks & Rollerblades"},
    "c3": {"nombre": "Lose Control", "artista": "Teddy Swims", "album": "I've Tried Everything But Therapy"},
    "c4": {"nombre": "Cruel Summer", "artista": "Taylor Swift", "album": "Lover"},
    "c5": {"nombre": "Greedy", "artista": "Tate McRae", "album": "Think Later"},
    "c6": {"nombre": "Paint The Town Red", "artista": "Doja Cat", "album": "Scarlet"},
    "c7": {"nombre": "Water", "artista": "Tyla", "album": "Tyla"},
    "c8": {"nombre": "La Diabla", "artista": "Xavi", "album": "Single"},
    "c9": {"nombre": "Monaco", "artista": "Bad Bunny", "album": "Nadie Sabe Lo Que Va A Pasar Mañana"},
    "c10": {"nombre": "QLONA", "artista": "Karol G", "album": "Mañana Será Bonito"}
}

def obtener_100_canciones():
    lista_100 = []
    #Itera 10 veces sobre nuestro diccionario de 10 canciones para llegar a 100
    for i in range(10):
        #.values() extrae solo los diccionarios con la info de la canción
        for data in canciones_base.values():
            #agrega un diferenciador al nombre para que sean 100 canciones únicas
            cancion_dinamica = {
                "nombre": f"{data['nombre']} (Mix {i+1})",
                "artista": data["artista"],
                "album": data["album"]
            }
            lista_100.append(cancion_dinamica)
    
    return lista_100