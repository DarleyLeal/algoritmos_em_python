from random import randint
from time import sleep
def sorteia(lista):
    print('\033[1;33mSorteando 5 valores da lista:\033[m')
    for cont in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n}  ', end='')
        sleep(0.3)

def somaPar(lista):
    print('\033[1;34m\nSorteando números pares na lista:\033[m')
    soma = 0
    for par in lista:
        if par % 2 == 0:
            soma += par
            sleep(0.3)
    print(f'\033[1;31mSomando os valores pares da seguinte lista: {lista}, temos {soma}\033[m')

# Main da função:
numeros = list()
sorteia((numeros))
somaPar(numeros)
# Fim da função:
