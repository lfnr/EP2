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

deck = cria_baralho()
random.shuffle(deck)

print(deck)
