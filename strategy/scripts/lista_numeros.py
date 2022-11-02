import abc
import numpy as np
from .sort import Ordenador

# Método abstrato para simular interface em python
class ListaNumeros(abc.ABC):

    def __init__(self):
        self.ordenador = Ordenador

    def retorna_ordenado(self, lista):
        return self.ordenador.ordena(lista)