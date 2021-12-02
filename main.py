from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print("""SUAS OPÇÕES:
[0] PEDRA
[1] PAPEL
[2] TESOURA""")
jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(0.7)
print('KEN')
sleep(0.7)
print('PO')
sleep(0.7)
print('-=' * 10)
print('Computador escolheu =  {}'.format(itens[computador]))
print('Jogador escolheu = {}'.format(itens[jogador]))
print('-=' * 10)

if computador == 0:  #computador jogou pedra
    if jogador == 0:
        print('EMPATE')

    elif jogador == 1:
        print('JOGADOR VENCEU')

    elif jogador == 2:
        print('COMPUTADOR VENCEU')
    else:
        print('JOGADA INVÁLIDA')
elif computador == 1: #computador jogou papel
    if jogador == 0:
        print('COMPUTADOR VENCEU')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCEU')
    else:
        print('JOGADA INVÁLIDA')
elif computador == 2: #computador jogou tesoura
    if jogador == 0:
        print('JOGADOR VENCEU')

    elif jogador == 1:
        print('COMPUTADOR VENCEU')

    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA')