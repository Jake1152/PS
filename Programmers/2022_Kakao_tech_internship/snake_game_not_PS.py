import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
width = 640
height = 480
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Define colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Define the snake's initial position and movement
snake_position = [[100, 50], [90, 50], [80, 50]]
snake_body = pygame.Surface((10, 10))
snake_body.fill(GREEN)
direction = 'RIGHT'

# Define the food's position
food_position = [random.randint(1, (width // 10) - 1) * 10,
                 random.randint(1, (height // 10) - 1) * 10]
food = pygame.Surface((10, 10))
food.fill(RED)

# Define the clock
clock = pygame.time.Clock()

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        # Handle arrow key presses to change the snake's direction
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != 'DOWN':
                direction = 'UP'
            elif event.key == pygame.K_DOWN and direction != 'UP':
                direction = 'DOWN'
            elif event.key == pygame.K_LEFT and direction != 'RIGHT':
                direction = 'LEFT'
            elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                direction = 'RIGHT'

    # Update the snake's position
    if direction == 'UP':
        snake_position[0][1] -= 10
    elif direction == 'DOWN':
        snake_position[0][1] += 10
    elif direction == 'LEFT':
        snake_position[0][0] -= 10
    elif direction == 'RIGHT':
        snake_position[0][0] += 10

    # Check if the snake has collided with the food
    if snake_position[0] == food_position:
        # Add a new segment to the snake
        snake_position.append([0, 0])

        # Generate new food position
        food_position = [random.randint(1, (width // 10) - 1) * 10,
                         random.randint(1, (height // 10) - 1) * 10]

    # Check if the snake has collided with itself or the window boundaries
    if (snake_position[0][0] < 0 or snake_position[0][0] >= width or
            snake_position[0][1] < 0 or snake_position[0][1] >= height or
            snake_position[0] in snake_position[1:]):
        # Game over
        pygame.quit()
        quit()

    # Move the rest of the snake's body
    for i in range(len(snake_position) - 1, 0, -1):
        snake_position[i] = list(snake_position[i - 1])

    # Clear the window
    window.fill(BLACK)

    # Draw the snake
    for pos in snake_position:
        window.blit(snake_body, pos)

    # Draw the food
    window.blit(food, food_position)

    # Update the display
    pygame.display.update()

    # Set the game's frame rate
    clock.tick(20)
