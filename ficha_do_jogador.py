#Algoritmo construído 03/02/23 - Aula de Python -- FUNÇÕES
def ficha(jog, gol):
    print(f'O {jog} fez {gol} gols no campeonato')
#Programa pricipal
n = input('Nome do Jogador: ')
g = input('Números de Gols: ')
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gol=g)
else:
    ficha(n, g)