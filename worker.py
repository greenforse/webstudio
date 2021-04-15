from abc import abstractmethod
from abc import ABCMeta, abstractmethod
import random

class Worker():
    def __init__(self,name,chief,departament):
        self.completeChance = random.randint(70,95)
        self.chief=bool(chief)
        self.name=name
        self.score=0
        self.departament=departament
        self.run = False

    def taskRun(self,day):    #поставил переменную day, планирую в  мейне(вайле)  вызывать каждый раз таскран и под конеч выдвать результат работы
        taskDays +=1
        complete=False
        if taskDays == day and random.randint(1,100) > self.completeChance:
            print("Выполнено в срок")
            complete=True
            self.score+=1
        if complete == False:
            self.run = True
        else: self.run = False
    def getScore(self):
        return self.score