import random

def jogada(opcao, arr):
    
    if opcao == 1: #escolher peca
        numero_aleatorio = random.randint(0, len(arr)-1)
    else:
        x = random.randint(0, 3)
        y = random.randint(0, 3)
        while arr[x][y] != '    ':
            x = random.randint(0, 3)
            y = random.randint(0, 3)
        return x, y