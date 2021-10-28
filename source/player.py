from enum import Enum
from random import randint

from source.property import Property, StatusProperty
from source.errors import IllegalArgumentError

class Behavior(Enum):
    """
        Mapeia os tipos de comportamento dos Players
        podendo ser IMPULSIVO, EXIGENTE, CAUTELOSO e ALEATÓRIO
    Args:
        Enum ([type]): [o tipo de comportamento]
    """
    ##impulsivo
    IMPULSIVE = 1
    ##exigente
    DEMANDING = 2
    ##cauteloso
    CAUTIONS = 3
    ##ALEATÓRIO
    RANDOM = 4
    

class Player:

    def __init__(self, behavior: Behavior, id: int):
        self.id = id
        self.balance = 300
        self.behavior = behavior
        self.properties = []
        self.position = 0

    def buy(self, property: Property):
        """
            Funcao para comprar uma propriedade, é levado em consideração
            o comportamento do jogador se será realizado ou não a compora
        Args:
            property (Property): [description]


        Returns:
            [type]: [Retorna a propriedade comprada se ela foi realizada com sucesso ou None]
        """
        if property.status == StatusProperty.PURCHASED:
            return None

        if not self.__has_balance__(property.purchase_value):
            return None
            

        if self.behavior == Behavior.IMPULSIVE:
            self.balance -= property.purchase_value
            property.status = StatusProperty.PURCHASED
            self.properties.append(property)
            return property
        
        if self.behavior == Behavior.DEMANDING:
            if property.rent_value > 50:
                self.balance -= property.purchase_value
                property.status = StatusProperty.PURCHASED
                self.properties.append(property)
                return property
            
            return None

        if self.behavior == Behavior.CAUTIONS:
            new_balance = self.balance - property.purchase_value
            if  new_balance > 80:
                self.balance = new_balance
                property.status = StatusProperty.PURCHASED
                self.properties.append(property)
                return property
            
            return None

        if self.behavior == Behavior.RANDOM:
            ##calcular probabilidade de 50%
            rvalue = randint(0,1)
            if bool(rvalue):
                self.balance - property.purchase_value
                property.status = StatusProperty.PURCHASED
                self.properties.append(property)
                return property
            return None

    def pay_rent(self, property):
        """
            Função que paga o aluguel de uma propriedade
        Args:
            property ([type]): [a propriedade]

        Returns:
            [type]: [True se o aluguel foi pago e False senão foi pago]
        """
        if self.__has_balance__(property.rent_value):
            ##não pago aluguel se a propriedade for minha
            if not self.__is_own_property__(property):
                self.balance -= property.rent_value
                return True
        
        return False

    def __has_balance__(self, money):
        return self.balance >= money and self.balance > 0

    def __is_own_property__(self, property):
        return property in self.properties

    def __str__(self):
        return f"Objeto Player: id: {self.id} saldo: {self.balance}, comportamento: {self.behavior}, posição no tabuleiro: {self.position}"

