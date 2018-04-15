import os
import sys
import threading
from threading import Thread
sys.path.insert(0, os.getcwd())  # adds current dir to import from
from Modo_Nucleo.nucleo import *
# from Modo_Nucleo.nucleo import isNucleo
# from Modo_Nucleo.nucleo import ReadFromFile


def UserSwitchSystem(state):
    if state and not CheckState():
        Thread(target=SwitchSystem, args=(state,)).start()
    elif not state and CheckState():
        Thread(target=SwitchSystem, args=(state,)).start()


def UserWriteEndFile(userName, message):
    UserSwitchSystem(True)
    global jobs

    job = Job(userName, WriteEndFile, [message])
    if userName == 'root':
        job.highPriority = True

    jobs.append(job)


def UserReadFromFile(userName, initial=False, final=False, isBot=False):
    UserSwitchSystem(True)
    global jobs

    job = Job(userName, ReadFromFile, [initial, final], isBot=isBot)
    if userName == 'root':
        job.highPriority = True

    jobs.append(job)

# def UpdateUserName(newName):
#     global userName
#     userName = newName
# def CheckAndSwitch(username)
# print('nope')

    # else:
    #     Thread(target)

    # process = multiprocessing.Process(target=SwitchSystem, args=(True,))
    # process.start()
    # jobs.append(process)
    # SwitchSystem(True)

    # job.userName = userName
    # job.function = TestCallSingle
    # job.parameters = [44]
    #  print('added job')


# def TestLib():
#     print("libTested!")


# def UserChangeTestVar():
#     ChangeTestVar('TESTED')


# if __name__ == '__main__':
#     UserSwitchSystem(True)
#     print('(Lib) Modo Nucleo:', isNucleo)
    # print(ReadFromFile(2, 5))
    # UserReadFromFile()
    # print(len(jobs))

    # process = multiprocessing.Process(target=SwitchSystem, args=(True,))
    # process.start()
    # SwitchSystem(True)

    # time.sleep(6)

    # UserChangeTestVar()
    # WriteEndFile('zeros e uns')
