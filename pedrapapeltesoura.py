
from time import sleep
import random


def jogo():

    placarplay1 = 0
    placarcom = 0

    while True:
        try:
            print('Faca sua escolha...')
            player1 = input('Pedra, Papel ou Tesoura? ').lower()
            opcoes = ['pedra', 'papel', 'tesoura']
            print('computador joga...')
            sleep(2)
            player2 = random.choice(opcoes)

            if player1 == 'pedra':
                if player2 == 'pedra':
                    print(
                        f'Você: {player1} X COM: {player2} - Houve um empate!')

                elif player2 == 'papel':
                    print(
                        f'Você: {player1} X COM: {player2} - Computador venceu!')
                    placarcom += 1
                elif player2 == 'tesoura':
                    print(f'Você: {player1} X COM: {player2} - Você venceu!')
                    placarplay1 += 1

            if player1 == 'papel':
                if player2 == 'pedra':
                    print(f'Você: {player1} X COM: {player2} - Você venceu!')
                    placarplay1 += 1
                elif player2 == 'papel':
                    print(
                        f'Você: {player1} X COM: {player2} - Houve um empate!')

                elif player2 == 'tesoura':
                    print(
                        f'Você: {player1} X COM: {player2} - Computador venceu!')
                    placarcom += 1

            if player1 == 'tesoura':
                if player2 == 'pedra':
                    print(
                        f'Você: {player1} X COM: {player2} - Computador venceu!')
                    placarcom += 1
                elif player2 == 'papel':
                    print(f'Você: {player1} X COM: {player2} - Você venceu!')
                    placarplay1 += 1
                elif player2 == 'tesoura':
                    print(
                        f'Você: {player1} X COM: {player2} - Houve um empate!')

            print(f'Placar: Você[ {placarplay1} ] X [ {placarcom} ] COM')
            print('')
            print(f'Deseja continuar a jogar? ')
            conti = input('[s] / [n]').lower()
            if conti[0] == 's':
                continue
            elif conti[0] == 'n':
                print('#### Até a proxima ####')
                print(
                    f'## Placar Final : Você[ {placarplay1} ] X [ {placarcom} ] COM ##')
                if placarplay1 > placarcom:
                    print('PARABÉNS VOCE VENCEU!!!')
                elif placarcom > placarplay1:
                    print('INFELIZMENTE VOCE PERDEU!!!')
                else:
                    print('JOGO EMPATADO!')
                break
            else:
                print('digite dados válidos!!')
                continue

        except:
            print('digite dados válidos!!')


def inicio():
    try:
        print(40 * '#')
        print(9 * '#', 'BEM-VINDO AO JOKENPY', 9 * '#')
        print(40 * '#')
        print('<<< DESEJA INICIAR O GAME? >>>')
        inicio = input('[S]IM / [N]AO ').lower()
        if inicio[0] == 's':
            print('vamos comecar...')
            sleep(2)
            jogo()

        elif inicio[0] == 'n':
            print("ok até a próxima!!")
        else:
            print('digite dados validos...')

    except:
        print('digite dados validos...')


inicio()
