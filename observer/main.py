from .scripts.impl.observador import Observador
from .scripts.impl.observavel import Observavel

if __name__ == "__main__":

    frase = Observavel()

    observador1 = Observador(id=1)
    observador2 = Observador(id=2)
    observador3 = Observador(id=3)

    frase.registra_observador(observador1)
    frase.registra_observador(observador2)
    frase.registra_observador(observador3)

    frase.set_frase("testando Observador De frases")

    frase.remove_observador(observador1)
    frase.notifica_observadores()