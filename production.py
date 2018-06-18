import sys 
import time  
import random
from enum import Enum
import datetime 

jobs = list(range(1,35))
pile = []

def Production():
    while len(pile) < 5:
        print('Producing',jobs[0])
        pile.append(jobs[0])
        jobs.remove(jobs[0])
    Consumption()

def Consumption():
    while len(pile) > 0:
        print('Consuming',pile[0])
        pile.remove(pile[0])
    Production()

if __name__ == '__main__':
    Production()