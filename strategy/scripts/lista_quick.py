from .lista_numeros import ListaNumeros
from .ordenador.impl.quick_sort import QuickSort

class ListaQuick(ListaNumeros):

    def __init__(self):
        self.lista_name = "quick"
        self.ordenador = QuickSort()