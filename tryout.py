from datetime import datetime
import pygame
pygame.init()
from definition import myfontsmall, myfont, black, white
from clock_date import run_clock_date

size = width, height = 320, 240



screen = pygame.display.set_mode(size)

run = True
while run:

	pygame.time.delay(500)
	run_clock_date(screen)


pygame.quit()
