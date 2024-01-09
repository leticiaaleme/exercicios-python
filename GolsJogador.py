dados = dict()
gols = []
totalgols = 0
dados['Nome'] = str(input("Nome do Jogador: "))
partidas = int(input(f"Quantas partidas {dados['Nome']} jogou? "))
for c in range(0, partidas):
    gol = int(input(f"Quantos gols na partida {c}? "))
    totalgols += gol
    gols.append(gol)
dados['Gols']= gols[:]
dados['Total de Gols'] = totalgols
print(dados)
print("-=" * 20)
for k, v in dados.items():
    print(f"O campo {k} tem valor {v}.")
print("-=" * 20)
print(f"O jogador {dados['Nome']} jogou {partidas} partidas.")
for c in range (0, partidas):
    print(f" => Na partida {c}, fez {dados['Gols'][c]} gols.")
print(f"Foi um total de {totalgols} gols.")
