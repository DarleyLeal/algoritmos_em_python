
def notas(*n, sit=False):
    """
    :param n: valor de notas recebidas pela função notas
    :param sit: situação: retorna caso seja pedido, senão programa funciona, mas sem retornar resultado
    :return: retorna valores das variaveis
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n) / len(n)
    if sit:
        if r['média'] >= 7:
            r['situação'] = 'BOA'
        elif r['média'] >= 5:
            r['situação'] = 'RUIM'
        else:
            r['situação'] = 'PÉSSIMA'
    return n


nota = notas(2, 8.5, 9.4, 10, sit=True)
print(nota)