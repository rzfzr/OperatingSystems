import os
import sys


sys.path.insert(0, os.getcwd())  # adds current dir to import from

from Modo_Nucleo.nucleo import *


import threading
from threading import Thread
# from Modo_Nucleo.nucleo import isNucleo
# from Modo_Nucleo.nucleo import ReadFromFile


def UserWriteEndFile(message):
    print('nope')


def UserSwitchSystem(on=True):
    Thread(target=SwitchSystem).start()
    # process = multiprocessing.Process(target=SwitchSystem, args=(True,))
    # process.start()
    # jobs.append(process)
    # SwitchSystem(True)


def UserReadFromFile(initial=False, final=False):
    print('UserRead isOn:', isOn)
    if not isOn:
        UserSwitchSystem()

    job = Job('Teste')
    global jobs
    jobs.append(job)
    print('added job')


def TestLib():
    print("libTested!")


def UserChangeTestVar():
    ChangeTestVar('TESTED')


if __name__ == '__main__':
        # UserSwitchSystem(True)
    print('(Lib) Modo Nucleo:', isNucleo)
    # print(ReadFromFile(2, 5))
    # UserReadFromFile()
    # print(len(jobs))

    # process = multiprocessing.Process(target=SwitchSystem, args=(True,))
    # process.start()
    # SwitchSystem(True)

    # time.sleep(6)

    # UserChangeTestVar()
    # WriteEndFile('zeros e uns')
