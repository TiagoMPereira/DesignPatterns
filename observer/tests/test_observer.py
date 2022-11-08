from observer.scripts.impl.observavel import Observavel
from observer.scripts.impl.observador import Observador

class TestObservavel():

    def test_observavel__sem_observador__expected_lista_vazia(self):
        # Exercise
        observavel = Observavel()
        
        # Assert
        assert len(observavel._observadores) == 0
    
    def test_observavel__insere_observador__expected_lista_com_observador(self):
        # Fixture
        observador = Observador(id=5)
        observavel = Observavel()
        observavel.registra_observador(observador)
        
        # Exercise
        n_observadores = len(observavel._observadores)
        
        # Assert
        assert n_observadores == 1
    
    def test_observavel__quantidade_palavras__expected_2_palavras(self):
        # Fixture
        observavel = Observavel()
        observavel.set_frase("Teste Palavra")
        
        # Exercise
        n_palavras = observavel.get_qtd_palavras()
        
        # Assert
        assert n_palavras == 2
    
    def test_observavel__quantidade_maiuscula__expected_2_maiusculas(self):
        # Fixture
        observavel = Observavel()
        observavel.set_frase("Teste Palavra")
        
        # Exercise
        n_maiusculas = observavel.get_comeca_maiuscula()
        
        # Assert
        assert n_maiusculas == 2
    
    def test_observavel__quantidade_pares__expected_1_palavra(self):
        # Fixture
        observavel = Observavel()
        observavel.set_frase("hello Python")
        
        # Exercise
        n_pares = observavel.get_caracteres_par()
        
        # Assert
        assert n_pares == 1
