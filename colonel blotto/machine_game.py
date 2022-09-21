import pygame
import random

pygame.init()
pygame.font.init()

font = pygame.font.SysFont("Comicsans", 100)


class Game:
    def __init__(self):
        # Setting the attributes for the game
        self.width = 1350
        self.height = 799
        self.num_towers = 3
        self.num_soldiers = 6
        self.window = pygame.display.set_mode((self.width, self.height))
        self.FPS = 500

        # Player one attributes
        self.choices_one = []

        # Player Two choices
        self.choices_two = []

        # Computer probabilities for choices
        self.strategy_scores = {}

        # Loading the images for the game
        self.soldier_img_size_x, self.soldier_img_size_y = (self.width // (2 * self.num_soldiers)), (
                self.width // (2 * self.num_soldiers))
        self.towers_img_size_x, self.towers_img_size_y = (self.width // (2 * self.num_towers)), (
                self.width // (2 * self.num_towers))
        self.player_one_img = pygame.transform.scale(pygame.image.load("bossman.png"),
                                                     (self.soldier_img_size_x, self.soldier_img_size_y))
        self.player_two_img = pygame.transform.scale(pygame.image.load("dylan_boss.png"),
                                                     (self.soldier_img_size_x, self.soldier_img_size_y))
        self.towers_img = pygame.transform.scale(pygame.image.load("towerlong3.png"),
                                                 (self.towers_img_size_x, self.towers_img_size_y))
        self.bg = pygame.transform.scale(pygame.image.load("background.png"), (self.width, self.height))

        # Fonts
        self.scores_fonts = pygame.font.SysFont("Comicsans", 30)

        self.winner_message = ""

    def run(self):
        self.draw_objects()
        self.player_one_choice()
        self.player_two_computer_choice()
        self.winner_message = self.find_winner()

        self.update_file()

        run = True
        clock = pygame.time.Clock()
        while run:
            clock.tick(self.FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            self.draw_objects()

    def draw_objects(self):
        # Puts the background on the screen
        self.window.blit(self.bg, (0, 0))

        # Puts the towers on the screen
        gap_towers = (self.width - (self.num_towers * self.towers_img_size_x)) // (self.num_towers + 1)
        for i in range(1, self.num_towers + 1):
            self.window.blit(self.towers_img, (((gap_towers * i) + (self.towers_img_size_x * (i - 1))), 275))

        # Putting the selected results by both players on the screen
        if len(self.choices_one) > 0:
            for i in range(self.num_towers):
                text_one = self.scores_fonts.render(str(self.choices_one[i]), True, (255, 255, 255))
                text_two = self.scores_fonts.render(str(self.choices_two[i]), True, (255, 255, 255))
                self.window.blit(text_one, (
                    ((gap_towers * (i + 1)) + (self.towers_img_size_x * i)), (280 + self.towers_img_size_y)))
                self.window.blit(text_two, (((gap_towers * (i + 1)) + (self.towers_img_size_x * i)), 260))

        # Puts the soldiers on the screen for both players
        gap_soldiers = (self.width - (self.num_soldiers * self.soldier_img_size_x)) // (self.num_soldiers + 1)
        for i in range(self.num_soldiers + 1):
            self.window.blit(self.player_two_img, (((gap_soldiers * i) + (self.soldier_img_size_x * (i - 1))), 5))
            self.window.blit(self.player_one_img, (((gap_soldiers * i) + (self.soldier_img_size_x * (i - 1))), 680))

        # Puts the winner on the screen
        text = font.render(str(self.winner_message), True, (255, 255, 255))
        self.window.blit(text, (450, 180))

        # Put text boxes on the screen

        # Put a confirm button on the screen

        pygame.display.update()

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
            message = "Tie !"

        elif player_one_score < player_two_score:
            message = "Player 2 wins"

        return message

    def player_two_computer_choice(self):
        strategies = ["3, 3, 0", "3, 0, 3", "0, 3, 3", "4, 1, 1", "1, 4, 1", "1, 1, 4", "2, 2, 2",
                      "3, 2, 1", "3, 1, 2", "2, 3, 1", "2, 1, 3", "1, 3, 2", "1, 2, 3", "4, 2, 0",
                      "4, 0, 2", "2, 4, 0", "2, 0, 4", "0, 2, 4", "0, 4, 2", "5, 1, 0", "5, 0, 1",
                      "1, 0, 5", "1, 5, 0", "0, 5, 1", "0, 1, 5", "0, 0, 6", "0, 6, 0", "6, 0, 0"]

        file = open("strategies.txt", "r")
        for i in range(len(strategies)):
            information = file.readline()
            strat, value = information.split(" = ")
            value = int(value)

            self.strategy_scores[strategies[i]] = value

        item_one = random.choices([k for k in self.strategy_scores], [self.strategy_scores[j] for j in self.strategy_scores])

        item_one = item_one[0]

        for j in range(len(item_one)):
            if j == 0 or j == 3 or j == 6:
                self.choices_two.append(int(item_one[j]))

        file.close()


    def player_one_choice(self):
        soldiers_left = self.num_soldiers

        for i in range(self.num_towers):
            selected_soldiers = int(input(f"Tower {i + 1}: "))

            if selected_soldiers <= soldiers_left:
                self.choices_one.append(selected_soldiers)
                soldiers_left -= selected_soldiers

            else:
                print("Invalid value! Try again")
                self.choices_one = []
                self.player_one_choice()


    def update_file(self):
        strategies = ["3, 3, 0", "3, 0, 3", "0, 3, 3", "4, 1, 1", "1, 4, 1", "1, 1, 4", "2, 2, 2",
                      "3, 2, 1", "3, 1, 2", "2, 3, 1", "2, 1, 3", "1, 3, 2", "1, 2, 3", "4, 2, 0",
                      "4, 0, 2", "2, 4, 0", "2, 0, 4", "0, 2, 4", "0, 4, 2", "5, 1, 0", "5, 0, 1",
                      "1, 0, 5", "1, 5, 0", "0, 5, 1", "0, 1, 5", "0, 0, 6", "0, 6, 0", "6, 0, 0"]

        if game.winner_message == "Player 2 wins":
            self.strategy_scores[f"{str(self.choices_two).strip(' []')}"] += 1


        file = open("strategies.txt", "w")

        for i in range(len(strategies)):
            file.write(f"{strategies[i]} = {self.strategy_scores[f'{strategies[i]}']}\n")

        file.close()


if __name__ == '__main__':
    pygame.init()
    pygame.font.init()

    game = Game()
    game.run()
