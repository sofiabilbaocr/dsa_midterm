import random

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def __repr__(self):
        return f"| {self.data['nombre']} |"

class LinkedList:
    def __init__(self):
        self.start = None
        self.current = None
        self.length = 0          # Llevamos la cuenta del tamaño
        self.is_shuffle = False  # Estado del shuffle (ON/OFF)
        self.history = []        # Historial para retroceder en modo shuffle

    def append(self, data):
        new_node = Node(data)
        self.length += 1         # Aumentamos el tamaño con cada inserción
        
        if self.start is None:
            self.start = new_node
            self.current = new_node
            return
        
        actual = self.start
        while actual.next is not None:
            actual = actual.next
        
        actual.next = new_node
        new_node.prev = actual

    def toggle_shuffle(self):
        # Invierte el estado de False a True o viceversa
        self.is_shuffle = not self.is_shuffle
        # Si encendemos el shuffle, limpiamos el historial para empezar fresco
        if self.is_shuffle:
            self.history = []

    def next_song(self):
        if self.current is None:
            return None

        if self.is_shuffle:
            # 1. Guardamos la canción actual en el historial antes de saltar
            self.history.append(self.current)
            
            # 2. Elegimos un número aleatorio de saltos
            pasos = random.randint(0, self.length - 1)
            
            # 3. NAVEGACIÓN DE NODOS (Requisito del examen)
            actual = self.start
            for _ in range(pasos):
                actual = actual.next
            
            self.current = actual
        else:
            # Comportamiento normal (lineal)
            if self.current.next is not None:
                self.current = self.current.next
            else:
                print("\n[!] Ya llegaste al FINAL de la playlist.") # <-- Agregado
                
        return self.current

    def prev_song(self):
        if self.current is None:
            return None

        if self.is_shuffle:
            # Sacamos el último nodo visitado del historial
            if len(self.history) > 0:
                self.current = self.history.pop()
            else:
                print("\n[!] Ya estás en la primera canción del shuffle.")
        else:
            # Comportamiento normal (lineal)
            if self.current.prev is not None:
                self.current = self.current.prev
            else:
                print("\n[!] Ya estás en el INICIO de la playlist.") # <-- Agregado
                
        return self.current