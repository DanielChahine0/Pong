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
PLAYER_SPEED = 10

# Ball constant
BALL_SIZE = 10
BALL_X = X_GAP + PLAYER_WIDTH
BALL_Y = HEIGHT//2 - BALL_SIZE//2
BALL_VEL_X = 5
BALL_VEL_Y = 5
MAX_Y_VEL = 5

# Outer Lines
LINE_WIDTH = 5
SMALL_WIDTH = 5

# Score
SCORE1 = 0
SCORE2 = 0
pygame.font.init()
FONT = pygame.font.SysFont("impact", 100)
SCORE_MARGIN = 10


# Initializing pygame
pygame.init()
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")
"""
----------------------------------------------------------------
                            Functions
----------------------------------------------------------------
"""


# Function that keeps track of the score and allows one of the player to lose
def lose():
    global SCORE1, SCORE2, BALL_X, BALL_Y, BALL_VEL_X, BALL_VEL_Y

    if BALL_X <= LINE_WIDTH:
        SCORE1 += 1
    if BALL_X >= WIDTH - BALL_SIZE - LINE_WIDTH:
        SCORE2 += 1

    BALL_X = X_GAP + PLAYER_WIDTH
    BALL_Y = HEIGHT//2 - BALL_SIZE//2
    BALL_VEL_X = 5
    BALL_VEL_Y = 5


# Detects the collision between the ball and players
def detect_collision():
    global BALL_VEL_X

    # if the ball touches the left player
    if X_GAP <= BALL_X <= X_GAP+PLAYER_WIDTH:
        if PLAYER_1_Y <= BALL_Y <= PLAYER_1_Y+PLAYER_HEIGHT:
            BALL_VEL_X = - BALL_VEL_X

    # if the ball touches the right player
    if WIDTH - X_GAP >= BALL_X >= WIDTH - X_GAP - PLAYER_WIDTH:
        if PLAYER_2_Y <= BALL_Y <= PLAYER_2_Y + PLAYER_HEIGHT:
            BALL_VEL_X = - BALL_VEL_X


# Draws the black screen on the back
def draw_bg():
    WINDOW.fill("black")


# Draws the players
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


# Draw the ball and handle its movement
def draw_ball():
    """
    This function draws the ball
    """
    global BALL_Y, BALL_X, BALL_VEL_X, BALL_VEL_Y

    ball = pygame.Rect(BALL_X, BALL_Y, BALL_SIZE, BALL_SIZE)

    # If the ball touches the right or left border
    if BALL_X > WIDTH-BALL_SIZE-LINE_WIDTH or BALL_X < LINE_WIDTH:
        lose()

    # If the ball hit the bottom or upper border
    if BALL_Y < 0 or BALL_Y > HEIGHT - BALL_SIZE:
        BALL_VEL_Y = -BALL_VEL_Y

    BALL_Y += BALL_VEL_Y
    BALL_X += BALL_VEL_X

    pygame.draw.rect(WINDOW, "white", ball)


def draw_score():
    score1 = FONT.render(f"{SCORE1}", True, "white")
    score2 = FONT.render(f"{SCORE2}", True, "white")
    # The score on the left
    WINDOW.blit(score2, (WIDTH//2-score2.get_width()-20, LINE_WIDTH+SCORE_MARGIN))
    # The score on the right
    WINDOW.blit(score1, (WIDTH//2+20, LINE_WIDTH+SCORE_MARGIN))


def draw_lines():
    line_top = pygame.Rect(0, 0, WIDTH, LINE_WIDTH)
    line_right = pygame.Rect(WIDTH-LINE_WIDTH, 0, LINE_WIDTH, HEIGHT)
    line_bottom = pygame.Rect(0, HEIGHT-LINE_WIDTH, WIDTH, LINE_WIDTH)
    line_left = pygame.Rect(0, 0, LINE_WIDTH, HEIGHT)

    pygame.draw.rect(WINDOW, "white", line_top)
    pygame.draw.rect(WINDOW, "white", line_right)
    pygame.draw.rect(WINDOW, "white", line_bottom)
    pygame.draw.rect(WINDOW, "white", line_left)

    num_of_rect = HEIGHT//SMALL_WIDTH
    for i in range(num_of_rect):
        small_rect = pygame.Rect(WIDTH//2, i*20+5, SMALL_WIDTH, SMALL_WIDTH)
        pygame.draw.rect(WINDOW, "white", small_rect)


# Fully drawing function - draws the background and player and the ball
def draw():
    """
    This function draws the game
    """
    draw_bg()
    draw_players()
    draw_ball()
    detect_collision()
    draw_lines()
    draw_score()

    pygame.display.update()


def main():
    """
    This is the main function of the program
    """
    # Creating the game loop
    running = True

    # Getting the global variables
    global PLAYER_1_Y, PLAYER_2_Y, BALL_VEL_Y, PLAYER_SPEED

    while running:
        clock = pygame.time.Clock()

        for event in pygame.event.get():
            # If the user closes the window
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        keys = pygame.key.get_pressed()

        # PLAYER ON THE LEFT
        if keys[pygame.K_s]:
            if HEIGHT - PLAYER_HEIGHT >= PLAYER_1_Y:
                PLAYER_1_Y += PLAYER_SPEED

        if keys[pygame.K_w]:
            if PLAYER_1_Y >= LINE_WIDTH:
                PLAYER_1_Y -= PLAYER_SPEED

        # PLAYER ON THE RIGHT
        if keys[pygame.K_DOWN]:
            if HEIGHT - PLAYER_HEIGHT - LINE_WIDTH >= PLAYER_2_Y:
                PLAYER_2_Y += PLAYER_SPEED

        if keys[pygame.K_UP]:
            if PLAYER_2_Y >= LINE_WIDTH:
                PLAYER_2_Y -= PLAYER_SPEED

        # Control Game Speed
        clock.tick(60)

        # Draw the
        draw()


# Make sure to run this file directly and not imported
if __name__ == "__main__":
    main()
