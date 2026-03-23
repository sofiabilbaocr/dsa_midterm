class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f"| {self.data['nombre']} |"

class LinkedList:
    def __init__(self):
        self.start = None
        self.current = None
        self.length = 0  #llevar la cuenta para el shuffle más adelante

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