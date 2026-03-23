from ll import LinkedList
from songs_data import canciones
from memory_profiler import profile
import timeit

# 1. PERFILAMIENTO DE MEMORIA
@profile
def perfilar_memoria():
    playlist_memoria = LinkedList()
    
    # Carga iterativa/dinámica de la data importada
    for cancion in canciones:
        playlist_memoria.append(cancion)
        
    return "Carga completada"


# 2. PERFILAMIENTO DE TIEMPO
def perfilar_tiempo():
    playlist_tiempo = LinkedList()
    
    # Carga iterativa/dinámica
    for cancion in canciones:
        playlist_tiempo.append(cancion)

if __name__ == "__main__":
    print("=" * 50)
    print(" INICIANDO PERFILAMIENTO DE MEMORIA ")
    print("=" * 50)
    # Al llamar esta función, se imprimirá la tabla de consumo MB a MB
    perfilar_memoria()
    
    print("\n" + "=" * 50)
    print(" INICIANDO PERFILAMIENTO DE TIEMPO ")
    print("=" * 50)
    # Ejecutamos la carga 500 veces para tener un promedio confiable
    tiempo_total = timeit.timeit(perfilar_tiempo, number=500)
    
    print(f"El tiempo total para 500 ejecuciones fue: {tiempo_total:.5f} segundos")
    print(f"El tiempo promedio por ejecucion (cargar 100 canciones) fue: {tiempo_total / 500:.6f} segundos")