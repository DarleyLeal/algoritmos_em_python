s = input('Frase: ')

def realce(s):
    s.capitalize()
    print('+'+'-' * len(s) + '+')
    print('+'+'-' * len(s) + '+')
    print(f'{s:^}')
    print('+'+'-' * len(s) + '+')
    print('+'+'-' * len(s) + '+')

realce(s)