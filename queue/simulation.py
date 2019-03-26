from Queue import Queue
import random
from printer import Printer
from Task import Task


def simulation(numSeconds, pagesPerMinute):
    labprinter = Printer(pagesPerMinute)
    printQueue = Queue()
    waitingtimes = []

    for currentSecond in range(numSeconds):
        if newPrintTask():
            task = Task(currentSecond)
            printQueue.enqueue(task)

        if(not labprinter.busy()) and (not printQueue.isEmpty()):
            # print(printQueue.size())
            nexttask = printQueue.dequeue()
            waitingtimes.append(nexttask.waitTime(currentSecond))
            # print(waitingtimes)
            labprinter.startNext(nexttask)

        labprinter.tick()
    # return waitingtimes
    return((sum(waitingtimes)/len(waitingtimes)), printQueue.size())


def newPrintTask():
    num = random.randrange(1, 181)
    # print(num)
    if num == 180:
        return True
    else:
        return False


for i in range(10):
    print(simulation(3600, 5))
