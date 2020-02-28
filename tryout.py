from datetime import datetime
import pygame, sys, os

pygame.init()
from definition import myfontsmall, myfont, black, white
from clock_date import run_clock_date

size = width, height = 680,480
os.environ['SDL_VIDEO_WINDOW_POS'] = "0,0"
screen = pygame.display.set_mode(size)

run = True
while run:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	pygame.time.delay(500)
	run_clock_date(screen)


pygame.quit()
