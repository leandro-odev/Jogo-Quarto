import random

def jogada(opcao, arr):
    
    if opcao == 1: #escolher peca
        index_random = random.randint(0, len(arr)-1)
        return index_random
    else:
        x = random.randint(0, 3)
        y = random.randint(0, 3)
        while arr[x][y] != '    ':
            x = random.randint(0, 3)
            y = random.randint(0, 3)
        return x, y
