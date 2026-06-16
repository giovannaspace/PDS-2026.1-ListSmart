from abc import ABC, abstractmethod
from backend import compartilhamento
######################## IMPLEMENTAÇÃO DESIGN PATTERN COMPORTAMENTAL OBSERVER ########################

# ETAPA 1 - DEFINIÇÃO DOS MÉTODOS -> INTERFACE DO SUBJECT

class Subject(ABC):

    @abstractmethod
    def attach(self, observer):
        pass

    @abstractmethod
    def detach(self, observer):
        pass

    @abstractmethod
    def notify(self):
        pass


# ETAPA 2 - IMPLEMENTAÇÃO DOS MÉTODOS

class ConcreteSubject(Subject):
    
    def __init__(self,dados_lista):
        self.observers = []
        self.dados_lista = dados_lista 

    # recebe e guarda observer na lista
    def attach(self, observer):
        self.observers.append(observer)

    # recebe e retira observer da lista
    def detach(self, observer):
        self.observers.remove(observer)


    def notify(self, email, numero):
        for observer in self.observers:
            observer.update(email,numero,self.dados_lista)
            


# ETAPA 3 - DEFINIÇÃO DOS MÉTODOS -> INTERFACE DO OBSERVER

class Observer(ABC):

    @abstractmethod
    def update(self, email, numero, dado_lista):
        pass


# ETAPA 4 - OBSERVADORES -> CADA UM IMPLEMENTA O SEU MÉTODO UPDATE

# WHATSAPP
class ConcreteObserver_1(Observer):
    
    def update(self, email, numero, dados_lista):
        comp = compartilhamento(dados_lista)
        comp.enviarZap(numero)


# EMAIL
class ConcreteObserver_2(Observer):
    def update(self,email, numero, dados_lista):
        comp = compartilhamento(dados_lista)
        comp.enviarEmail(email)


# CANAL FUTURO
#class ConcreteObserver_3(Observer):
#    def update(self,parametro):
#        pass
