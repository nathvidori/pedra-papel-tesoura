# Pedra, papel ou tesoura:

from random import randint
from time import sleep
print('Bem vindo(a) ao jogo!')

sleep(1)

opções = ['pedra', 'papel', 'tesoura'] #variável que contem as opções em uma lista para o computador jogar

while True:
    jogador = str(input('Escolha pedra, papel ou tesoura! Se quiser sair do programa digite "sair". ')).lower()

    if jogador == 'sair':
        break

    if jogador not in opções: # se a resposta do jogador não estiver entre as opções o programa vai continuar pedindo para escolher uma opção
        print('Digite algo válido!')
        continue

    # o randint vai escolher aleatoriamente os numeros 0, 1 ou 2:
    computador  = randint(0, 2)
    computador_opções = opções[computador] # onde ocorre a conversão dos números (0, 1 e 2) para as opções

    if jogador == computador_opções:
        print('Empate!')
    elif jogador == 'Pedra' and computador_opções == 'Tesoura': # and é uma operação lógica
        print(f'Você escolheu "{jogador}" e o computador escolheu "{computador_opções}". Você ganhou!')
    elif jogador == 'Papel' and computador_opções == 'Pedra':
        print(f'Você escolheu "{jogador}" e o computador escolheu "{computador_opções}". Você ganhou!')
    elif jogador == 'Tesoura' and computador_opções == 'Papel':
        print(f'Você escolheu "{jogador}" e o computador escolheu "{computador_opções}". Você ganhou!')
    else:
        print(f'Você escolheu "{jogador}" e o computador escolheu "{computador_opções}". Você perdeu!')



# lower() é um método embutido usado para manipulação de strings. Os métodos lower() retornam a string em minúsculas da string fornecida.
# Ele converte todos os caracteres maiúsculos em minúsculos. Se não houver caracteres maiúsculos, ele retornará a string original
