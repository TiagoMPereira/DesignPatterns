from observer.scripts.interfaces.observavel import IFrase
class Observavel(IFrase):

    def __init__(self):
        self._qtd_palavras = 0
        self._caracteres_par = 0
        self._comeca_maiuscula = 0
        self._observadores = []

    def registra_observador(self, obs):
        self._observadores.append(obs)
        print(f"!!!! OBSERVADOR {obs.id} CRIADO !!!!")

    def remove_observador(self, obs):
        if obs in self._observadores:
            self._observadores.remove(obs)
            print(f"XXXX REMOVENDO OBSERVADOR {obs.id} XXXX")

    def notifica_observadores(self):
        for observador in self._observadores:
            observador.update(self)
    
    def set_qtd_palavras(self, value):
        self._qtd_palavras = value
    def set_caracteres_par(self, value):
        self._caracteres_par = value
    def set_comeca_maiuscula(self, value):
        self._comeca_maiuscula = value
    def get_qtd_palavras(self):
        return self._qtd_palavras 
    def get_caracteres_par(self):
        return self._caracteres_par 
    def get_comeca_maiuscula(self):
        return self._comeca_maiuscula 

    def _cont_palavras(self, frase):
        return len(frase.split(" "))

    def _cont_palavras_pares(self, frase):
        total = 0
        for palavra in frase.split(" "):
            if len(palavra) % 2 == 0:
                total += 1
        return total

    def _cont_palavras_maiuscula(self, frase):
        total = 0
        for palavra in frase.split(" "):
            if palavra[0].isupper():
                total += 1
        return total

    def set_frase(self, frase: str):
        self.set_qtd_palavras(self._cont_palavras(frase))
        self.set_caracteres_par(self._cont_palavras_pares(frase))
        self.set_comeca_maiuscula(self._cont_palavras_maiuscula(frase))

        self.notifica_observadores()