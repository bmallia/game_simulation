from source.property import Board, Property, StatusProperty
from source.player import Player, Behavior
from source.dice import Dice

class Match:
    
    def __init__(self):
        self.round = 0
        p1 = Property(1, StatusProperty.AVAILABLE ,5000.0, 50)
        p2 = Property(2, StatusProperty.AVAILABLE ,7000.0, 70)
        p3 = Property(3, StatusProperty.AVAILABLE ,10000.0, 80)
        p4 = Property(4, StatusProperty.AVAILABLE ,12000.0, 30)
        p5 = Property(5, StatusProperty.AVAILABLE ,5500.0, 50)
        p6 = Property(6, StatusProperty.AVAILABLE ,12000.0, 70)
        p7 = Property(7, StatusProperty.AVAILABLE ,15000.0, 50)
        p8 = Property(8, StatusProperty.AVAILABLE ,16000.0, 70)
        p9 = Property(9, StatusProperty.AVAILABLE ,3500.0, 63)
        p10 = Property(10, StatusProperty.AVAILABLE ,12300.0, 77)
        p11 = Property(11, StatusProperty.AVAILABLE ,10500.0, 100)
        p12 = Property(12, StatusProperty.AVAILABLE ,8200.0, 80)
        p13 = Property(13, StatusProperty.AVAILABLE ,7500.0, 80)
        p14 = Property(14, StatusProperty.AVAILABLE ,3330.0, 40)
        p15 = Property(15, StatusProperty.AVAILABLE ,7200.0, 70)
        p16 = Property(16, StatusProperty.AVAILABLE ,11000.0, 95)
        p17 = Property(17, StatusProperty.AVAILABLE ,8000.0, 25)
        p18 = Property(18, StatusProperty.AVAILABLE ,11200.0, 110)
        p19 = Property(19, StatusProperty.AVAILABLE ,13200.0, 150)
        p20 = Property(20, StatusProperty.AVAILABLE ,12200.0, 120)

        self.board = Board([p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14,p15,p16,p17,p18,p19,p20])
        ##carrega os jogadores
        player1 = Player(Behavior.IMPULSIVE,1)
        player2 = Player(Behavior.DEMANDING,2)
        player3 = Player(Behavior.CAUTIONS,3)
        player4 = Player(Behavior.RANDOM,4)
        
        self.players = [player1, player2, player3, player4]
        self.winner = None
    
    def __is_game_finished__(self):
        return len(self.players) == 1

    def play(self):
        
        while not self.__is_game_finished__() and self.round < 1000:
            
            for index, player in enumerate(self.players):
                dice_number = Dice.play()
                player.position += dice_number
                print(f"O jogador {str(player)} está na posição  {player.position} no tabuleiro")
                
                ##quando o jogador completa a volta no tabuleiro
                if player.position >= self.board.threshold:
                    player.position -= self.board.threshold
                    ##print(f"deu a volta no tabuleiro, a nova posição do player é: {player.position}") 
                    player.balance += 100

                property = self.board.path[player.position]
                ##paga o aluguel se não for o dono e existir um dono  
                rent_paid = player.pay_rent(property)
                
                ##encontra o owner para pagar ele
                if rent_paid:
                    self.update_balance_owner(property)

                purchased_property = player.buy(property)
                if purchased_property is not None:
                    ##se a venda realmente ocorreu atualiza o tabuleiro para que a propriedade 
                    ##esteja disponível novamente
                    print(f"O player {str(player)} comprou a propriedade {str(property)}")
                    self.board.path[player.position] = purchased_property

                    
                
                if player.balance <= 0:                    
                    ##remove o jogador da lista de player e atualiza o status das propriedades removidas do player
                    self.remove_player(player, index)
   
            self.round += 1
            #print(f"Atualizando a rodada para {self.round}")

        self.get_winner()
        ##print(f"O jogo acabou! e o vencedor é: {str(self.winner)}")

    
    def remove_player(self, player, index):
        """
            Removendo usuário e deixando as suas propriedades disponíveis no tabuleiro
        Args:
            player ([Player]): [player que será removido]
            index ([int]): [indice da lista de player]
        """
        for b in range(len(self.board.path)):
            for p in range(len(player.properties)):
                if self.board.path[b].id ==  player.properties[p].id:
                    self.board.path[b].status = StatusProperty.AVAILABLE
                                  
        ##quando eu removo o player preciso vender as propriedades
        player_removed = self.players.pop(index)
        ##print(f"Player {str(player_removed)} removido do jogo")

    def get_winner(self):
        ##preciso decobrir o player com o maior saldo, e se der empate será na ordem
        ##do turno
        pmax: Player = Player(Behavior.RANDOM, 0)
        pmax.balance = 0
        for p in self.players:
            if p.balance > pmax.balance:
                pmax = p
        
        self.winner = pmax


    def update_balance_owner(self, prop):
        player = next((x for x in self.players if x.id == prop.owner), None)
        if player:
            player.balance += prop.rent_value        
            return True
        return False
        
