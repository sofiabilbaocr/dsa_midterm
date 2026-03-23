# main.py
from ll import LinkedList
from songs_data import obtener_100_canciones
from memory_profiler import profile
import timeit


# 1. PERFILAMIENTO DE MEMORIA
@profile
def perfilar_carga_memoria():
    playlist_memoria = LinkedList()
    datos = obtener_100_canciones()
    
    # Carga iterativa
    for cancion in datos:
        playlist_memoria.append(cancion)
        
    return "Carga de memoria completada"

# 2.PERFILAMIENTO DE TIEMPO

def perfilar_carga_tiempo():
    playlist_tiempo = LinkedList()
    datos = obtener_100_canciones()
    
    #Carga iterativa
    for cancion in datos:
        playlist_tiempo.append(cancion)

if __name__ == "__main__":
    print("="*50)
    print(" INICIANDO PERFILAMIENTO DE MEMORIA ")
    print("="*50)
    #Al llamar esta función, el decorador @profile imprimirá la tabla
    perfilar_carga_memoria()
    
    print("\n" + "="*50)
    print(" INICIANDO PERFILAMIENTO DE TIEMPO ")
    print("="*50)
    #Usa timeit para correr la carga 500 veces y promediar
    tiempo_total = timeit.timeit(perfilar_carga_tiempo, number=500)
    print(f"El tiempo total para 500 ejecuciones fue: {tiempo_total:.5f} segundos")
    print(f"El tiempo promedio por ejecucion (100 canciones) fue: {tiempo_total / 500:.6f} segundos")