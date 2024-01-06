import pygame


def main():
    white = (255, 255, 255)
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)

    height = 500
    width = 700

    pygame.init()

    window = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Testing shapes")

    window.fill(white)

    pygame.draw.rect(window, red, (20, height - 120, 20, 100), 0, 0, 0, 0, 0, 0)
    pygame.draw.circle(window, blue, (width / 2, height / 2), 50)
    pygame.draw.line(window, green, (width - 30, height - 20), (width - 30, 20), 20)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    return

        pygame.display.update()


if __name__ == '__main__':
    main()
