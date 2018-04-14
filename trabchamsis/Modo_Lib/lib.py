import os
import sys
sys.path.insert(0, os.getcwd())
# sys.path.insert(0, '..')  # imports from parent folder
# sys.path.insert(0, '.././Modo_Nucleo')
# from Modo_Nucleo.nucleo import ReadFromToPosition

from Modo_Nucleo.nucleo import *

if __name__ == '__main__':
    print('Modo Nucleo:', isNucleo)
    print(ReadFromToPosition(2, 5))
    # WriteEndFile('zeros e uns')
