import pygame, sys

# Setup pygame/window ---------------------------------------- #
mainClock = pygame.time.Clock()
from pygame.locals import *

pygame.init()

pygame.display.set_caption('Escape the Crypt!')
icon = pygame.image.load('icon (2).png')
screen = pygame.display.set_mode((500, 500), 0, 32)

font = pygame.font.SysFont(None, 20)


def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


click = False


# menu screen and buttons

def text_objects(param, smallText):
    pass


def main_menu() -> object:
    while True:

        screen.fill((0, 0, 0))
        draw_text('main menu', font, (255, 255, 255), screen, 20, 20)

        #collision
        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(50, 100, 200, 50)
        button_2 = pygame.Rect(50, 200, 200, 50)
        if button_1.collidepoint((mx, my)):
            if click:
                game()
        if button_2.collidepoint((mx, my)):
            if click:
                options()
        pygame.draw.rect(screen, (255, 165, 0), button_1)
        pygame.draw.rect(screen, (255, 165, 0), button_2)




        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        mainClock.tick(60)


# game loop

def game():
    running = True
    while running:
        screen.fill((0, 0, 0))

        draw_text('Escape the crypt', font, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False


        #level 2

        pygame.display.set_caption('Escape the Crypt! Level 2')
        icon = pygame.image.load('icon (2).png')
        pygame.display.set_icon(icon)
        bg3 = pygame.image.load('sidec.png').convert()
        bg4 = pygame.image.load('sided.png').convert()
        bgx3 = 0
        bgx4 = bg3.get_width()
        clock = pygame.time.Clock()
        speed = 20

        # define score/points
        score = 0

        def return_points():
            print(score)

        # introduce player & guard

        px = 90
        py = 225
        pxc = 0

        player = pygame.image.load('player_sprite.png').convert_alpha()
        player_rect = player.get_rect().move(px, py)

        # introduce guard

        gx = 400
        gy = 225

        guard = pygame.image.load('guard_sprite.png').convert_alpha()
        guard_rect = guard.get_rect().move(gx, gy)

        # define player
        def player_blit():
            screen.blit(player, (px, py))

        # define guard
        def guard_blit():
            screen.blit(guard, (gx, gy))

        # scrolling background
        def redraw_bg():
            screen.blit(bg3, (bgx3, 0))
            screen.blit(bg4, (bgx4, 0))

        # main game loop
        game_loop = True
        while game_loop:
            # scrolling bg loop
            redraw_bg()
            clock.tick(speed)
            bgx3 -= 1.4
            bgx4 -= 1.4
            if bgx3 < bg3.get_width() * -1:
                bgx3 = bg3.get_width()
            if bgx4 < bg4.get_width() * -1:
                bgx4 = bg4.get_width()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_loop = False
                # get key presses
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        pxc = -5
                    if event.key == pygame.K_d:
                        pxc = 5
                    # change below to and when i can get collisions to work
                    if event.key == pygame.K_SPACE or player_rect.colliderect(guard_rect):
                        print('ATTACK!')
                        score = score + 10
                        return_points()
                    if event.key == pygame.K_r:
                        print('pick up!')
                    if event.key == pygame.K_u:
                        print('upgrade!')
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_a or event.key == pygame.K_d:
                        pxc = 0
            if score == 100:
                print('YOU WIN!')
                game_loop = False

            px += pxc
            player_blit()
            guard_blit()

            pygame.display.update()


# when presing the options button
def options():
    running = True
    while running:
        screen.fill((0, 0, 0))

        draw_text('options', font, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        pygame.display.update()
        mainClock.tick(60)


main_menu()


