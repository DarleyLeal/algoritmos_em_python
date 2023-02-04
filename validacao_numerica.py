def leiaInt():
    while True:
        numero = input('Digite um numero: ')
        if numero.isnumeric():
            numero = int(numero)
            break
        else:
            print('\033[1;33mErro, digite um número\033[m')
    return f'Você digitou o número {numero} e ele é inteiro'


print(leiaInt())
