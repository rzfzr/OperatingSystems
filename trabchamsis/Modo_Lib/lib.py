import os
import sys
sys.path.insert(0, os.getcwd())  # adds current dir to import from

from Modo_Nucleo.nucleo import *
# from Modo_Nucleo.nucleo import isNucleo
# from Modo_Nucleo.nucleo import ReadFromFile


def UserWriteEndFile(message):
    print('nope')


# def UserSwitchSystem():
#     process = multiprocessing.Process(target=SwitchSystem, args=(True,))
#     # jobs.append(process)
#     process.start()
#     # SwitchSystem(True)


def UserReadFromFile(initial=False, final=False):
    # print('UserRead isOn:', isOn)

    # if not isOn:
    #     UserSwitchSystem()

    job = Job('Teste')
    jobs.append(job)
    print('added job')


def TestLib():
    print("libTested!")


if __name__ == '__main__':
    print('(Lib) Modo Nucleo:', isNucleo)
    # print(ReadFromFile(2, 5))

    UserReadFromFile()
    # WriteEndFile('zeros e uns')
