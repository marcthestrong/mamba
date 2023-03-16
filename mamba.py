import pygame
import random
import time

# Define the constants
# Set the window size
WINDOW_SIZE = {
    "x": 1280,
    "y": 720
}

# Set the colors
COLOR = {
    "black": pygame.Color(50, 50, 50),
    "white": pygame.Color(255, 255, 255),
    "red": pygame.Color(255, 0, 0),
    "green": pygame.Color(0, 153, 0),
    "orange": pygame.Color(255, 89, 0),
    "grey": pygame.Color(185, 185, 185)
}



# Set the fonts
FONTS = {
    "score": {
        "name": "times new roman",
        "size": 36
    },
    "game_over": {
        "name": "times new roman",
        "size": 120
    }
}

# Set the starting speed
mamba_speed = 10

def show_score(choice, color, font, size):
    # Make the font object
    score_font = pygame.font.SysFont(FONTS["score"]["name"], FONTS["score"]["size"])

    # Make the display surface object
    score_surface = score_font.render("Score: " + str(score), True, color)

    # Make a rectangular surface object
    score_rect = score_surface.get_rect()

    # Display the text
    window.blit(score_surface, score_rect)

def game_over():
    # Create font object
    my_font = pygame.font.SysFont(FONTS["game_over"]["name"], FONTS["game_over"]["size"])

    # Make text surface object
    game_over_surface = my_font.render("Score : " + str(score), True, COLOR["red"])

    # Make rectangular object for text surface object
    game_over_rect = game_over_surface.get_rect()

    # Setting position of the text
    game_over_rect.midtop = (WINDOW_SIZE["x"] / 2, WINDOW_SIZE["y"] / 3)

    # Draw the text on the screen
    window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()

    # Wait 2 secs to quit the program
    time.sleep(2)

    # Exit the program
    quit()

# Initialize pygame
pygame.init()

# Initialize the window
pygame.display.set_caption("Mamba")
window = pygame.display.set_mode((WINDOW_SIZE["x"], WINDOW_SIZE["y"]))

# Frames per second controller
fps = pygame.time.Clock()

# Set default position
mamba_position = [640, 360]

# Set sqares for the snakes body
mamba_body = [
    [640, 360],
    [620, 360],
    [600, 360],
    [580, 360],
    [560, 360]
]

# Fruit position
fruit_position = [
    random.randrange(1, (WINDOW_SIZE["x"] // 20)) * 20,
    random.randrange(1, (WINDOW_SIZE["y"] // 20)) * 20
]

fruit_spawn = True

# Set default movement direction to the right
direction = "RIGHT"
change_to = direction

score = 0

# Main
while True:

    # Handle key events
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = "UP"
            if event.key == pygame.K_DOWN:
                change_to = "DOWN"
            if event.key == pygame.K_LEFT:
                change_to = "LEFT"
            if event.key == pygame.K_RIGHT:
                change_to = "RIGHT"

    # If two keys pressed simultaneously
    # we don't want snake to move into two directions
    # simultaneously
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    # Moving the snake
    if direction == 'UP':
        mamba_position[1] -= 20
    if direction == 'DOWN':
        mamba_position[1] += 20
    if direction == 'LEFT':
        mamba_position[0] -= 20
    if direction == 'RIGHT':
        mamba_position[0] += 20

    # Snake body growing mechanism
    # if fruits and snakes collide then scores will be
    # incremented by 10
    mamba_body.insert(0, list(mamba_position))
    if mamba_position[0] == fruit_position[0] and mamba_position[1] == fruit_position[1]:
        score += 15
        mamba_speed += 1
        fruit_spawn = False
    else:
        mamba_body.pop()

    if not fruit_spawn:
        fruit_position = [
            random.randrange(1, (WINDOW_SIZE["x"] // 20)) * 20,
            random.randrange(1, (WINDOW_SIZE["y"] // 20)) * 20
        ]

    fruit_spawn = True
    window.fill(COLOR["grey"])

    for position in mamba_body:
        pygame.draw.rect(window, COLOR["black"], pygame.Rect(position[0], position[1], 20, 20))

    fruit_border = pygame.Rect(fruit_position[0], fruit_position[1], 20, 20)
    pygame.draw.circle(window, COLOR["orange"], fruit_border.center, 10)

    # Game Over conditions
    if mamba_position[0] < 0 or mamba_position[0] > WINDOW_SIZE["x"] - 20:
        game_over()
    if mamba_position[1] < 0 or mamba_position[1] > WINDOW_SIZE["y"] - 20:
        game_over()

    # Touching the snake body
    for block in mamba_body[1:]:
        if mamba_position[0] == block[0] and mamba_position[1] == block[1]:
            game_over()

    # Show the Score
    show_score(1, COLOR["white"], FONTS["score"]["name"], FONTS["score"]["size"])

    pygame.display.update()

    fps.tick(mamba_speed)
