import os
import sys
sys.path.insert(0, os.getcwd())  # adds current dir to import from

# from Modo_Nucleo.nucleo import ReadFromToPosition
from Modo_Lib.lib import *

userName = ''


def Menu():  # Your menu design here
    global userName
    userName = input('Enter your name:')
    selection = ''
    while selection is not '0':
        print(8 * '-', 'MENU', 8 * '-', '\n',
              '0. Sair', '\n',
              '1. Escrita', '\n',
              '2. Leitura', '\n',
              22 * '-')
        selection = input('Sua escolha (0-2): ')
        if selection == '1':
            selection = input('Digite a informacao: ')
            UserWriteEndFile(selection)

        elif selection == '2':
            print(5 * '-', 'Leitura', 5 * '-', '\n',
                  '0. Sair', '\n',
                  '1. Ler dentro de um intervalo', '\n',
                  '2. Ler todo o arquivo', '\n',
                  22 * '-')

            selection = input('Sua Escolha (0-2): ')
            if(selection == '2'):
                UserReadFromFile()

        elif selection == '3':
            print('Menu 3 has been selected')
        elif selection == '4':
            print('Menu 4 has been selected')
        elif selection == '0':
            print('Menu 5 has been selected')
        else:
            input('Nada selecionado, tente novamente...')


if __name__ == '__main__':

    Menu()

    # isNucleo = True
    # print('Modo Nucleo:', isNucleo)
    # print(ReadFromFile(2, 5))

    # TestLib()

    # WriteEndFile('zeros e uns')
