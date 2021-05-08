import random

def cria_baralho():
    baralho = []
    valor = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    naipes = ["♠", "♥", "♦", "♣"]
    for num in valor:
        for naipe in naipes:
            baralho.append(str(num)+naipe)
    return baralho


deck = cria_baralho()
random.shuffle(baralho)

print(deck)
