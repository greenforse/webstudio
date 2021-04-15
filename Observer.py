from abc import ABCMeta, abstractmethod
class Observer(metaclass=abstractmethod):
    def __init__(self):
    @abstractmethod
    def run(self):
        pass

