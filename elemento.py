

class Elemento:

    def __init__(self, novo_valor):
        self._valor = novo_valor
        self._esquerda = None
        self._direita = None

    def get_valor(self):
        return self._valor

    def set_valor(self, valor):
        self._valor = valor

    def get_direita(self):
        return self._direita
    
    def set_direita(self, direita):
        self._direita = direita

    def get_esquerda(self):
        return self._esquerda

    def set_esquerda(self, esquerda):
        self._esquerda = esquerda