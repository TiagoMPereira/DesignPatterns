import abc
import numpy as np

# Método abstrato para simular interface em python
class Ordenador(abc.ABC):

    @abc.abstractmethod
    def ordena(lista: np.array) -> np.array:
        pass