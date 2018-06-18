import sys 
import time  
import random
from enum import Enum
import datetime 


jobs = list(range(1,35))
pile = []

def Process(job):
    print(job)

def Next():
    if jobs:
        Process(jobs[0])
        jobs.pop(0)
        Next()



bankJobs = []
accounts = []


class JobType(Enum):
    BALANCECHECK    = 1
    WITHDRAW     = 2
    TRANFER   = 3

class bankJob:
    defy __init__(self,jobType,a,amount=0,)

class Level(Enum):
    ECONOMY    = 1
    MEDIUM     = 2
    MASTER     = 3


class Account:
    def __init__(self , name,balance,id,level):
        self.name = name
        self.balance = balance
        self.id = id
        self.level = level
        self.history = []

def Balance(account):

    return account.balance




if __name__ == '__main__':
    Next()