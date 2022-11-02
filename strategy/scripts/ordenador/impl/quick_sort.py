from strategy.scripts.sort import Ordenador

from random import randint
import numpy as np

class QuickSort(Ordenador):

    def __init__(self):
        self.alg_name = "quick"

    def ordena(self, lista: np.array) -> np.array:
        if len(lista) < 2:
            return lista

        low, same, high = [], [], []
        pivot = lista[randint(0, len(lista) - 1)]

        for item in lista:
            if item < pivot:
                low.append(item)

            elif item == pivot:
                same.append(item)

            elif item > pivot:
                high.append(item)

        return self.ordena(low) + same + self.ordena(high)