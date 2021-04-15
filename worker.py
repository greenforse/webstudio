from abc import abstractmethod
from abc import ABCMeta, abstractmethod
import random

class Worker(metaclass=abstractmethod):
    def __init__(self,name,chief):
        self.completeChance = random.randint(70,95)
        self.chief=bool(chief)
        self.name=name
        self.score=0

    def taskRun(self):
        if random.randint(1,100) > self.completeChance:
            print("Выполнено в срок")
            self.score+=1
        else:
            self.score-=1

    def getScore(self):
        return self.score