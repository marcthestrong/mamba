from tkinter import *
import pygame
from pygame.locals import *
import sys
from pathlib import Path
import random
import time


class Game:
    def __init__(self, x, y):
        self.x = x
        self.x = y
        self._speed = 10
        self._score = 0
        self.food_spawn = True
        self.direction = "RIGHT"
        self.change_to = self.direction
        self.BASE_PATH = Path(__file__).resolve().parent
        self.SOUND_CHEW_PATH = str(self.BASE_PATH) + "/sounds/chewing.wav"
        self.SOUND_CHEW = pygame.mixer.Sound(self.SOUND_CHEW_PATH)
        self.SOUND_SMASH_PATH = str(self.BASE_PATH) + "/sounds/smash.wav"
        self.SOUND_SMASH = pygame.mixer.Sound(self.SOUND_SMASH_PATH)

        self.WINDOW_SIZE = {
            "x": x,
            "y": y
        }

        self.COLOR = {
            "black": pygame.Color(50, 50, 50),
            "white": pygame.Color(255, 255, 255),
            "red": pygame.Color(255, 0, 0),
            "green": pygame.Color(0, 153, 0),
            "purple": pygame.Color(150, 0, 255),
            "orange": pygame.Color(255, 89, 0),
            "grey": pygame.Color(185, 185, 185)
        }

        self.FONTS = {
            "score": {
                "name": "times new roman",
                "size": 36
            },
            "game_over": {
                "name": "times new roman",
                "size": 120
            }
        }

        self.window = pygame.display.set_mode((self.WINDOW_SIZE["x"], self.WINDOW_SIZE["y"]))

        # Set starting position
        self.mamba_position = [640, 360]

        # Set squares for the snakes body
        self.mamba_body = [
            [640, 360],
            [600, 360],
            [540, 360],
            [500, 360],
            [460, 360]
        ]

        # Fruit position
        self.food_position = [
            random.randrange(1, (self.WINDOW_SIZE["x"] // 40)) * 40,
            random.randrange(1, (self.WINDOW_SIZE["y"] // 40)) * 40
        ]

    def score(self, choice, color, font, size):
        # Make the font object
        score_font = pygame.font.SysFont(self.FONTS["score"]["name"], self.FONTS["score"]["size"])

        # Make the display surface object
        score_surface = score_font.render("Score : " + str(self.score), True, color)

        # Make a rectangular surface object
        score_rect = score_surface.get_rect()

        # Display the text
        self.window.blit(score_surface, score_rect)

    def set_score(self, score_increment):
        self._score += score_increment

    def get_score(self):
        return self._score

    def set_speed(self, speed_increment):
        self._speed += speed_increment

    def get_speed(self):
        return self._speed

    def game_over(self):
        # Create font object
        game_over_font = pygame.font.SysFont(self.FONTS["game_over"]["name"], self.FONTS["game_over"]["size"])

        # Make text surface object
        game_over_surface = game_over_font.render("Score : " + str(self.score), True, self.COLOR["red"])

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
