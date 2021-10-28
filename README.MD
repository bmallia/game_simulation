
Simulação do jogo de tabuleiro muito semelhante ao Banco Imobiliário

- jogadores se alternam e rodadas, numa ordem definida aleatoriamente no começo da partida
- tabuleiro tem 20 propriedades em sequência, Cada propriedade tem um custo da venda, um valor de aluguel caso a propriedade já esteja comprada
- seguem uma determinada ordem do tabuleiro (essa ordem é aleatória também?)

- No começo o jogador de 6 faces que determina quantos espaços no tabuleiro o jogador 
vai andar

Desejamos rodar uma simulação para decidir qual a melhor estratégia. Para isso, idealizamos uma partida com 4 diferentes tipos de possíveis jogadores. Os comportamentos definidos são:
O jogador um é impulsivo;
O jogador dois é exigente;
O jogador três é cauteloso;
O jogador quatro é aleatório;O jogador impulsivo compra qualquer propriedade sobre a qual ele parar.
O jogador exigente compra qualquer propriedade, desde que o valor do aluguel dela seja maior do que 50.
O jogador cauteloso compra qualquer propriedade desde que ele tenha uma reserva de 80 saldo sobrando
depois de realizada a compra.
O jogador aleatório compra a propriedade que ele parar em cima com probabilidade de 50%.
Caso o jogo demore muito, como é de costume em jogos dessa natureza, o jogo termina na milésima rodada
com a vitória do jogador com mais saldo. O critério de desempate é a ordem de turno dos jogadores nesta
partida.
Saída
Uma execução do programa proposto deve rodar 300 simulações, imprimindo no console os dados referentes
às execuções. Esperamos encontrar nos dados as seguintes informações:
Quantas partidas terminam por time out (1000 rodadas);
Quantos turnos em média demora uma partida;
Qual a porcentagem de vitórias por comportamento dos jogadores;
Qual o comportamento que mais vence.


o que é uma simulação: é o jogo terminar com algum vencedor ou ter 1000 rodadas

turno: depois que todos os jogadores jogam acaba o turno e o primeiro jogador joga novamente
Jogador (id, saldo, propriedades, comportamento, resultado: vencedor ou perdedor)
tem diferença entre rodadas e turno?
Match (turno: inteiro, lista de jogadores, verifica se a partida acaba ou se chega a 1000 rodadas)


GameSimulation (300 simulações)

- Quantas partidas terminam por timeout (1000 rodadas)



