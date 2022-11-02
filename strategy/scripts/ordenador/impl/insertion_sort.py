from ...sort import Ordenador

import numpy as np

class InsertionSort(Ordenador):

    def __init__(self):
        self.alg_name = "insertion"

    def ordena(self, lista: np.array) -> np.array:
        
        for i in range(1, len(lista)):
            key_item = lista[i]
            j = i - 1

            while j >= 0 and lista[j] > key_item:
                lista[j + 1] = lista[j]
                j -= 1

            lista[j + 1] = key_item

        return lista