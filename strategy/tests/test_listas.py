from strategy.scripts.lista_bubble import ListaBubble
from strategy.scripts.lista_quick import ListaQuick
from strategy.scripts.lista_insertion import ListaInsertion
import numpy as np

class TestListaBubble():

    def test_lista_bubble__expected_nome_correto(self):
        # Exercise
        lista = ListaBubble()
        
        # Assert
        assert lista.ordenador.alg_name == "bubble"

    def test_ordena_bubble__expected_lista_ordenada(self):
        # Fixture
        nums = np.array([5, 2, 9, 0, 3, 6, 8, 4, 1, 7])
        expected = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        lista = ListaBubble()

        # Exercise
        ordenado = lista.retorna_ordenado(nums)

        # Assert
        assert np.array_equal(expected,ordenado)


class TestListaQuick():

    def test_lista_quick__expected_nome_correto(self):
        # Exercise
        lista = ListaQuick()
        
        # Assert
        assert lista.ordenador.alg_name == "quick"

    def test_ordena_quick__expected_lista_ordenada(self):
        # Fixture
        nums = np.array([5, 2, 9, 0, 3, 6, 8, 4, 1, 7])
        expected = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        lista = ListaQuick()

        # Exercise
        ordenado = lista.retorna_ordenado(nums)

        # Assert
        assert np.array_equal(expected,ordenado)


class TestListaInsertion():

    def test_lista_insertion__expected_nome_correto(self):
        # Exercise
        lista = ListaInsertion()
        
        # Assert
        assert lista.ordenador.alg_name == "insertion"

    def test_ordena_insertion__expected_lista_ordenada(self):
        # Fixture
        nums = np.array([5, 2, 9, 0, 3, 6, 8, 4, 1, 7])
        expected = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        lista = ListaInsertion()

        # Exercise
        ordenado = lista.retorna_ordenado(nums)

        # Assert
        assert np.array_equal(expected,ordenado)