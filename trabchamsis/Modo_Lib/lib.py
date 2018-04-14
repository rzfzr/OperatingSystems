import os
import sys
sys.path.insert(0, os.getcwd())  # adds current dir to import from

from Modo_Nucleo.nucleo import *
# from Modo_Nucleo.nucleo import isNucleo
# from Modo_Nucleo.nucleo import ReadFromFile


def UserWriteEndFile(message):
    if not isOn:
        SwitchSystem(True)


def TestLib():
    print("libTested!")


if __name__ == '__main__':
    print('Modo Nucleo:', isNucleo)
    print(ReadFromFile(2, 5))
    # WriteEndFile('zeros e uns')
