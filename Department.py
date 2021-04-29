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
        self.freeWorkerList=[]
        #self.ready=False #пометочка
    def addWorker(self,worker):
        if not worker.chief :
            self.workerList.append(worker)
            self.freeWorkerList.append(worker)
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
            print(" нотифай ")
    
        

    def addTask(self,task):
        self.worklist.append(task)

    def run(self):
        self.freeWorkerList=[]
        for worker in self.workerList:
            if worker.task == None:
                self.freeWorkerList.append(worker)
        while len(self.worklist) != 0 and len(self.freeWorkerList) != 0 or len(self.worklist) != 0 and self.chief.task != None  :
            self.selectWorker(self.worklist[0])
            del self.worklist[0]
            print(" выбор сотруника ", self.number)
        for worker in self.workerList:
            worker.taskRun()
            #print(" выбор сотруника ")

    def selectWorker(self,task):
        #self.freeWorkerList=[]
        #for worker in self.workerList:
        #    if worker.task == None:
        #        self.freeWorkerList.append(worker)
        if len(self.freeWorkerList)!=0:
            self.freeWorkerList[0].addTask(task)
            del self.freeWorkerList[0]
        elif self.chief.task==None:
            self.chief.addTask(task)
        else: self.addTask(task)
        #for worker in self.workerList:
        #    if worker.task == None :
        #        worker.taskRun(task)
        #        #del self.worklist[0]
        #        self.ready=True
        #if self.ready == False and self.chief.task== None:
        #    self.chief.taskRun(task)
        #    #del self.worklist[0]
        #    self.ready = True
        #if self.ready == False:
        #    self.addTask(task)
        ##    pass
        #    


        
