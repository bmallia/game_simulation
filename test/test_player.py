import pytest

from source.player import Player, Behavior
from source.property import Property, StatusProperty
from source.errors import IllegalArgumentError

def test_buy_unavailable_property():
    p = Property(1, StatusProperty.PURCHASED, 7000.0, 300.0)
    player1 = Player(Behavior.IMPULSIVE, 1)
    result = player1.buy(p)    
    assert result == None
    
def test_buy_available_property_with_balance():
    p = Property(1, StatusProperty.AVAILABLE, 7000.0, 300.0)
    player1 = Player(Behavior.IMPULSIVE, 1)
    player1.balance = 20000
    result = player1.buy(p)
    assert result == p


def test_buy_rent_demanding_player_error_balance_minor_50():
    p = Property(1, StatusProperty.AVAILABLE, 7000.0, 30)
    player1 = Player(Behavior.DEMANDING, 2)
    player1.balance = 20000
    result = player1.buy(p)
    assert result == None


def test_buy_rent_demanding_player_balance_ok():
    p = Property(1, StatusProperty.AVAILABLE, 7000.0, 70)
    player1 = Player(Behavior.DEMANDING,2)
    player1.balance = 20000
    result = player1.buy(p)
    assert result == p    

def test_buy_countions_player_balance_ok():
    p = Property(1, StatusProperty.AVAILABLE, 7000.0, 70)
    player1 = Player(Behavior.CAUTIONS,3)
    player1.balance = 20000
    result = player1.buy(p)
    assert result == p    

def test_buy_countions_player_balance_error():
    p = Property(1, StatusProperty.AVAILABLE, 10000.0, 70)
    player1 = Player(Behavior.CAUTIONS,3)
    player1.balance = 10070
    result = player1.buy(p)
    assert result == None

def test_rent_player_balance_ok():
    p = Property(1, StatusProperty.AVAILABLE, 10000.0, 70)
    player1 = Player(Behavior.CAUTIONS,3)
    player1.balance = 10070
    result = player1.pay_rent(p)
    assert result == True
   
def test_buy_random_player_balance_ok():
    p1 = Property(1, StatusProperty.AVAILABLE, 10000.0, 70)
    p2 = Property(2, StatusProperty.AVAILABLE, 12000.0, 75)
    p3 = Property(3, StatusProperty.AVAILABLE, 7000.0, 30)
    p4 = Property(3, StatusProperty.AVAILABLE, 5500.0, 25)

    player1 = Player(Behavior.RANDOM,4)
    player1.balance = 1000000
    result1 = player1.buy(p1)
    result2 = player1.buy(p2)
    result3 = player1.buy(p3)
    result4 = player1.buy(p4)

    assert isinstance(result1, Property) or isinstance(result2, Property) or isinstance(result3, Property) or isinstance(result4, Property)
    

def test_not_pay_rent_own_property():
    p = Property(1, StatusProperty.AVAILABLE, 10000.0, 70)
    player = Player(Behavior.IMPULSIVE,1)
    player.balance = 50000.0
    player.buy(p)
    result = player.pay_rent(p)

    assert result == False
    assert player.balance == 40000.0
    assert len(player.properties) == 1
