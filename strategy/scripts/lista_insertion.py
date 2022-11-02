from .lista_numeros import ListaNumeros
from .ordenador.impl.insertion_sort import InsertionSort

class ListaInsertion(ListaNumeros):

    def __init__(self):
        self.lista_name = "insertion"
        self.ordenador = InsertionSort()