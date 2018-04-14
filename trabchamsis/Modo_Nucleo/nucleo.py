import sys
import time
import random
import os
import multiprocessing
import datetime


fileName = "Modo_Nucleo/binary.txt"
isNucleo = False  # flag for usermode
isOn = False


jobs = []  # pool of jobs


class Job:
    # userName = ''
    def __init__(self, userName):
        self.userName = userName


def WriteEndFile(message):  # append at the end

    if(CheckAuth()):
        file = open(fileName, "a")
        file.write(message)


def ReadFromFile(initial=False, final=False):
    if(CheckAuth()):
        file = open(fileName, "r").read()
        if(not initial and not final):  # if no specified positions then return whole file
            return file
        return file[initial:final]


def CheckAuth():
    if(isNucleo):
        print('Action executed, user authorized')
        return True

    print('Action denied, user not authorized!')
    return False


def TestCall():
    print('testCalled as nucleo: ', isNucleo)


def SwitchSystem(on):
    if(on):
        print("Starting at", datetime.datetime.now().strftime("%H:%M:%S"))
        global isOn
        isOn = True
        global isNucleo
        isNucleo = True
        print('(Nucleo) Modo Nucleo:', isNucleo)
        Cycle()


def Cycle():
    counter = 0
    while (counter < 5):
        # counter += 1
        print('Checking at', datetime.datetime.now().strftime('%H:%M:%S'),
              'Number of jobs: ', len(jobs))

        time.sleep(3)
        # TestCall()
        sys.stdout.flush()  # required to run on vscode terminal


if __name__ == '__main__':
    # isNucleo = True
    print('(Nucleo) Modo Nucleo:', isNucleo)

    # SwitchSystem(True)
    # TestCall()

    # WriteEndFile('01010010101001')

    # print(ReadFromFile())
    # print(ReadFromFile(5, 10))
