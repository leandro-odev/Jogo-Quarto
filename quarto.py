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
jogador = 1

while True:
    
    while True:
        #jogador 1 escolhe a peça para o jogador 2 jogar
        print('As peças possuem as seguintes características:\n')
        print('Azul: A\nVermelho: V\nQuadrada: Q\nRedonda: R\nGrande: G\nPequena: P\nFurada: F\nNão furada: N\n\n')
        print('Exemplo: AQRG\n')
        print('A peça AQRG é uma peça azul, quadrada, grande e furada\n')
        peca = input('Qual peça escolhe pro seu adversário? ')
        print('\n')
        if ('A' in peca or 'V' in peca) and ('Q' in peca or 'R' in peca) and ('G' in peca or 'P' in peca) and ('F' in peca or 'N' in peca):
            break
        else:
            print('Peça inválida\n')

    print(f'Jogador {jogador} escolheu a peça {peca} para o outro jogador jogar!\n')
    if jogador == 2:
        jogador = 1
    elif jogador == 1:
        jogador = 2
    
    
    while True:
        x = int(input('Digite a linha que deseja colocar a peça: '))
        y = int(input('Digite a coluna que deseja colocar a peça: '))
        if x > 3 or x < 0 or y > 3 or y < 0 or tabuleiro[x][y] != '    ':
            print('Posição inválida\n')
        else:
            break

    tabuleiro[x][y] = f'{peca}   '

    print_game(tabuleiro)
    if verificar(tabuleiro) == 'Deu velha!':
        print('Deu velha!')
        break
    elif verificar(tabuleiro) != True:
        print(f'{jogador} venceu juntando 4 peças com a característica {verificar(tabuleiro)}!')
        break



print('\nFim de jogo. Obrigado por jogar!\n')
