# Author: Marcus Armstrong
# Based on code from: https://www.geeksforgeeks.org/snake-game-in-python-using-pygame-module/

import pygame
import sys
from pathlib import Path
import random
import time
import pygame.gfxdraw


class Game:
    def __init__(self, x, y):

        # Set the instance variables
        self.last_time = time.time()
        self.x = x
        self.y = y
        self._speed = 10
        self._score = 0
        self._food_spawn = True
        self._food_color = "green"
        self.direction = "RIGHT"
        self.change_to = self.direction

        # Set the file paths
        self.BASE_PATH = Path(__file__).resolve().parent
        self.SOUNDS_PATH = str(self.BASE_PATH) + "/assets/sounds/"
        self.GFX_PATH = str(self.BASE_PATH) + "/assets/graphics/"

        # Load the sound fx
        self.SOUND_CHEW = pygame.mixer.Sound(self.SOUNDS_PATH + "chewing.wav")
        self.SOUND_SMASH = pygame.mixer.Sound(self.SOUNDS_PATH + "smash.wav")
        self.BACKGROUND_IMG = pygame.image.load(str(self.GFX_PATH) + "background.png")

        # Store the window size
        self.WINDOW_SIZE = {
            "x": x,
            "y": y
        }

        # Set  position
        self.food_position = [
            random.randrange(1, (self.WINDOW_SIZE["x"] // 40)) * 40,
            random.randrange(1, (self.WINDOW_SIZE["y"] // 40)) * 40
        ]

        # Store the colors used in the game
        self.COLOR = {
            "black": pygame.Color(28, 28, 28),
            "white": pygame.Color(255, 255, 255),
            "grey": pygame.Color(150, 150, 150),
            "red": pygame.Color(255, 0, 0),
            "green": pygame.Color(0, 153, 0),
            "blue": pygame.Color(17, 0, 255),
            "purple": pygame.Color(150, 0, 255),
            "orange": pygame.Color(255, 128, 0),
            "yellow": pygame.Color(255, 255, 0)
        }

        # Store the font and the font size
        self.FONTS = {
            "score": {
                "name": "Roboto",
                "size": 36
            },
            "game_over": {
                "name": "Roboto",
                "size": 120
            }
        }

        # Initialize the pygame window
        self.window = pygame.display.set_mode((self.WINDOW_SIZE["x"], self.WINDOW_SIZE["y"]))

        # Set starting position
        self.mamba_position = [self.x / 2, self.y / 2]

        # Set squares for the snake's body
        self.mamba_body = [
            [self.x / 2, self.y / 2],
            [(self.x / 2) - 40, self.y / 2]
        ]

    def set_food_position(self):
        self.food_position = [
            random.randrange(1, (self.WINDOW_SIZE["x"] // 40)) * 40,
            random.randrange(1, (self.WINDOW_SIZE["y"] // 40)) * 40
        ]
        # Set the boolean true
        self.set_food_spawn(True)

    def get_food_position(self):
        # Set the food at a random X-Y coordinates
        return self.food_position

    # Get the current score
    def get_score(self):
        return self._score

    # Get the current speed
    def get_speed(self):
        return self._speed

    # Get the boolean
    def get_food_spawn(self):
        return self._food_spawn

    # Set the score
    def set_score(self):
        if self.get_food_color() == "red":
            self._score += 10
        elif self.get_food_color() == "blue":
            self._score += 15
        elif self.get_food_color() == "purple":
            self._score += 20
        elif self.get_food_color() == "orange":
            self._score += 25
        elif self.get_food_color() == "yellow":
            self._score += 35
        else:
            self._score += 5

    # Increment the speed by 1
    def set_speed(self):
        self._speed += 0.5

    # Set the boolean
    def set_food_spawn(self, food_spawn):
        self._food_spawn = food_spawn

    # set the food color
    def set_food_color(self):
        food_colors = list(self.COLOR.keys())
        random_index = random.randint(3, len(food_colors) - 1)
        self._food_color = f"{food_colors[random_index]}"

    # Get the food color
    def get_food_color(self):
        return self._food_color

    # Show the score

    def show_score(self, color):
        # Make the font object
        score_font = pygame.font.SysFont(self.FONTS["score"]["name"], self.FONTS["score"]["size"], bold=True)

        # Make the display surface object
        score_surface = score_font.render(" Score : " + str(self.get_score()), True, color)

        # Make a rectangular surface object
        score_rect = score_surface.get_rect()

        # Display the text
        self.window.blit(score_surface, score_rect)

    def game_over(self):
        # Create font object
        game_over_font = pygame.font.SysFont(self.FONTS["game_over"]["name"], self.FONTS["game_over"]["size"], bold=True)

        # Make text surface object
        game_over_surface = game_over_font.render("Score : " + str(self.get_score()), True, self.COLOR["red"])

        # Make rectangular object for text surface object
        game_over_rect = game_over_surface.get_rect()

        # Setting position of the text
        game_over_rect.midtop = (self.WINDOW_SIZE["x"] / 2, self.WINDOW_SIZE["y"] / 3)

        # Draw the text on the screen
        self.window.blit(game_over_surface, game_over_rect)
        pygame.display.flip()

        # Wait 2 secs to quit the program
        time.sleep(2)

        # Exit the program
        pygame.quit()
        sys.exit()

    @staticmethod
    def draw_rounded_line(surface, color, start_pos, end_pos, width):
        pygame.draw.line(surface, color, start_pos, end_pos, width)
        pygame.gfxdraw.aacircle(surface, int(start_pos[0]), int(start_pos[1]), int(width // 2), color)
        pygame.gfxdraw.filled_circle(surface, int(start_pos[0]), int(start_pos[1]), int(width // 2), color)
        pygame.gfxdraw.aacircle(surface, int(end_pos[0]), int(end_pos[1]), int(width // 2), color)
        pygame.gfxdraw.filled_circle(surface, int(end_pos[0]), int(end_pos[1]), int(width // 2), color)