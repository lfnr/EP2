import random

def cria_baralho():
    baralho = []
    valor = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    for i in range(13):
        baralho.append([i+1, "♠"])
    for i in range(13):
        baralho.append([i+1, "♥"])
    for i in range(13):
        baralho.append([i+1, "♦"])
    for i in range(13):
        baralho.append([i+1, "♣"])
    return baralho

def lista_movimentos_possiveis(baralho, indice):
    numero = baralho[indice-1][0]
    naipe = baralho[indice-1][1]
    movimentos = []
    if indice == 1:
        return movimentos
    if indice > 1:
        if numero == baralho[indice-2][0] or naipe == baralho[indice-2][1]:
            movimentos.append(baralho[indice-2])
    if indice >= 4:
        if numero == baralho[indice-4][0] or naipe == baralho[indice-4][1]:
            movimentos.append(baralho[indice-4])
    return movimentos


deck = cria_baralho()
random.shuffle(deck)

print(deck)
