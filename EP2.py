import random

def cria_baralho():
    baralho = []
    naipes = ["♠", "♥", "♦", "♣"]
    for valor in range(1, 14):
        for naipe in naipes:
            baralho.append(str(valor)+naipe)
return baralho

deck = cria_baralho()
random.shuffle(baralho)

print(baralho)
