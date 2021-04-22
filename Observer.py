from abc import ABCMeta, abstractmethod
class Observer(metaclass=abstractmethod):
    def __init__(self):
        pass
    
    @abstractmethod
    def run(self):
        pass
