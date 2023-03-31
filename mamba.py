# Author: Marcus Armstrong
# Based on code from: https://www.geeksforgeeks.org/snake-game-in-python-using-pygame-module/
# Assisted with OpenAI
# Driver file

from game import *

# Set the resolution to 1280x720 pixels
x = 1280
y = 720

# Initialize the game
pygame.init()
objGame = Game(x, y)

# Initialize the window
pygame.display.set_caption("Mamba")
window = objGame.window

# FPS (Frames per second controller)
fps = pygame.time.Clock()

change_to = objGame.change_to
direction = objGame.direction

# Main
while True:
    # Draw the background
    window.blit(objGame.BACKGROUND_IMG, (0, 0))

    # Print the X/Y coordinates of the snake
    # for debugging the snake movement
    # Uncomment the following line to print the coordinates
    # print(f"X:{objGame.mamba_position[0]}", f"Y:{objGame.mamba_position[1]}")

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

    # Snake body
    objGame.mamba_body.insert(0, list(objGame.mamba_position))

    # Conditional statement when the snake eats the food
    if objGame.mamba_position == objGame.get_food_position():

        # Play chewing sound
        objGame.SOUND_CHEW.play()

        # Add points to the score
        objGame.set_score()

        # Increase the speed of the snake
        objGame.set_speed()

        # Set the food
        objGame.set_food_spawn(False)
    else:
        # Remove the last segment of the snake body
        objGame.mamba_body.pop()

    # Place the food at a random spot within the window
    if not objGame.get_food_spawn():

        objGame.set_food_color()
        objGame.set_food_position()

    '''# Set a border around the snake
    for segment in objGame.mamba_body:
        pygame.draw.circle(window, objGame.COLOR["grey"], (segment[0] + 20, segment[1] + 20), 20)

        #pygame.draw.rect(window, objGame.COLOR["grey"], pygame.Rect(segment[0], segment[1], 40, 40))'''

    for i in range(len(objGame.mamba_body) - 1):
        start_pos = objGame.mamba_body[i][0] + 20, objGame.mamba_body[i][1] + 20
        end_pos = objGame.mamba_body[i + 1][0] + 20, objGame.mamba_body[i + 1][1] + 20
        objGame.draw_rounded_line(window, objGame.COLOR["grey"], start_pos, end_pos, 40)


    # Set a border around the food
    food_border = pygame.Rect(objGame.food_position[0], objGame.food_position[1], 40, 40)

    # Draw the food in the window
    pygame.draw.circle(window, objGame.get_food_color(), food_border.center, 20)

    # Game Over conditions
    # Touching the window border (X)
    if objGame.mamba_position[0] < 0 or objGame.mamba_position[0] > (x - 40):
        objGame.SOUND_SMASH.play()
        objGame.game_over()
    # Touching the window border (Y)
    if objGame.mamba_position[1] < 0 or objGame.mamba_position[1] > (y - 40):
        objGame.SOUND_SMASH.play()
        objGame.game_over()

    # Touching the snake body
    for segment in objGame.mamba_body[1:]:
        if objGame.mamba_position[0] == segment[0] and objGame.mamba_position[1] == segment[1]:
            objGame.SOUND_SMASH.play()
            objGame.game_over()

    # Show the Score
    objGame.show_score(objGame.COLOR["white"])

    # Update the window
    pygame.display.update()

    # Update the frames inside the window
    fps.tick(objGame.get_speed())
