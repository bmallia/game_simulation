import pytest
from source.property import Board
from source.property import Property, StatusProperty
from source.errors import IllegalArgumentError
from source.player import Player

@pytest.fixture
def property_list():
    property_list = set()
    p1 = Property(1, StatusProperty.AVAILABLE ,5000.0, 200.0)
    p2 = Property(2, StatusProperty.PURCHASED, 7000.0, 300.0)
    p3 = Property(3, StatusProperty.AVAILABLE, 8000.0, 500.0)
    property_list.add(p1)
    property_list.add(p2)
    property_list.add(p3)
    return property_list


def test_board_with_less_required_property(property_list):
    with pytest.raises(IllegalArgumentError):
        board = Board(property_list, 5)

def test_board_with_greater_required_property(property_list):
    with pytest.raises(IllegalArgumentError):
        p1 = Property(4, StatusProperty.AVAILABLE, 17000,350.0)
        property_list.add(p1)
        board = Board(property_list, 3)


def test_board_with_repeted_properties(property_list):
    p1 = Property(1, StatusProperty.AVAILABLE, 12000, 700.0)
    property_list.add(p1)

    assert len(property_list) == 3