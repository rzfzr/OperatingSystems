fileName = "Modo_Nucleo/binary.txt"
isNucleo = False


def WriteEndFile(message):
    file = open(fileName, "a")
    file.write(message)


def ReadFromToPosition(initial, final):
    file = open(fileName, "r").read()
    return file[initial:final]


# print file.read()


# if __name__ == '__main__':
#     isNucleo = True
#     print('Modo Nucleo:', isNucleo)
#     # print(ReadFromToPosition(2, 5))
#     WriteEndFile('zeros e uns')
