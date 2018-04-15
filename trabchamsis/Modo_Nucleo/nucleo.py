import sys  # for custom paths
import time  # for waits
# import random
# import os
# import multiprocessing
import datetime  # for logging time

logPath = "Modo_Nucleo/nucleoLog.txt"
binaryPath = "Modo_Nucleo/binary.txt"
isNucleo = False  # flag for usermode
isOn = False  # flag for system state

jobs = []  # pool of jobs

botsPath = "bots/"


class Job:
    def __init__(self, userName, function, parameters, highPriority=False, isBot=False):
        self.userName = userName
        self.function = function
        self.parameters = parameters
        self.highPriority = highPriority
        self.isBot = isBot


def WriteEndFile(message, botName=False):  # append at the end
    if(CheckAuth(botName)):
        file = open(binaryPath, "a")
        file.write(message)
        return 'Escrito com sucesso'


def ReadFromFile(initial=False, final=False, botName=False):
    if(CheckAuth(botName)):
        file = open(binaryPath, "r").read()
        if(not initial and not final):  # if no specified positions then return whole file
            return file
        # print("ini:", initial, "final:", final)
        return file[initial:final]


def CheckAuth(botName=False):
    if(isNucleo):
        if botName:
            LogBot(botName, '\nAction executed, user authorized\n')
        log('Action executed, user authorized\n')
        print('\nAction executed, user authorized')
        return True

    if botName:
        LogBot(botName, '\nAction denied, user not authorized!\n')
    log('Action denied, user not authorized!\n')
    print('\nAction denied, user not authorized!')
    return False


def CheckState():
    return isOn
    # log('checked mofo \n')


def SwitchSystem(state):
    global isOn
    global isNucleo

    if(state):
        log("Starting at %s \n" % datetime.datetime.now().strftime("%H:%M:%S"))
        isOn = isNucleo = True
        log('(Nucleo) Modo Nucleo: %s\n' % isNucleo)
        Cycle()
    else:
        if isOn:
            log("Ending at %s \n\n\n" %
                datetime.datetime.now().strftime("%H:%M:%S"))
            isOn = isNucleo = False


def ProcessOldest():
    # global jobs
    job = jobs[0]
    log('Processing job from %s \n' % job.userName)
    if job.isBot:

        LogBot(job.userName, "Resposta de leitura as %s" %
               datetime.datetime.now().strftime("%H:%M:%S"))
        LogBot(job.userName, str(job.function(
            *job.parameters, botName=job.userName)))
    else:  # splat saves the night
        print(str(job.function(*job.parameters)))
    del jobs[0]


def ProcessHighest():
    for i, job in enumerate(jobs):
        if job.highPriority:
            log('Interrupted -> Processing job from %s \n' % job.userName)
            if job.isBot:

                LogBot(job.userName, "Resposta de leitura as %s" %
                       datetime.datetime.now().strftime("%H:%M:%S"))
                LogBot(job.userName, str(job.function(
                    *job.parameters, botName=job.userName)))
            else:  # splat saves the night
                print(str(job.function(*job.parameters)))
            del jobs[i]
            return True
    return False


def Cycle():
    if isOn:
        # counter = 0
        # while (counter < 5):
        # counter += 1
        log('Checking at %s Number of jobs: %s\n' %
            (datetime.datetime.now().strftime('%H:%M:%S'), len(jobs)))
        if(len(jobs) > 0):
            if not ProcessHighest():
                ProcessOldest()
        # log(str(isOn))
        # job = Job('Teste')
        # jobs.append(job)
        # TestCall()
        sys.stdout.flush()  # required to run on vscode terminal when looping

        time.sleep(5)
        Cycle()


def log(message):
    with open(logPath, 'a') as f:  # 0 as buffer so no wait
        f.write(message)
    # while(True):
    #     f.write('{}\n'.format(datetime.datetime.now()))
    #     time.sleep(1)


def LogBot(userName, message):
    file = open(botsPath+userName+'.txt', "a")
    file.write(message)
# def TestCall(ini, fini):
#     # print('testCalled as nucleo: ', isNucleo)
#     print('tested x: ', ini, 'y: ', fini)

# def TestCallSingle(fini):
#     # print('testCalled as nucleo: ', isNucleo)
#     print('tested y: ', fini)


# testVar = 'untested'
# print('testing')
# def ChangeTestVar(message):
#     print('changing testVar')
#     global testVar
#     testVar = message


# if __name__ == '__main__':
    # isNucleo = True

    # log('test')
#     log('(Nucleo) Modo Nucleo: %s\n' % isNucleo)

    # log('testesteste')
    # SwitchSystem(True)
    # TestCall()

    # WriteEndFile('01010010101001')

    # print(ReadFromFile())
    # print(ReadFromFile(5, 10))
