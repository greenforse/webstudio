from Department import Departament
from worker import Worker
from Task import Task
from CompleteList import CompleteList
import random
DepDesign=Departament(0)
Anton=Worker("Anton",True,DepDesign)
DepDesign.addChief(Anton)
Genadiy=Worker("Генадий",False,DepDesign)
Misha=Worker("Миша",False,DepDesign)
Roma=Worker("Roma",False,DepDesign)
DepDesign.addWorker(Genadiy)
DepDesign.addWorker(Misha)
DepDesign.addWorker(Roma)

DepFront=Departament(1)
Artyr=Worker("Артур",True,DepFront)
DepFront.addChief(Artyr)
Vladimir=Worker("Владимир",False,DepFront)
Pasha=Worker("Паша",False,DepFront)
Fedya=Worker("Федя",False,DepFront)
DepFront.addWorker(Vladimir)
DepFront.addWorker(Pasha)
DepFront.addWorker(Fedya)

DepBack=Departament(2)
Artem=Worker("Артем",True,DepBack)
DepBack.addChief(Artem)
Vlad=Worker("Влад",False,DepBack)
Masha=Worker("Marya",False,DepBack)
Tatyana=Worker("Татьяна",False,DepBack)
DepBack.addWorker(Vlad)
DepBack.addWorker(Masha)
DepBack.addWorker(Tatyana)

Clist = CompleteList()

DepDesign.subscribe(DepFront)
DepFront.subscribe(DepBack)
DepBack.subscribe(Clist)

day=0
zadanie=0
while Clist.complete < 10:
#while day < 20:
    if day < 10:
        task=Task(random.randint(2,5),random.randint(2,5),random.randint(2,5))
        DepDesign.addTask(task)
        zadanie+=1
        print("Поступило задание", zadanie)
    DepDesign.run()
    DepFront.run()
    DepBack.run()
    day += 1
    #print(" Прошел один день")
print(" Отдел дизайна ")
for worker in DepDesign.workerList:
    print(f"{worker.getName()}:{worker.getScore()}")
print(f"начальник:{DepDesign.chief.getName()}:{DepDesign.chief.getScore()}")

print(" Отдел фронтенда ")
for worker in DepFront.workerList:   
    print(f"{worker.getName()}:{worker.getScore()}")
print(f"начальник:{DepFront.chief.getName()}:{DepFront.chief.getScore()}")

print(" Отдел бекенда ")
for worker in DepBack.workerList:
    print(f"{worker.getName()}:{worker.getScore()}")
print(f"начальник:{DepBack.chief.getName()}:{DepBack.chief.getScore()}")