from collections import deque

class Fila:
    def __init__(self):
        self.lista = deque()

    def insere(self, val):
            self.lista.append(val)

    def remove(self):
        return self.lista.popleft()
    
    def __repr__(self):
        return f"{self.lista}".format()