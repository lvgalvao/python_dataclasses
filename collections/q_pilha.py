from collections import deque

class Pilha:
    def __init__(self):
        self.pilha = deque()

    def insere(self, val):
        self.pilha.append(val)

    def remove(self):
        return self.pilha.pop()

    def __repr__(self):
        return f"{self.pilha}".format()