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
        self.spendDays=0

    def taskRun(self,task):    #поставил переменную day, планирую в  мейне(вайле)  вызывать каждый раз таскран и под конеч выдвать результат работы
        self.spendDays+=1
        if random.randint(1,100) < self.completeChance and self.spendDays == task.deadlines[self.departament.number]:
            print("Выполнено в срок")
            self.spendDays=0
            self.score+=1
        if self.spendDays > task.deadlines[self.departament.number] and random.randint(1,100) < self.completeChance :
            print("выполнена не в срок")
            self.spendDays = 0
            self.score -= 1
            self.departament.chief.score -= 1
        #if complete == False:
        #    self.run = True
        #else: self.run = False
    def getScore(self):
        return self.score