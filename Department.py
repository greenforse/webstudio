from worker import Worker
from Observer import Observer
class Departament(Observer):
    def __init__(self):
        self.workerList=[]
        self.observers=[]
        self.worklist=[]
    def addWorker(self,worker):
        self.workerList.append(worker)

    def subscribe(self,observer):
        self.observers.append(observer)

    def unsubcribe(self,observer):

    def notify(self):
        for observer in self.observers:
            observer.run()

    def run(self,):
        
