'''
    0 1 2 3 4 5 6 7 8 9
    f p f p f p f p f p
 f  0   1   2   3   4
 p    0   1   2   3   4

even = fork
odd  = phil

'''

import collections
import sys
import time
import random
from enum import Enum
import datetime
import threading
from threading import Thread

import os
import multiprocessing

pool= multiprocessing.Pool(processes=(multiprocessing.cpu_count() - 2))

seats = []
forks = []

class State(Enum):
    THINKING = 0
    EATING = 1

class Level(Enum):
    LOW    = 1
    MEDIUM = 2
    HIGH   = 3

class Fork():
    def __init__(self,id):
        self.id = id
        self.inUse = False


class Seat():
    phil = '' 
    def __init__(self,id):
        self.id = id

class Phil():
    def __init__(self , id , hunger):
        self.id = id
        self.hunger = hunger
        # self.level = level
        self.state=State.THINKING
        
    


def Eat(choice,left,right):


    choice.phil.state=State.EATING
    forks[left].inUse = True
    forks[right].inUse = True


    # if choice.phil.state == State.EATING:



    choice.phil.hunger-=2
    time.sleep(5)

    choice.phil.state = State.THINKING
    forks[left].inUse = False
    forks[right].inUse = False

# class Payload(object):
#     def __init__(self, d):
#         self.__dict__ = d



def Waiter():
    # while(True):
    choice = random.choice(seats)
    # print('choice:',choice.id) #,'position:',seats.index(choice))
    # print(choice.phil.state)
    # print('hunger:',choice.phil.hunger)

    if choice.phil.hunger > 0:
        left,right =CheckForks(seats.index(choice))
        if not left and not right:
            print('cannot eat!')
            ammount = 10
        else:
            print('eat!')
            # ammount = 10
            # p = Payload(choice)
            process = multiprocessing.Process(target=Eat, args=(choice,left,right,))
            
            #seats.index(choice),))
            process.start()


            # Thread(target=Eat, args=(choice,)).start()
        
    else:
        ammount = 10
        # print('not hungry!')


    time.sleep(2)
    Waiter()
        
        
def Map():

    print('| 1 | 2 | 3 | 4 | 5 |')
    print(
        seats[0].phil.state,
        seats[1].phil.state,
        seats[2].phil.state,
        seats[3].phil.state,
        seats[4].phil.state)
    time.sleep(1)
    Map()

def CheckForks(id):
    if id == 0:
        left = forks[-1] 
        right = forks[0]
    elif id == 4:
        left = forks[id]
        right = forks[0]
    else:
        left = forks[id]
        right = forks[id+1]

    if not left.inUse and not right.inUse:
        return forks.index(left), forks.index(right)
    else:
        return False, False


if __name__ == '__main__':

    forks.append(Fork(0))
    forks.append(Fork(2))
    forks.append(Fork(4))
    forks.append(Fork(6))
    forks.append(Fork(8))

    seats.append(Seat(1))
    seats.append(Seat(3))
    seats.append(Seat(5))
    seats.append(Seat(7))
    seats.append(Seat(9))
    
    seats[0].phil = Phil(0,10)
    seats[1].phil = Phil(1,10)
    seats[2].phil = Phil(2,10)
    seats[3].phil = Phil(3,10)
    seats[4].phil = Phil(4,10)

    # process = multiprocessing.Process(target=Map, args=())
    # process.start()
    
    Thread(target=Map, args=()).start()
    
    Waiter()


    
    #seats.index(choice),))

