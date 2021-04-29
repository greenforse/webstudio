from Observer import Observer
class CompleteList(Observer):
    def __init__(self):
        self.complete = 0
    def addTask(self,task):
        self.complete += 1
        print("Выполенено", self.complete)