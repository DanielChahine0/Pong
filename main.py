"""
This is a remake of the game Pong using pygame
    no photos will be used, it will mainly be consisted of squares and rectangles
"""
import pygame


"""
----------------------------------------------------------------
                            Constants
----------------------------------------------------------------
"""
# Window sizes
WIDTH = 800
HEIGHT = 600

# Players constants
X_GAP = 50
PLAYER_WIDTH = 7
PLAYER_HEIGHT = 100
PLAYER_1_X = X_GAP
PLAYER_1_Y = HEIGHT//2-PLAYER_HEIGHT//2
PLAYER_2_X = WIDTH-X_GAP
PLAYER_2_Y = HEIGHT//2-PLAYER_HEIGHT//2
PLAYER_SPEED = 5


# Initializing pygame
pygame.init()
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")
"""
----------------------------------------------------------------
                            Functions
----------------------------------------------------------------
"""


def draw_bg():
    WINDOW.fill("black")


def draw_players():
    """
    This function draws the players
    """
    # initializing the players
    player1 = pygame.Rect(PLAYER_1_X, PLAYER_1_Y, PLAYER_WIDTH, PLAYER_HEIGHT)
    player2 = pygame.Rect(PLAYER_2_X, PLAYER_2_Y, PLAYER_WIDTH, PLAYER_HEIGHT)

    # Drawing the players
    pygame.draw.rect(WINDOW, "white", player1)
    pygame.draw.rect(WINDOW, "white", player2)


def draw():
    """
    This function draws the game
    """
    draw_bg()
    draw_players()

    pygame.display.update()


def main():
    """
    This is the main function of the program
    """
    # Creating the game loop
    running = True

    # Getting the global variables
    global PLAYER_1_Y, PLAYER_2_Y, PLAYER_SPEED

    while running:
        clock = pygame.time.Clock()

        for event in pygame.event.get():
            # If the user closes the window
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                # if event.key == pygame.K_DOWN:
                #     if HEIGHT - PLAYER_HEIGHT > PLAYER_1_Y > 0:
                #         PLAYER_1_Y += 10

        keys = pygame.key.get_pressed()

        # PLAYER ON THE LEFT
        if keys[pygame.K_s]:
            if HEIGHT - PLAYER_HEIGHT >= PLAYER_1_Y:
                PLAYER_1_Y += PLAYER_SPEED

        if keys[pygame.K_w]:
            if PLAYER_1_Y >= 0:
                PLAYER_1_Y -= PLAYER_SPEED

        if keys[pygame.K_DOWN]:
            if HEIGHT - PLAYER_HEIGHT >= PLAYER_2_Y:
                PLAYER_2_Y += PLAYER_SPEED

        if keys[pygame.K_UP]:
            if PLAYER_2_Y >= 0:
                PLAYER_2_Y -= PLAYER_SPEED

        # Control Game Speed
        clock.tick(60)

        draw()


# Make sure to run this file directly and not imported
if __name__ == "__main__":
    main()
