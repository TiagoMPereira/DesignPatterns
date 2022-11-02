import abc
import numpy as np
from strategy.scripts.sort import Ordenador

# Método abstrato para simular interface em python
class ListaNumeros(abc.ABC):

    def __init__(self):
        self.ordenador = Ordenador

    def retorna_ordenado(self, lista):
        return np.array(self.ordenador.ordena(lista))