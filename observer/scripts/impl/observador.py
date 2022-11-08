from observer.scripts.interfaces.observador import IObservador

class Observador(IObservador):
    
    def __init__(self, id):
        self.id = id

    def update(self, frase):
        print(f"==== OBSERVADOR Nº: {self.id} ====")
        print(f"==== QUANTIDADE DE PALAVRAS: {frase.get_qtd_palavras()} ====")
        print(f"==== QUANTIDADE DE PALAVRAS (QUANTIDADE PAR DE CARACTERES): {frase.get_caracteres_par()} ====")
        print(f"==== QUANTIDADE DE PALAVRAS (COMEÇADAS COM MAIÚSCULAS): {frase.get_comeca_maiuscula()} ====")
        print(f"============")
