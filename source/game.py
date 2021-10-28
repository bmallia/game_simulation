from source.match import Match
from source.player import Behavior

class Simulation:
    """
        Classe que representa a simulacao do jogo
    """
    def __init__(self, number_simulation):
        self.number_simulation = number_simulation
        self.matches = []
    
    def start(self):
        print(f"Começando simulação: quantidade de simulações {self.number_simulation}")

        for i in range(self.number_simulation):
            match = Match()
            match.play()
            self.matches.append(match)
        
        total_matches = self.count_timeout_matches()
        print(f"{total_matches} partidas terminaram por time out")
        total_shift = self.calculate_shift()
        print(f"A média de turnos é {total_shift}")
        perc_impulsive, perc_demanding, perc_cautions, perc_random =  self.calculate_percentage_victory()
        print(f"{perc_impulsive}% dos vencedores são impulsivos")
        print(f"{perc_demanding}% dos vencedores são exigentes")
        print(f"{perc_cautions}% dos vencedores são cuidadosos")
        print(f"{perc_random}% dos vencedores são aleatórios")

    def count_timeout_matches(self):
        total = 0
        [total := total + 1 for m in self.matches if m.round == 1000]
        return total
    
    def calculate_shift(self):
        total_shift = 0
        [total_shift := total_shift + (m.round * len(m.players)) for m in self.matches]
        return round(total_shift / len(self.matches))

    
    def calculate_percentage_victory(self):
        
        total_winners = len([m.winner for m in self.matches])
        impulsive_players = len([m.winner for m in self.matches if m.winner.behavior == Behavior.IMPULSIVE])
        demanding_players = len([m.winner for m in self.matches if m.winner.behavior == Behavior.DEMANDING])
        cautions_players = len([m.winner for m in self.matches if m.winner.behavior == Behavior.CAUTIONS])
        random_players = len([m.winner for m in self.matches if m.winner.behavior == Behavior.RANDOM])

        perc_impulsive = (100 * impulsive_players) / total_winners
        perc_demanding = (100 * demanding_players) / total_winners
        perc_cautions = (100 * cautions_players) / total_winners
        perc_random = (100 * random_players) / total_winners

        return perc_impulsive, perc_demanding , perc_cautions , perc_random
        
        