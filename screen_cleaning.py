import os

def cls():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

cls(); print('Screen is cleared. / Экран очищен.')
