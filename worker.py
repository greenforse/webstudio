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
        self.task=None

    def addTask(self,task):
        self.task=task

    def taskRun(self):   
        if self.task != None :
            self.spendDays+=1
            if random.randint(1,100) < self.completeChance and self.spendDays == self.task.deadlines[self.departament.number]:
                print(f"Выполнено в срок{self.departament.number}")
                self.spendDays=0
                self.score+=1
                self.departament.notify(self.task)
                self.task=None
            elif self.spendDays > self.task.deadlines[self.departament.number] and random.randint(1,100) < self.completeChance :
                print(f"выполнена не в срок {self.departament.number}")
                self.spendDays = 0
                self.score -= 1
                self.departament.chief.score -= 1
                self.departament.notify(self.task)
                self.task=None

    def getName(self):
        return self.name

        #if complete == False:
        #    self.run = True
        #else: self.run = False
    def getScore(self):
        return self.score