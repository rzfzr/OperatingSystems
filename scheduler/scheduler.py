import sys  # for custom paths
import time  # for waits
import random
# import os
# import multiprocessing
from enum import Enum
import datetime  # for logging time
jobs = []  # pool of jobs
tickets = []
class Type(Enum):
    FIFO= 1
    PRIORITY = 2
    PRIORITY_FILE = 3
    FAIR_SHARING = 4
    LOTTERY = 5

class State(Enum):
    READY    = 1
    WORKING  = 2

class Level(Enum):
    LOW    = 1
    MEDIUM = 2
    HIGH   = 3

class Job:
    def __init__(self , pid , type, function, level=Level.MEDIUM, luck=1):
        self.pid = pid
        self.function = function
        self.state=State.READY
        
        if(type == Type.LOTTERY):
            while luck>0:
                luck-=1
                tickets.append(pid)

        elif (type==Type.PRIORITY):
            self.level=level 



def ProcessHighest():
    currentLevel = len(Level) #genius
    while True:
        for job in jobs:
            if job.level==Level(currentLevel):
                StartProcess(job)
                return
        currentLevel-=1

def ProcessOldest():
    StartProcess(jobs[0])

def ProcessLucky():    
    global tickets
    choice = random.choice(tickets)                                     # print('rand: ',choice)
    tickets = list(filter(lambda a: a != choice, tickets))              # print('tickets:',tickets)
    for job in jobs:
        if job.pid == choice:
            StartProcess(job)
            break



def StartProcess(job):
    print('Starting Process: %s \n' % job.pid)
    job.function(job.pid)
    jobs.remove(job)

def Fun(pid):
    ran=random.randint(2,5)
    ran =0
    while ran>0:
        ran-=1
        print('Process:',pid,'          Action:',ran)

def Schedule(type):
    print('Checking at %s Number of jobs: %s\n' %(datetime.datetime.now().strftime('%H:%M:%S'), len(jobs)))
    if(len(jobs) < 1):
        print('No Jobs, stopping')
        return
    if(type == Type.FIFO):
        ProcessOldest()
    if(type==Type.LOTTERY):
        ProcessLucky()
    if(type==Type.PRIORITY):
        ProcessHighest()

    Schedule(type)

if __name__ == '__main__':

    # tempType = Type.FIFO
    # jobs.append(Job(1000,tempType,Fun))
    # jobs.append(Job(1001,tempType,Fun))
    # jobs.append(Job(1002,tempType,Fun))
    # jobs.append(Job(1003,tempType,Fun))
    # jobs.append(Job(1004,tempType,Fun))
    # jobs.append(Job(1005,tempType,Fun))

    # tempType = Type.LOTTERY
    # jobs.append(Job(1000,tempType,Fun,luck=1))
    # jobs.append(Job(1001,tempType,Fun,luck=2))
    # jobs.append(Job(1002,tempType,Fun,luck=3))
    # jobs.append(Job(1003,tempType,Fun,luck=4))
    # jobs.append(Job(1004,tempType,Fun,luck=5))
    # jobs.append(Job(1005,tempType,Fun,luck=6))

    # tempType = Type.PRIORITY
    # jobs.append(Job(1000,tempType,Fun,level=Level.LOW))
    # jobs.append(Job(1001,tempType,Fun,level=Level.LOW))
    # jobs.append(Job(1002,tempType,Fun,level=Level.MEDIUM))
    # jobs.append(Job(1003,tempType,Fun,level=Level.MEDIUM))
    # jobs.append(Job(1004,tempType,Fun,level=Level.HIGH))
    # jobs.append(Job(1005,tempType,Fun,level=Level.HIGH))

    tempType = Type.FAIR_SHARING
    jobs.append(Job(1000,tempType,Fun,level=Level.LOW))
    jobs.append(Job(1001,tempType,Fun,level=Level.LOW))
    jobs.append(Job(1002,tempType,Fun,level=Level.MEDIUM))
    jobs.append(Job(1003,tempType,Fun,level=Level.MEDIUM))
    jobs.append(Job(1004,tempType,Fun,level=Level.HIGH))
    jobs.append(Job(1005,tempType,Fun,level=Level.HIGH))
    

    Schedule(tempType)