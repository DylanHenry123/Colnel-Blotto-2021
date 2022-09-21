# This is a current model that works on probability of a result being the best. But the results are not adaptive.
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
    strategy_scores = {"[3, 3, 0]": 0, "[3, 0, 3]": 0, "[0, 3, 3]": 0, "[4, 1, 1]": 0, "[1, 4, 1]": 0,
                       "[1, 1, 4]": 0, "[2, 2, 2]": 0, "[3, 2, 1]": 0, "[3, 1, 2]": 0, "[2, 3, 1]": 0,
                       "[2, 1, 3]": 0, "[1, 3, 2]": 0, "[1, 2, 3]": 0, "[4, 2, 0]": 0, "[4, 0, 2]": 0,
                       "[2, 4, 0]": 0, "[2, 0, 4]": 0, "[0, 2, 4]": 0, "[0, 4, 2]": 0, "[5, 1, 0]": 0,
                       "[5, 0, 1]": 0, "[1, 0, 5]": 0, "[1, 5, 0]": 0, "[0, 5, 1]": 0, "[0, 1, 5]": 0,
                       "[0, 0, 6]": 0, "[0, 6, 0]": 0, "[6, 0, 0]": 0}

    strategies = ["[3, 3, 0]", "[3, 0, 3]", "[0, 3, 3]", "[4, 1, 1]", "[1, 4, 1]", "[1, 1, 4]", "[2, 2, 2]",
                  "[3, 2, 1]", "[3, 1, 2]", "[2, 3, 1]", "[2, 1, 3]", "[1, 3, 2]", "[1, 2, 3]", "[4, 2, 0]",
                  "[4, 0, 2]", "[2, 4, 0]", "[2, 0, 4]", "[0, 2, 4]", "[0, 4, 2]", "[5, 1, 0]", "[5, 0, 1]",
                  "[1, 0, 5]", "[1, 5, 0]", "[0, 5, 1]", "[0, 1, 5]", "[0, 0, 6]", "[0, 6, 0]", "[6, 0, 0]"]

    score = 0
    total_games = 0
    ties = 0
    player1_wins = 0
    player2_wins = 0

    print("\n------------------------------------------------------------------------------------------------------")
    print("\nThe results for all possible games on the computer for a 3 tower 6 soldier game:\n")
    file = open("strategies_two.txt", "r")
    for x in file:
        strat_one, strat_two = x.split("/")

        strat_one = strat_one.split(", ")
        strat_two = strat_two.split(", ")
        for i in range(len(strat_one)):
            strat_one[i] = int(strat_one[i])
            strat_two[i] = int(strat_two[i])

        game = Game(strat_one, strat_two)
        game.run()

        if game.winner_message == "Player 1 wins":
            strategy_scores[f"{strat_one}"] += 1
            score += 1
            total_games += 1
            player1_wins += 1
        elif game.winner_message == "Tie !        ":
            ties += 1
            total_games += 1
        else:
            total_games += 1
            player2_wins += 1

        print(game)

    print("\n\n")
    for i in range(len(strategy_scores)):
        print(f'Probability of strategy: {strategies[i]}  winning is  {(round(strategy_scores[strategies[i]] / score, 3))*100}% (1dp)')

    print("\n\n")
    for i in range(len(strategy_scores)):
        print(f"{strategies[i]} won {strategy_scores[strategies[i]]} times")

    file.close()

    print(f"""

Total games: {total_games}
Ties: {ties}
Player 1 wins: {player1_wins}
Player 2 wins: {player2_wins}

""")


if __name__ == '__main__':
    train()
