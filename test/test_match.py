import pytest

from source.match import Match 

def test_run_match():
    match = Match()
    player1 = match.players[0]
    player1.balance = 200000
    player2 = match.players[1]
    player2.balance = 200000
    
    match.play()