import quarto_JxJ
import quarto_JxIA

print('Bem vindo ao jogo de Quarto!')
print('Selecione o estilo de jogo:')
print('1 - Humano vs Humano')
print('2 - Humano vs IA')
op = int(input('Digite o número da opção desejada: '))

if op == 1:
    quarto_JxJ.jogar()
elif op == 2:
    quarto_JxIA.jogar()
else:
    print('Opção inválida!')