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

# pool= multiprocessing.Pool(processes=(multiprocessing.cpu_count() - 2))

seats = []
forks = []
tickets = []


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
    def __init__(self , id , level):
        self.id = id
        # self.hunger = hunger
        self.state=State.THINKING

        self.luck = 0
        if level == Level.LOW:
            self.hunger = 333
        elif level == Level.MEDIUM:
            self.hunger = 666
        elif level == Level.HIGH:
            self.hunger = 999


        while self.luck > 0:
            self.luck=-1
            tickets.append(id)
        
    


def Eat(choice,left,right):
    choice.phil.state=State.EATING
    forks[left].inUse = True
    forks[right].inUse = True
    
    time.sleep(5)
    choice.phil.hunger-=1

    choice.phil.state = State.THINKING
    forks[left].inUse = False
    forks[right].inUse = False


def Lucky(tickets):
    choice = ''
    lucky = random.choice(tickets)
    # print('random:',lucky)
    
    tickets = list(filter(lambda a: a != lucky, tickets))              # print('tickets:',tickets)
    for seat in seats:
        if seat.phil.id == lucky:
            choice = seat
            break

def Waiter():

    global tickets
    
    # if len(tickets) == 0:
        # print('out of tickets')
        # return


    choice = random.choice(seats)

    # print('choice:',choice.id) #,'position:',seats.index(choice))
    # print(choice.phil.state)
    # print('hunger:',choice.phil.hunger)

    if choice.phil.hunger > 0:
        left,right =CheckForks(seats.index(choice))
        if not left and not right:
            # print('cannot eat!')
            amount = 10
        else:
            # print('eat!')
            # ammount = 10
            # p = Payload(choice)



            Thread(target=Eat, args=(choice,left,right,)).start()

            # process = multiprocessing.Process(target=Eat, args=(choice,left,right,))
            # process.start()
            
            #seats.index(choice),))


            # Thread(target=Eat, args=(choice,)).start()
        
    else:
        ammount = 10
        # print('not hungry!')


    time.sleep(.1)
    Waiter()
        
        
def Map():

    

    hunger = '|'
    for seat in seats:
        hunger += '  '+ str(seat.phil.hunger)+' |'

    
    ids = '|'
    for seat in seats:
        ids += '   '+str(seat.phil.id)+'  |'

    states = '|'
    for seat in seats:
        if seat.phil.state==State.EATING:
            states += '   E  |'
        else:
            states += '      |'
    
    message = '    '
    for fork in forks:
        if fork.inUse:
            message += '       '
        else:
            message += '   Y   '


    print(hunger)
    print(ids)
    print(states)
    print(message)
    
    
    time.sleep(1)
    Map()

def CheckForks(id):
    # Map()

    # print('id:',id)

    if id == 0:
        left = forks[-1] 
        right = forks[0]
    elif id == 4:
        left = forks[id-1]
        right = forks[id]
    else:
        left = forks[id-1]
        right = forks[id]

    if not left.inUse and not right.inUse:

        # print('forks:',forks.index(left),' r:',forks.index(right))
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
    
    seats[0].phil = Phil(0,Level.LOW)
    seats[1].phil = Phil(1,Level.LOW)
    seats[2].phil = Phil(2,Level.MEDIUM)
    seats[3].phil = Phil(3,Level.HIGH)
    seats[4].phil = Phil(4,Level.HIGH)

    # process = multiprocessing.Process(target=Map, args=())
    # process.start()
    
    Thread(target=Map, args=()).start()
    
    Waiter()


    
    #seats.index(choice),))

