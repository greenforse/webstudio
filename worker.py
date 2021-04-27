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

    def taskRun(self,task):   
        self.spendDays+=1
        self.task=task
        if random.randint(1,100) < self.completeChance and self.spendDays == self.task.deadlines[self.departament.number]:
            print("Выполнено в срок")
            self.spendDays=0
            self.score+=1
            self.departament.notify(task)
            self.task=None
        if self.spendDays > self.task.deadlines[self.departament.number] and random.randint(1,100) < self.completeChance :
            print("выполнена не в срок")
            self.spendDays = 0
            self.score -= 1
            self.departament.chief.score -= 1
            self.department.notify(task)
            self.task=None

    def getName(self):
        return self.name

        #if complete == False:
        #    self.run = True
        #else: self.run = False
    def getScore(self):
        return self.score