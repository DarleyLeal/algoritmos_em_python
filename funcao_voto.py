def voto(ano):
    from datetime import date
    ano_atual = date.today().year
    idade = (ano_atual - ano)
    if idade < 16:
        return f'Com {idade} anos: você ainda não vota!'
    elif 16 <= idade < 18 or idade >= 65:
        return f'Com {idade} anos: voto é OPCIONAL'
    else:
        return f'Com {idade} anos: voto é OBRIGATORIO'

ano_nascimento = int(input('Em que ano você nasceu? '))
print(voto(ano_nascimento))