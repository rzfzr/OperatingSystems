import os
import sys
sys.path.insert(0, os.getcwd())  # adds current dir to import from

# from Modo_Nucleo.nucleo import ReadFromToPosition
from Modo_Lib.lib import *


userName = ''


def Menu():  # Your menu design here

    userName = input('Enter your name:')

    choice = ''
    while choice is not '0':

        print(8 * '-', 'MENU', 8 * '-', '\n',
              '0. Exit', '\n',
              '1. Write', '\n',
              '2. Read', '\n',
              22 * '-')
        choice = input('Enter your choice [1-5]: ')

        if choice == '1':
            print('Menu 1 has been selected')
        elif choice == '2':
            print('Menu 2 has been selected')
        elif choice == '3':
            print('Menu 3 has been selected')
        elif choice == '4':
            print('Menu 4 has been selected')
        elif choice == '0':
            print('Menu 5 has been selected')
        else:
            input('Wrong option selection. Enter any key to try again..')


if __name__ == '__main__':

    Menu()

    # isNucleo = True
    # print('Modo Nucleo:', isNucleo)
    # print(ReadFromFile(2, 5))

    # TestLib()

    # WriteEndFile('zeros e uns')
