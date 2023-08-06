from components.verificar import verificar
from components.print_game import print_game

tabuleiro = [
    ['    ', '    ', '    ', '    '],
    ['    ', '    ', '    ', '    '],
    ['    ', '    ', '    ', '    '],
    ['    ', '    ', '    ', '    ']
    ]
print_game(tabuleiro)
pecas = ['AQGF', 'AQPF', 'ARGF', 'ARPF', 'VQGF', 'VQPF', 'VRGF', 'VRPF', 'AQGN', 'AQPN', 'ARGN', 'ARPN', 'VQGF', 'VQPF', 'VRGF', 'VRPF']
jogador = 1

while True:
    print('As peças que estão disponíveis possuem as seguintes características:\n')
    print('Azul: A\nVermelho: V\nQuadrada: Q\nRedonda: R\nGrande: G\nPequena: P\nFurada: F\nNão furada: N\n\n')
    print('Exemplo: AQGF\n')
    print('A peça AQGF é uma peça azul, quadrada, grande e furada\n')
    while True:
        #jogador 1 escolhe a peça para o jogador 2 jogar
        print(f'As peças disponíveis são: {pecas}\n')
        peca = input('Qual peça escolhe pro seu adversário? ')
        print('\n')
        if peca in pecas:
            break
        else:
            print('Peça inválida\n')
    pecas.remove(peca)

    if jogador == 1:
        jog = 2
    else:
        jog = 1
    print(f'Jogador {jogador} escolheu a peça {peca} para o jogador {jog} jogar!\n')
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

    tabuleiro[x][y] = f'{peca}'

    print_game(tabuleiro)
    if verificar(tabuleiro) == 'Deu velha!':
        print('Deu velha!')
        break
    elif verificar(tabuleiro) != True:
        print(f'{jogador} venceu juntando 4 peças com a característica {verificar(tabuleiro)}!')
        break



print('\nFim de jogo. Obrigado por jogar!\n')
