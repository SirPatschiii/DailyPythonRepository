import pygame
import sys


global window


def init():
    global window

    width = 300
    height = 200

    pygame.init()
    window = pygame.display.set_mode((width, height))
    pygame.display.set_caption("ComboBox")

    return


def draw_combobox():
    global window

    white = (255, 255, 255)
    black = (0, 0, 0)

    font = pygame.font.Font(None, 16)

    pygame.draw.rect(window, white, (50, 50, 200, 40))
    pygame.draw.rect(window, black, (50, 50, 200, 40), 1)

    text = font.render("Here should be an option", None, black)
    window.blit(text, (60, 60))

    return


def main():
    global window

    white = (255, 255, 255)

    init()
    draw_combobox()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        window.fill(white)
        draw_combobox()

        pygame.display.flip()


if __name__ == '__main__':
    main()
