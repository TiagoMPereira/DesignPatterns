from strategy.scripts.lista_numeros import ListaNumeros
from strategy.scripts.ordenador.impl.insertion_sort import InsertionSort

class ListaInsertion(ListaNumeros):

    def __init__(self):
        self.lista_name = "insertion"
        self.ordenador = InsertionSort()