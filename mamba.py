from game import *
from tkinter import *

root = Tk()
x = ((root.winfo_screenwidth() / 2) * 0.50)
y = root.winfo_screenheight() * 0.50

# Initialize pygame
pygame.init()
objGame = Game(x, y)

# Initialize the window
pygame.display.set_caption("Mamba")
window = objGame.window

BASE_PATH = Path(__file__).resolve().parent
sound_chew_path = str(BASE_PATH) + "/sounds/chewing.wav"
bite_sound = pygame.mixer.Sound(sound_chew_path)
sound_smash_path = str(BASE_PATH) + "/sounds/smash.wav"
smash_sound = pygame.mixer.Sound(sound_smash_path)

# FPS (Frames per second controller)
fps = pygame.time.Clock()

change_to = objGame.change_to
direction = objGame.direction

# Main
while True:

    window.fill(objGame.COLOR["grey"])

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
        objGame.mamba_position[1] -= 40
    if direction == 'DOWN':
        objGame.mamba_position[1] += 40
    if direction == 'LEFT':
        objGame.mamba_position[0] -= 40
    if direction == 'RIGHT':
        objGame.mamba_position[0] += 40

    objGame.mamba_body.insert(0, list(objGame.mamba_position))
    if objGame.mamba_position[0] == objGame.food_position[0] and objGame.mamba_position[1] == objGame.food_position[1]:

        # Play chewing sound
        objGame.SOUND_CHEW.play()

        # Add points to the score
        objGame.set_score(15)

        # Increase the speed of the snake
        objGame.set_speed(1)

        objGame.food_spawn = False
    else:
        objGame.mamba_body.pop()

    if not objGame.food_spawn:
        objGame.food_position = [
            random.randrange(1, (objGame.WINDOW_SIZE["x"] // 40)) * 40,
            random.randrange(1, (objGame.WINDOW_SIZE["y"] // 40)) * 40
        ]

    for segment in objGame.mamba_body:
        pygame.draw.rect(window, objGame.COLOR["black"], pygame.Rect(segment[0], segment[1], 40, 40))

    food_border = pygame.Rect(objGame.food_position[0], objGame.food_position[1], 40, 40)
    pygame.draw.circle(window, objGame.COLOR["green"], food_border.center, 20)

    # Game Over conditions
    if objGame.mamba_position[0] < 0 or objGame.mamba_position[0] > objGame.WINDOW_SIZE["x"] - 40:
        objGame.SOUND_SMASH.play()
        objGame.game_over()
    if objGame.mamba_position[1] < 0 or objGame.mamba_position[1] > objGame.WINDOW_SIZE["y"] - 40:
        objGame.SOUND_SMASH.play()
        objGame.game_over()

    # Touching the snake body
    for segment in objGame.mamba_body[1:]:
        if objGame.mamba_position[0] == segment[0] and objGame.mamba_position[1] == segment[1]:
            objGame.SOUND_SMASH.play()
            objGame.game_over()

    # Show the Score
    objGame.score(1, objGame.COLOR["white"], objGame.FONTS["score"]["name"], objGame.FONTS["score"]["size"])

    pygame.display.update()

    fps.tick(objGame.get_speed())
