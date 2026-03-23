class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None  #double

    def __repr__(self):
        return f"| {self.data['nombre']} |"

class LinkedList:
    def __init__(self):
        self.start = None
        self.current = None
        self.length = 0

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
        
        #double
        actual.next = new_node
        new_node.prev = actual

    def next_song(self):
        if self.current is not None and self.current.next is not None:
            self.current = self.current.next
        return self.current

    def prev_song(self):
        if self.current is not None and self.current.prev is not None:
            self.current = self.current.prev
        return self.current