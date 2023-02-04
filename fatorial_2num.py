def fatorial(num=1, show=False):
    """
    :param num:  Recebe número fora do escopo global
    :param show: mostra ou não a conta
    :return: retorna valores
    """

    print(f'\033[1;33mFATORIAL DO NÚMERO\033[m')
    fat = 1
    for i in range(num, 0, -1):
        if show:
            print(f'{i} x', end=' ')
        fat *= i
    return f'{numero} = {fat}'


numero = int(input('Digite um número: '))
print(f'A fatorial de {fatorial(numero, show=True)}')

