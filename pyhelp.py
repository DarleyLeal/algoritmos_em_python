# programa ensina a colocar cores na saída do console Python 04/02/23
from time import sleep
c = ('\033[m',        # 0 - Sem cores
    '\033[1;30;41m',  # 1 - Vermelho
    '\033[1;30;42m',  # 2 - Verde
    '\033[1;30;43m',  # 1 - Amarelo
    '\033[1;30;44m',   # 0 - Azul
    '\033[1;30;45m',  # 1 - Roxo
    '\033[7;30m',      # 0 - Branco
     )


def ajuda(com):
    titulo(f'Acessando o manual\'{com}\'', 4)
    print(c[6], end='')
    print
    help(com)
    print(c[0], end='')
    sleep(2)


def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[6], end='')
    print('=' * tam)
    print(f'{msg}')
    print('=' * tam)
    print(c[0], end='')
    sleep(2)


# programa principal
titulo('SISTEMA DE AJUDA PYHELP', 2)
comando = ''
while True:
    comando = input('Função ou Biblioteca: ')
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
    print('ATÉ LOGO!', 1)
