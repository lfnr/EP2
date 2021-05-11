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

def jogo():
    deck = cria_baralho()
    random.shuffle(deck)
    mao = deck[0:4]

    while teste_mao(mao) == False:
        deck = cria_baralho()
        random.shuffle(deck)
        mao = deck[0:4]
    
    
    print("Estado atual da mesa")
    print("====================")
    for carta in mao:
        printa_carta(carta)

    print("====================")

    origem = int(input("Qual a posição da carta que gostaria de mover?(1-4) "))

    while origem not in range(1, 5):
        print("Tente outro número")
        origem = int(input("Qual a posição da carta que gostaria de mover?(1-4) "))

    if lista_movimentos_possiveis(mao, origem) == []:
        print("Tente outro número")
        int(input("Qual a posição da carta que gostaria de mover?(1-4) "))

    i = 3
    while len(mao) >1 and teste_mao(mao):

        if lista_movimentos_possiveis(mao, origem):
            print("Cartas possíveis:")
            for carta in lista_movimentos_possiveis(mao, origem):
                printa_carta(carta)

        destino = int(input(("Sobre qual carta você gostaria de empilhar?(Utilize as posicões de 1-{}) ").format(i+1)))

        mao = empilha(mao, origem, destino)

        print("Estado atual da mesa")
        print("====================")

        for carta in mao:
            printa_carta(carta)

        print("====================")

        if not teste_mao(mao) and len(mao) > 1:
            print("Jogo acabou")
            b = input("Você gostaria de jogar novamente? ")
            if b == "sim":
                jogo()
            break

        origem = int(input(("Qual a posição da carta que gostaria de mover?(1-{}) ").format(i)))
        i = i-1

    if len(mao) == 1:
        print("Você venceu!")
        a = input("Você gostaria de jogar novamente? ")
        if a == "sim":
            jogo()


resp = input("Você gostaria de começar um jogo? ")

if resp == "sim":
    jogo()

