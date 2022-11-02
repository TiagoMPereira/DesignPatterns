from .lista_numeros import ListaNumeros
from .ordenador.impl.bubble_sort import BubbleSort

class ListaBubble(ListaNumeros):

    def __init__(self):
        self.lista_name = "bubble"
        self.ordenador = BubbleSort()