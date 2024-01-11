import sys
import pygame
import random
import time


global window
global height
global width


def random_array(length):
    try:
        length = int(length)
    except:
        print("Value needs to be a integer")
        sys.exit(1)

    if length < 1:
        print("Value needs to be larger than 0")
        sys.exit(1)
    array = [0] * length
    for i in range(length):
        array[i] = i + 1
    for i in range(100):
        random.shuffle(array)
    return array


def draw_array(array):
    global window
    global height
    global width

    v_len = len(array)
    v_max = max(array)
    white = (255, 255, 255)
    black = (0, 0, 0)

    window.fill(white)

    for i, e in enumerate(array):
        w = float(int(width) // v_len)
        h = float((height // v_max) * e)
        x = float((int(width) // v_len) * (i + 1))
        y = float(height - h)
        pygame.draw.rect(window, black, (x, y, w, h))

    return


def selection_sort_ascending(array):
    for i in range(len(array)):
        min_pos = i
        min = array[min_pos]
        for j in range(i + 1, len(array)):
            if array[j] < min:
                min_pos = j
                min = array[min_pos]

        if min_pos != i:
            array[min_pos] = array[i]
            array[i] = min

        draw_array(array)
        pygame.display.update()
        time.sleep(0.05)


def main():
    global window
    global height
    global width

    white = (255, 255, 255)
    array = random_array(100)

    height = 1080
    width = 1920

    pygame.init()
    window = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Visualization of Selection Sort")
    window.fill(white)
    pygame.time.Clock().tick(120)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    return

        selection_sort_ascending(array)

        draw_array(array)
        pygame.display.update()


if __name__ == '__main__':
    main()
