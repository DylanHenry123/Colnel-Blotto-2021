import pygame
import math

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

        # Loading the images for the game
        self.soldier_img_size_x, self.soldier_img_size_y = (self.width // (2*self.num_soldiers)), (self.width // (2*self.num_soldiers))
        self.towers_img_size_x, self.towers_img_size_y = (self.width // (2*self.num_towers)), (self.width // (2*self.num_towers))
        self.player_one_img = pygame.transform.scale(pygame.image.load("bossman.png"), (self.soldier_img_size_x, self.soldier_img_size_y))
        self.player_two_img = pygame.transform.scale(pygame.image.load("dylan_boss.png"), (self.soldier_img_size_x, self.soldier_img_size_y))
        self.towers_img = pygame.transform.scale(pygame.image.load("towerlong3.png"), (self.towers_img_size_x, self.towers_img_size_y))
        self.bg = pygame.transform.scale(pygame.image.load("background.png"), (self.width, self.height))

        # Fonts
        self.scores_fonts = pygame.font.SysFont("Comicsans", 30)

        self.winner_message = ""

    def run(self):
        self.draw_objects()
        self.player_one_choice()
        self.player_two_computer_choice()
        self.winner_message = self.find_winner()

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
        gap_towers = (self.width - (self.num_towers * self.towers_img_size_x)) // (self.num_towers+1)
        for i in range(1, self.num_towers+1):
            self.window.blit(self.towers_img, (((gap_towers * i) + (self.towers_img_size_x * (i - 1))), 275))

        # Putting the selected results by both players on the screen
        if len(self.choices_one) > 0:
            for i in range(self.num_towers):
                text_one = self.scores_fonts.render(str(self.choices_one[i]), True, (255, 255, 255))
                text_two = self.scores_fonts.render(str(self.choices_two[i]), True, (255, 255, 255))
                self.window.blit(text_one, (((gap_towers * (i + 1)) + (self.towers_img_size_x * i)), (280 + self.towers_img_size_y)))
                self.window.blit(text_two, (((gap_towers * (i + 1)) + (self.towers_img_size_x * i)), 260))

        # Puts the soldiers on the screen for both players
        gap_soldiers = (self.width - (self.num_soldiers * self.soldier_img_size_x)) // (self.num_soldiers+1)
        for i in range(self.num_soldiers+1):
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
        soldiers_left = self.num_soldiers
        towers_left = self.num_towers
        indexes_left = [i for i in range(len(self.choices_one))]
        indexes_of_choices_one = [i for i in range(len(self.choices_one))]
        sort = sorted(self.choices_one)
        new_choices = []

        if self.num_towers % 2 != 0:
            for i in range(math.ceil(self.num_towers/2)):
                if self.choices_one.index(sort[i]) in indexes_of_choices_one:
                    new_choices.append((sort[i] + 1, self.choices_one.index(sort[i])))
                    soldiers_left -= (sort[i] + 1)
                    towers_left -= 1
                    indexes_left.remove(self.choices_one.index(sort[i]))
                    indexes_of_choices_one.remove(self.choices_one.index(sort[i]))
                else:
                    new_choices.append((sort[i] + 1, indexes_of_choices_one[0]))
                    soldiers_left -= (sort[i] + 1)
                    towers_left -= 1
                    indexes_left.remove(indexes_of_choices_one[0])
                    indexes_of_choices_one.remove(indexes_of_choices_one[0])

        else:
            for i in range(math.ceil(self.num_towers/2) + 1):
                if self.choices_one.index(sort[i]) in indexes_of_choices_one:
                    new_choices.append((sort[i] + 1, self.choices_one.index(sort[i])))
                    soldiers_left -= (sort[i] + 1)
                    towers_left -= 1
                    indexes_left.remove(self.choices_one.index(sort[i]))
                    indexes_of_choices_one.remove(self.choices_one.index(sort[i]))
                else:
                    new_choices.append((sort[i] + 1, indexes_of_choices_one[0]))
                    soldiers_left -= (sort[i] + 1)
                    towers_left -= 1
                    indexes_left.remove(indexes_of_choices_one[0])
                    indexes_of_choices_one.remove(indexes_of_choices_one[0])

        new_choices.append((soldiers_left, indexes_left[0]))
        towers_left -= 1
        indexes_left.remove(indexes_left[0])

        if towers_left > 0:
            for i in range(towers_left):
                new_choices.append((0, indexes_left[0]))
                indexes_left.remove(indexes_left[0])

        for i in range(self.num_towers):
            for j in range(len(new_choices)):
                if new_choices[j][1] == i:
                    self.choices_two.append(new_choices[j][0])

    def player_one_choice(self):
        soldiers_left = self.num_soldiers

        for i in range(self.num_towers):
            selected_soldiers = int(input(f"Tower {i+1}: "))

            if selected_soldiers <= soldiers_left:
                self.choices_one.append(selected_soldiers)
                soldiers_left -= selected_soldiers

            else:
                print("Invalid value! Try again")
                self.choices_one = []
                self.player_one_choice()


if __name__ == '__main__':
    pygame.init()
    pygame.font.init()

    game = Game()
    game.run()