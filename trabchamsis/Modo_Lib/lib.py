import os
import sys
import threading
from threading import Thread
sys.path.insert(0, os.getcwd())  # adds current dir to import from
from Modo_Nucleo.nucleo import *
# from Modo_Nucleo.nucleo import isNucleo
# from Modo_Nucleo.nucleo import ReadFromFile


def UserWriteEndFile(message):
    print('nope')


def UserSwitchSystem(state):
    Thread(target=SwitchSystem, args=(state,)).start()
    # else:
    #     Thread(target)

    # process = multiprocessing.Process(target=SwitchSystem, args=(True,))
    # process.start()
    # jobs.append(process)
    # SwitchSystem(True)


def UserReadFromFile(initial=False, final=False):
    if not CheckState():
        UserSwitchSystem(True)

    job = Job('Teste')
    global jobs
    jobs.append(job)
    print('added job')


def TestLib():
    print("libTested!")


def UserChangeTestVar():
    ChangeTestVar('TESTED')


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
