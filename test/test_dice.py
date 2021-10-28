from source.dice import Dice

def test_dice_value_between_1_6_ok():
    list_dice = [value for value in range(1,6)]
    
    assert Dice.play() in list_dice
    assert Dice.play() in list_dice
    assert Dice.play() in list_dice
    assert Dice.play() in list_dice