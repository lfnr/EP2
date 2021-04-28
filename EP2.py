import random

class Carta:
    #Cria uma lista de Naipes e Valores
    listaNaipes = ["♠", "♥", "♦", "♣"]
    listaValores = ["Ás", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    def __init__(self, naipe, valor):
        #Inicializa os atributos que descrevem uma carta
        self.naipe = naipe
        self.valor = valor
    def __str__ (self):
        return (self.listaValores[self.valor]) + ' ' + (self.listaNaipes[self.naipe]) 
