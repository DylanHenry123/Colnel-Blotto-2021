# This models
import random


class Game:
    def __init__(self, strategy_one, strategy_two):
        self.num_towers = 3
        self.num_soldiers = 6
        self.choices_one = strategy_one
        self.choices_two = strategy_two
        self.winner_message = ""

    def run(self):
        self.winner_message = self.find_winner()

    def find_winner(self):
        player_one_score = 0
        player_two_score = 0
        message = ""

        for i in range(self.num_towers):
            if self.choices_one[i] > self.choices_two[i]:
                player_one_score += 1
            elif self.choices_one[i] == self.choices_two[i]:
                player_one_score += 1
                player_two_score += 1
            elif self.choices_one[i] < self.choices_two[i]:
                player_two_score += 1
            else:
                print("Unknown error has occurred")

        if player_one_score > player_two_score:
            message = "Player 1 wins"

        elif player_one_score == player_two_score:
            message = "Tie !        "

        elif player_one_score < player_two_score:
            message = "Player 2 wins"

        return message

    def __str__(self):
        return f"{self.winner_message}    Player 1: {self.choices_one}    Player 2: {self.choices_two}"

    def __repr__(self):
        return self.__str__()


def train():
    strategy_scores = {}

    strategies = ["3, 3, 0", "3, 0, 3", "0, 3, 3", "4, 1, 1", "1, 4, 1", "1, 1, 4", "2, 2, 2",
                  "3, 2, 1", "3, 1, 2", "2, 3, 1", "2, 1, 3", "1, 3, 2", "1, 2, 3", "4, 2, 0",
                  "4, 0, 2", "2, 4, 0", "2, 0, 4", "0, 2, 4", "0, 4, 2", "5, 1, 0", "5, 0, 1",
                  "1, 0, 5", "1, 5, 0", "0, 5, 1", "0, 1, 5", "0, 0, 6", "0, 6, 0", "6, 0, 0"]

    file = open("strategies.txt", "r")
    for i in range(len(strategies)):
        information = file.readline()
        strat, value = information.split(" = ")
        value = int(value)

        strategy_scores[strategies[i]] = value

    count = 0

    for i in range(1000000):

        item_one = random.choices([k for k in strategy_scores], [strategy_scores[j] for j in strategy_scores])
        item_two = random.choices([k for k in strategy_scores], [strategy_scores[j] for j in strategy_scores])

        strat_one = []
        strat_two = []

        item_one, item_two = item_one[0], item_two[0]

        for j in range(len(item_one)):
            if j == 0 or j == 3 or j == 6:
                strat_one.append(int(item_one[j]))
                strat_two.append(int(item_two[j]))

        print(strat_one, strat_two)
        game = Game(strat_one, strat_two)
        game.run()

        count += 1

        print(f" {game.winner_message}  player1 = {strat_one}  player2={strat_two}   count: {count}")

        if game.winner_message == "Player 1 wins":
            strategy_scores[f"{str(strat_one).strip(' []')}"] += 1

        elif game.winner_message == "Player 2 wins":
            strategy_scores[f"{str(strat_two).strip(' []')}"] += 1

    file.close()

    file = open("strategies.txt", "w")

    for i in range(len(strategies)):
        file.write(f"{strategies[i]} = {strategy_scores[f'{strategies[i]}']}\n")

    file.close()




if __name__ == '__main__':
    train()