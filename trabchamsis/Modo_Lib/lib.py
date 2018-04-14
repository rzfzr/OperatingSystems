import os
import sys
sys.path.insert(0, os.getcwd())  # adds current dir to import from

# from Modo_Nucleo.nucleo import ReadFromToPosition
from Modo_Nucleo.nucleo import *

if __name__ == '__main__':
    print('Modo Nucleo:', isNucleo)
    print(ReadFromToPosition(2, 5))
    # WriteEndFile('zeros e uns')
