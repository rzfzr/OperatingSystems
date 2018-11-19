# import collections
# import sys
# import time
# import random
from enum import Enum
# import datetime
# import threading
# from threading import Thread
# import os
# import multiprocessing

users = []
fileID=0
currentUser=''

# class Level(Enum):
#     READ    = 1
#     WRITE   = 2
#     EXECUTE = 3

class Mode(Enum):
    READ    = 1
    WRITE   = 2
    EXECUTE = 3

class Permission():
    def __init__(self,owner,group,others):
        self.owner=owner
        self.group=group
        self.others=others

    def __str__(self):
        return (self.owner + self.group + self.others)

defaultPermission = Permission('rwx','r','') #0740

class User():
    def __init__(self,id,group):
        self.id = id        
        self.group = group
        self.files = []
    
    def createFile(self,name,permission=defaultPermission):
        self.files.append(File(name,self.id,self.group,permission))

class File():
    def __init__(self,name,id,group,permission):
        global fileID
        self.id=fileID
        fileID+=1
        self.name=name
        self.owner=id
        self.group =group
        self.permission=permission
    # def __str__(self):
    #     return self.name
    # def __repr__(self):    
    #     return self.name


def PrintUsers():
    for user in users:
        print('User ID:',user.id,'  Group:',user.group,'    Files(', len(user.files) ,'):', user.files)


def GetAllFiles():
    files = []
    for user in users:
        for file in user.files:
            files.append(file)
    # files.sort()
    return files;

def PrintFiles():
    
    for file in GetAllFiles():
        print('File ID:', file.id,'Name:',file.name,'           Owner:',file.owner,'Group:',file.group, 'Permissions:', file.permission)

def CheckPermissions(user, file, mode):
    # print('mode',mode)
    # print('current id group',user.id,user.group, '  file id owner group', file.id, file.owner, file.group)
    if user.id == file.owner:
        print('Usuario Dono')
        if mode in file.permission.owner:
            print('com direito de acesso')
        else:
            print('sem direito de acesso')
    elif user.group == file.group:
        print('Usuario do mesmo grupo')
        if mode in file.permission.group:
            print('com direito de acesso')
        else:
            print('sem direito de acesso')
    else:
        print('Usuario outro')
        if mode in file.permission.others:
            print('com direito de acesso')
        else:
            print('sem direito de acesso')
    # if mode == Mode.READ:
    # print('Usuario nao tem acesso')

if __name__ == '__main__':

    user0 = User(0,'A')
    user1 = User(1,'B')
    user2 = User(2,'A')

    user0.createFile('teste0.txt')

    # print(user0.files[0])
    

    user0.createFile('teste1.txt')
    user1.createFile('baixarRAM.html')
    user2.createFile('opentray.bat')
    user2.createFile('closetray.bat',permission=Permission('rwx','rwx','rwx'))

    currentUser=user0
    users.append(user0)
    users.append(user1)
    users.append(user2)

    print('AccessControl')
 
    sel ='0'
    while sel !='-1':

        print('\n\n\n')

        print('Credenciado como usuario id:', currentUser.id, 'Grupo:', currentUser.group )
        print('1 = Lista Usuarios')
        print('2 = Lista Arquivos')
        print('3 = Ler Arquivo')
        print('4 = Escrever Arquivo')
        print('5 = Executar Arquivo')
        print('6 = Alterar Permissoes de Arquivo*')
        print('7 = Trocar de Usuario*')

        # print('fileID',fileID)
        sel = input ("Selecione: ")
        print('\n\n\n')
        
        
        if sel == '1':
            PrintUsers()
        elif sel == '2':
            PrintFiles()
        elif sel == '3' or sel == '4' or sel =='5':
            PrintFiles()
            # sel=''
            selFile = input ("Selecione o id do arquivo: ")
            # selFile = File('tt',1,'B',defaultPermission)
            for file in GetAllFiles():
                if file.id == int(selFile):
                    # print('found')  
                    fileSelected = file

            if sel == '3':
                CheckPermissions(currentUser,fileSelected,'r')
            elif sel == '4':
                CheckPermissions(currentUser,fileSelected,'w')
            else:
                CheckPermissions(currentUser,fileSelected,'x')


        else:
            print("Tente novamente")




