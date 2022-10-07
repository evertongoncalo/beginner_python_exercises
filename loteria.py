import random
from time import sleep


def Loto():

    n = ([i for i in range(1, 26)])
    x = random.sample(n, k=5)

    rep = 1
    cc = []
    while rep < 6:
        var = int(input(f'Digite o {rep}º numero: '))
        if var <= 0 or var >= 26:
            print('Digite numeros entre 0 e 25')
            if rep >= 1:
                rep -= 1
        else:
            cc.append(var)
        rep += 1

    print('Sorteando...')
    sleep(3)

    v = list(set(x) & set(cc))

    print('Seus números escolhidos foram: {}'.format(cc))
    print('Números sorteados foram: {}'.format(x))
    print(40*'-')
    print('Números que acertou foram: {}'.format(v))
    print(40*'-')

    if len(v) == 5:
        print('Parabéns você ganhou o 1º premio')
    elif len(v) == 4:
        print('Parabéns você ganhou o 2º premio')
    elif len(v) == 3:
        print('Parabéns você ganhou o 3º premio')
    else:
        print('Você não ganhou nada!!!')


def start():

    print('''\u001b[32m                         .-. .-.
                        (   |   )
                      .-.:  |  ;,-.
                     (_ __`.|.'_ __)
                     (    ./Y\.    )
                      `-.-' | `-.-'
                            |
                            |   \u001b[0m''')

    print('<< DESEJA INICIAR A LOTERIA? >> ')
    iniciar = input('Digite Sim ou Nao: ').lower().strip()
    if iniciar[0] == 's':
        print('OK! Vamos comecar!!')
        print(40*'-')
        print('1º premio: 5 acertos\n2º premio: 4 acertos\n3º premio: 3 acertos\n')
        print('Boa Sorte!')
        sleep(2)
        print(40*'-')
        print('Escolha 5 numeros de 1 a 25: ')

        Loto()
    elif iniciar[0] == 'n':
        print('Fica pra próxima!!')

    else:
        print('Digite algo valido')


start()