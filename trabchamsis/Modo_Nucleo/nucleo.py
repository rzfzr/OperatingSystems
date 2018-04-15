import sys
import time
import random
import os
import multiprocessing
import datetime

logPath = "Modo_Nucleo/nucleoLog.txt"
binaryPath = "Modo_Nucleo/binary.txt"
isNucleo = False  # flag for usermode
isOn = False


jobs = []  # pool of jobs


class Job:
    userName = ''
    function = ''
    attributes = []
    # def __init__(self, userName):
    #     self.userName = userName


def WriteEndFile(message):  # append at the end
    if(CheckAuth()):
        file = open(binaryPath, "a")
        file.write(message)


def ReadFromFile(initial=False, final=False):
    if(CheckAuth()):
        file = open(binaryPath, "r").read()
        if(not initial and not final):  # if no specified positions then return whole file
            return file
        return file[initial:final]


def CheckAuth():
    if(isNucleo):
        log('Action executed, user authorized\n')
        print('Action executed, user authorized')
        return True
    log('Action executed, user authorized\n')
    print('Action denied, user not authorized!')
    return False


# def TestCall(ini, fini):
#     # print('testCalled as nucleo: ', isNucleo)
#     print('tested x: ', ini, 'y: ', fini)


# def TestCallSingle(fini):
#     # print('testCalled as nucleo: ', isNucleo)
#     print('tested y: ', fini)


def CheckState():
    # log('checked mofo \n')
    return isOn


def SwitchSystem(state):
    global isOn
    global isNucleo

    if(state):
        log("Starting at %s \n" % datetime.datetime.now().strftime("%H:%M:%S"))
        isOn = isNucleo = True
        log('(Nucleo) Modo Nucleo: %s\n' % isNucleo)
        Cycle()
    else:
        log("Ending at %s \n\n\n" %
            datetime.datetime.now().strftime("%H:%M:%S"))
        isOn = isNucleo = False

# testVar = 'untested'
# print('testing')
# def ChangeTestVar(message):
#     print('changing testVar')
#     global testVar
#     testVar = message


def ProcessOldest():
    # global jobs
    job = jobs[0]
    log('Processing job from %s \n' % job.userName)
    print(str(job.function(*job.attributes)))  # splat saves the night
    del jobs[0]


def Cycle():
    # counter = 0
    # while (counter < 5):
    # counter += 1
    log('Checking at %s Number of jobs: %s\n' %
        (datetime.datetime.now().strftime('%H:%M:%S'), len(jobs)))

    if(len(jobs) > 0):  # process the oldest
        ProcessOldest()

    # log(str(isOn))
    # job = Job('Teste')
    # jobs.append(job)
    # TestCall()
    sys.stdout.flush()  # required to run on vscode terminal when looping

    time.sleep(5)
    if isOn:
        Cycle()


def log(message):
    with open(logPath, 'a') as f:  # 0 as buffer so no wait
        f.write(message)
    # while(True):
    #     f.write('{}\n'.format(datetime.datetime.now()))
    #     time.sleep(1)


if __name__ == '__main__':
    # isNucleo = True

    # log('test')
    log('(Nucleo) Modo Nucleo: %s\n' % isNucleo)
    # log('testesteste')
    # SwitchSystem(True)
    # TestCall()

    # WriteEndFile('01010010101001')

    # print(ReadFromFile())
    # print(ReadFromFile(5, 10))
