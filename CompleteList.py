from Observer import Observer
class CompleteList(Observer):
    def __init__(self):
        self.complete=[]
    def addTask(self,task):
        self.complete.append(task)