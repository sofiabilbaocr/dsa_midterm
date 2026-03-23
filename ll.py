class Node:
    def __init__(self, data):
        # data será el diccionario con la info de la canción
        self.data = data
        self.next = None
        self.prev = None  # Puntero para hacerla doblemente enlazada

    def __repr__(self):
        return f"| {self.data['nombre']} |"

class LinkedList:
    def __init__(self):
        self.start = None
        self.current = None  # Puntero para saber qué canción está sonando

    def append(self, data):
        new_node = Node(data)
        
        # Caso 1: La lista está vacía
        if self.start is None:
            self.start = new_node
            self.current = new_node
            return
        
        # Caso 2: La lista ya tiene elementos, navega hasta el final
        actual = self.start
        while actual.next is not None:
            actual = actual.next
        
        # Conexión doble: engancha el nuevo nodo al final
        actual.next = new_node
        new_node.prev = actual

    def next_song(self):
        if self.current is not None:
            if self.current.next is not None:
                self.current = self.current.next
        return self.current

    def prev_song(self):
        if self.current is not None:
            if self.current.prev is not None:
                self.current = self.current.prev
        return self.current