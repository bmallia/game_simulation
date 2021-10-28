from enum import Enum

from source.errors import IllegalArgumentError

class StatusProperty(Enum):
    AVAILABLE = 0
    PURCHASED = 1

class Property:

    """
        Classe que representa uma propriedade no jogo. Toda propriedade possui um id único, 
        um status (disponível ou comprada, vide class StatusProperty), um valor de compra 
        e um valor de aluguel
    """
    def __init__(self, id, status , purchase_value, rent_value, owner = 0):
        self.id = id 
        self.status = status
        self.purchase_value = purchase_value
        self.rent_value = rent_value
        self.owner = owner

    def __str__(self):
        return f"id :{self.id}, status: {self.status}, valor de compra: {self.purchase_value}, valor de alugue: {self.rent_value}, owner: {self.owner}"

    def __hash__(self):
        return hash((self.id))
    
    def __eq__(self, other):
        return self.id == other.id

class Board:
    """
        Classe que representa o tabuleiro onde recebe no contrutor uma lista de propriedades, a o 
        threshold que é a quantidade máxima de casas nesse tabuleiro
    """
    def __init__(self, list_properties, threshold=20):
        self.threshold = threshold
        self.path = []

        if len(list_properties) != self.threshold:
            raise IllegalArgumentError(f"A quantidade de propriedades no tabuleiro pricesa ser de {self.threshold}")
            
        for prop in list_properties:
            self.path.append(prop)

        

        
