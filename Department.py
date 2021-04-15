from worker import Worker
from Observer import Observer
class Departament(Observer):
    def __init__(self):
        self.workerList=[]
        self.observers=[]
        self.worklist=[]
        self.chief = None
    def addWorker(self,worker):
        if worker.chief == False:
            self.workerList.append(worker)
        else:
            print("начальник не может быть обычным сотрудником")
    def addChief(self,chief):
        self.chief = chief

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

    def selectWorker(self):
        ready= False
        for worker in self.workerList:
            if worker.run == False :
                worker.taskRun(day)
                ready=True
        if ready == False and self.chief.run == False:
            self.chief.taskRun(day):
            ready = True
        if ready == False: 
            pass
            


        
