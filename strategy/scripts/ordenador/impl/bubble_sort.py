from strategy.scripts.sort import Ordenador

import numpy as np

class BubbleSort(Ordenador):

    def __init__(self):
        self.alg_name = "bubble"

    def ordena(self, lista: np.array) -> np.array:

        n = len(lista)

        for i in range(n):
            already_sorted = True

            for j in range(n - i - 1):
                if lista[j] > lista[j + 1]:
                    lista[j], lista[j + 1] = lista[j + 1], lista[j]
                    already_sorted = False

            if already_sorted:
                break

        return lista