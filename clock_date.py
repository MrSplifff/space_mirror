from datetime import datetime
import pygame
from definition import myfontsmall, myfont, black, white

size = width, height = 320, 240



screen = pygame.display.set_mode(size)

def run_clock_date(screen):
    run = True
    while run:
    	current_time = datetime.now()
    	pygame.time.delay(500)

    	screen.fill(black)
    	time = myfont.render(current_time.strftime("%H:%M:%S"), 1, white)
    	date = myfontsmall.render(current_time.strftime("%d.%m.%Y"), 1, white)
    	screen.blit(time, (30, 30))
    	screen.blit(date, (35, 80))
    	pygame.display.update()
    pygame.quit()
