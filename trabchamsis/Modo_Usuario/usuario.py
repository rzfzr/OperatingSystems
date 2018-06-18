import os
import sys
import time
import random
sys.path.insert(0, os.getcwd())  # adds current dir to import from
# from Modo_Nucleo.nucleo import ReadFromToPosition
from Modo_Lib.lib import *
# userName = ''
botsPath = "bots/"
userNames = []
speed = 1
botsOn = False



def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def Menu():  # Your menu design here
    # global userName
    userName = input('Enter your name: ')

    selection = ''
    while selection is not '0':
        print('\n', 8 * '-', 'MENU', 8 * '-', '\n',
              '0. Saida', '\n',
              '1. Escrita', '\n',
              '2. Leitura', '\n',
              22 * '-')
        selection = input('Sua escolha: ')

        if selection == '0':
            print('Saindo')
            UserSwitchSystem(False)

        elif selection == '1':
            selection = input('Digite a informacao: ')
            confirmation = input(
                'Escrever "%s", tem certeza? s/n: ' % selection)
            if confirmation == 's':
                UserWriteEndFile(userName, selection)

        elif selection == '2':
            print('\n', 5 * '-', 'Leitura', 5 * '-', '\n',
                  '9. Voltar', '\n',
                  '1. Ler dentro de um intervalo', '\n',
                  '2. Ler todo o arquivo', '\n',
                  22 * '-')
            selection = input('Sua escolha: ')
            if(selection == '9'):
                print('Voltando\n')
            elif(selection == '1'):
                initial = input('Posicao initial: ')
                final = input('Posicao final: ')
                UserReadFromFile(userName, int(initial), int(final)+1)
            elif(selection == '2'):
                UserReadFromFile(userName)

        elif selection == '666':
            UserSwitchSystem(False)
            cls()
            for i in range(51):
                sys.stdout.write('\r')
                sys.stdout.write("[%-10s] %d%%" % ('='*i, 2*i))
                sys.stdout.write("helpmepleasegodno")
                sys.stdout.flush()
                time.sleep(0.017)
            cls()
            print('\n', 5 * '-', 'UserSimulator2000', 5 * '-', '\n',
                  '9. Voltar', '\n',
                  '1. Simular', '\n',
                  29 * '-')
            selection = input('Sua escolha: ')

            if(selection == '9'):
                print('Voltando\n')
            elif(selection == '1'):
                lowUsers = input('Numero de usuarios normais: ')
                for i in range(int(lowUsers)):
                    userNames.append(input('Nome do usuario n%s: ' % i))
                    LogBot(userNames[i], '\nInicializado com sucesso\n')
                highUsers = input('Numero de usuarios root: ')
                userNames.append('root')
                LogBot('root', '\nInicializado com sucesso\n')

                print('Abra os "terminais"!')
                global speed
                speed = input('Velocidade (1-10): ')
                speed = 10-int(speed)
                SwitchBots(True)

                temp = input('Pare os bots')
                SwitchBots(False)

        else:
            input('Tente novamente: ')


def SwitchBots(on):
    global botsOn
    botsOn = on
    time.sleep(2)
    if on:
        for userName in userNames:
            time.sleep(2)
            Thread(target=SingleBot, args=(userName,)).start()
            # SingleBot(userName)
    else:
        UserSwitchSystem(False)


def SingleBot(userName):
    # print(botsOn)
    # print(speed)
    if botsOn:
        # LogBot(userName, 'Requisicao de leitura \n')
        LogBot(userName, "\n\nRequisicao de leitura as %s \n" %
               datetime.datetime.now().strftime("%H:%M:%S"))

        UserReadFromFile(userName, isBot=True)
        # LogBot(userName, 'testing\n')

        speedTemp = speed
        if userName == 'root':
            speedTemp = speed+5
        time.sleep(random.randint(speedTemp, speedTemp+3))
        SingleBot(userName)


def LogBot(userName, message):
    file = open(botsPath+userName+'.txt', "a")
    file.write(message)
    # return 'Escrito com sucesso'


if __name__ == '__main__':
    Menu()
    # isNucleo = True
    # print('Modo Nucleo:', isNucleo)
    # print(ReadFromFile(2, 5))
    # TestLib()
    # WriteEndFile('zeros e uns')
