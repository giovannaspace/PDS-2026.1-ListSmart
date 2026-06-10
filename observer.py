from abc import ABC, abstractmethod

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
   
    def attach(self, observer):
        pass

    def detach(self, observer):
        pass

    def notify(self):
        pass


# ETAPA 3 - DEFINIÇÃO DOS MÉTODOS -> INTERFACE DO OBSERVER

class Observer(ABC):

    @abstractmethod
    def update(self):
        pass


# ETAPA 4 - OBSERVADORES -> CADA UM IMPLEMENTA O SEU MÉTODO UPDATE

class ConcreteObserver_1(Observer):
    pass


class ConcreteObserver_2(Observer):
    pass

class ConcreteObserver_3(Observer):
    pass