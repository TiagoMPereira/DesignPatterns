import abc

class IFrase(abc.ABC):
    
    def registra_observador(self, obs):
        pass
    def remove_observador(self, obs):
        pass
    def notifica_observadores(self):
        pass