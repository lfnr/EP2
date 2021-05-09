import random

def cria_baralho():
    baralho = []
    valor = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    naipes = ["♠", "♥", "♦", "♣"]
    for num in valor:
        for naipe in naipes:
            baralho.append(str(num)+naipe)
    return baralho

def extrai_valor(carta):
    if carta[0] == "1":
        valor = carta[0] + carta[1]
    else:
        valor = carta[0]
    return valor

def extrai_naipe(carta):
    if carta[0] == "1":
        naipe = carta[2]
    else:
        naipe = carta[1]
    return naipe

def lista_movimentos_possiveis(baralho, indice):
    valor = extrai_valor(baralho[indice])
    naipe = extrai_naipe(baralho[indice])
    movimentos = []
    if indice == 0:
        return movimentos
    if indice > 0:
        if valor in baralho[indice -1] or naipe in baralho[indice-1]:
            movimentos.append(baralho[indice])
    if indice >= 3:
        if valor in baralho[indice -3] or naipe in baralho[indice-3]:
            movimentos.append(baralho[indice-2])
    return movimentos


deck = cria_baralho()
random.shuffle(deck)

print(deck)
