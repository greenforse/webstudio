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
        #self.ready=False #пометочка
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

    def notify(self,task):
        for observer in self.observers:
            observer.addTask(task)
    
        

    def addTask(self,task):
        self.worklist.append(task)

    def run(self):
        if len(self.worklist)!=0:
            self.selectWorker(self.worklist[0])
            del self.worklist[0]

    def selectWorker(self,task):
        self.ready= False
        for worker in self.workerList:
            if worker.task == None :
                worker.taskRun(task)
                #del self.worklist[0]
                self.ready=True
        if self.ready == False and self.chief.task== None:
            self.chief.taskRun(task)
            #del self.worklist[0]
            self.ready = True
        if self.ready == False:
            self.addTask(task)
        #    pass
            


        
