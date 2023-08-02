from components.verificar import verificar
import colorama

colorama.init()
'''print(colorama.Fore.RED + 'some red text' + colorama.Style.RESET_ALL)
print('automatically back to default color again')
print(colorama.Fore.GREEN + 'and with a green background' + colorama.Style.RESET_ALL)'''

def colorir(var):
    if 'A' in var:
        #print(colorama.Fore.BLUE + var + colorama.Style.RESET_ALL)
        return colorama.Fore.LIGHTBLUE_EX + var + colorama.Style.RESET_ALL
    elif 'V' in var:
       #print(colorama.Fore.RED + var + colorama.Style.RESET_ALL)
       return colorama.Fore.RED + var + colorama.Style.RESET_ALL
    else:
        #print(' ')
        return '    '

def print_game(matriz):
    print(f'\n----------------------------\n {colorir(matriz[0][0])} | {colorir(matriz[0][1])} | {colorir(matriz[0][2])} | {colorir(matriz[0][3])} \n----------------------------\n {colorir(matriz[1][0])} | {colorir(matriz[1][1])} | {colorir(matriz[1][2])} | {colorir(matriz[1][3])} \n----------------------------\n {colorir(matriz[2][0])} | {colorir(matriz[2][1])} | {colorir(matriz[2][2])} | {colorir(matriz[2][3])} \n----------------------------\n {colorir(matriz[3][0])} | {colorir(matriz[3][1])} | {colorir(matriz[3][2])} | {colorir(matriz[3][3])} \n----------------------------\n')


tabuleiro = [
    ['    ', '    ', '    ', '    '],
    ['    ', '    ', '    ', '    '],
    ['    ', '    ', '    ', '    '],
    ['    ', '    ', '    ', '    ']
    ]

while True:
    peca = input('Qual peça escolhe pro seu adversário? ')
    print('\n')

    while True:
        x = int(input('Digite a linha: '))
        y = int(input('Digite a coluna: '))
        if x > 3 or y > 3 or tabuleiro[x][y] != '    ':
            print('Posição inválida\n')
        else:
            break

    tabuleiro[x][y] = f'{peca}   '

    print_game(tabuleiro)
    if verificar(tabuleiro) == 'Deu velha!':
        print('Deu velha!')
        break
    elif verificar(tabuleiro) != True:
        print(f'{verificar(tabuleiro)} venceu!')
        break
        
    
    
