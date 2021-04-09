import pygame 
pygame.init()

#colors
black = [0, 0, 0]
white = [255, 0, 0]

#screen settings
screen_size = width, height = 640, 800
screen = pygame.display.set_mode(screen_size)
screen.fill(black)

#main loop
start = True
while start:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			start = False
		elif event.type = KEYDOWN:
			if event.key

	pygame.draw.rect(screen, white, (0,0,50,50),2)
	pygame.display.flip()

