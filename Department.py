from worker import Worker
from Observer import Observer
from Task import Task
class Departament(Observer):
    def __init__(self,departmentNumber):
        self.number=departmentNumber
        self.workerList=[]
        self.observers=[]
        self.worklist=[]
        self.chief = None
    def addWorker(self,worker):
        if not worker.chief :
            self.workerList.append(worker)
        else:
            self.addChief(worker)
    def addChief(self,chief):
        if self.chief == None:
            self.chief = chief
        else:
            raise ValueError("Не может быть 2 начальника в отделении")

    def subscribe(self,observer):
        self.observers.append(observer)

    def unsubcribe(self,observer):
        for i in range(len(self.observers)):
            self.observers[i]=observer
            del self.observers[i]

    def notify(self):
        for observer in self.observers:
            observer.run()

    def run(self):
        pass

    def selectWorker(self,task):
        ready= False
        for worker in self.workerList:
            if worker.spendDays == 0 :
                worker.taskRun(task)
                ready=True
        if ready == False and self.chief.spendDays:
            self.chief.taskRun(task)
            ready = True
        if ready == False: 
            pass
            


        
