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
    if indice > 1:
        if numero == baralho[indice-2][0] or naipe == baralho[indice-2][1]:
            movimentos.append(baralho[indice-2])
    if indice >= 4:
        if numero == baralho[indice-4][0] or naipe == baralho[indice-4][1]:
            movimentos.append(baralho[indice-4])
    return movimentos

def teste_mao(mao):
    for i in range(len(mao)):
        if lista_movimentos_possiveis(mao, i+1) != []:
            return True
    return False

def printa_carta(carta):
    valor = carta[0]
    if carta[0] == 11:
        valor = "J"
    if carta[0] == 12:
        valor = "Q"
    if carta[0] == 13:
        valor = "K"
    if carta[0] == 1:
        valor = "A"
    print(str(valor) + carta[1])

def empilha(mao, origem, destino):
    mao[destino-1] = mao[origem-1]
    mao.pop(origem-1)
    return mao
    
    
#Interface ==================================================================================

deck = cria_baralho()
random.shuffle(deck)
mao = deck[0:4]

while not teste_mao(mao):
    deck = cria_baralho()
    random.shuffle(deck)
    mao = deck[0:4]
    break

resp = input("Você gostaria de começar um jogo? ")

if resp == "sim":
    for carta in mao:
        printa_carta(carta)

origem = int(input("Qual a posição da carta que gostaria de mover?(1-4) "))

while origem not in range(1, 5):
    print("Tente outro número")
    origem = int(input("Qual a posição da carta que gostaria de mover?(1-4) "))

if lista_movimentos_possiveis(mao, origem):
    for carta in lista_movimentos_possiveis(mao, origem):
        printa_carta(carta)
