from abc import ABCMeta, abstractmethod
class Observer():
    def __init__(self):
        pass
    
    @abstractmethod
    def run(self):
        pass
