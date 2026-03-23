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
        self.length = 0          # Para saber hasta dónde puede saltar
        self.is_shuffle = False  # Estado del reproductor
        self.history = []        # Historial para el botón de "Anterior" en shuffle

    def append(self, data):
        new_node = Node(data)
        self.length += 1
        
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
        self.is_shuffle = not self.is_shuffle
        if self.is_shuffle:
            # Limpia el historial al inciarlo para empezar limpio
            self.history = []

    def next_song(self):
        if self.current is None:
            return None

        if self.is_shuffle:
            # 1. Guarda dónde está antes de saltar
            self.history.append(self.current)
            
            # 2. Elige cuántos pasos dara al azar
            pasos = random.randint(0, self.length - 1)
            
            # 3. Navegación basada en nodos
            actual = self.start
            for _ in range(pasos):
                actual = actual.next
            
            self.current = actual
        else:
            # Comportamiento normal (lineal)
            if self.current.next is not None:
                self.current = self.current.next
        return self.current

    def prev_song(self):
        if self.current is None:
            return None

        if self.is_shuffle:
            # Retrocede sacando el último nodo visitado del historial
            if len(self.history) > 0:
                self.current = self.history.pop()
            else:
                print("\n[!] Ya estás en la primera canción del shuffle.")
        else:
            # Comportamiento normal (lineal)
            if self.current.prev is not None:
                self.current = self.current.prev
        return self.current