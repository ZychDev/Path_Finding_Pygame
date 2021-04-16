import pygame 
pygame.init()

#colors
black = [0, 0, 0]
red = [255, 0, 0]

#screen settings
screen_size = width, height = 800, 800
screen = pygame.display.set_mode(screen_size)
screen.fill(black)

#rectangle
size = 20
size_rect =int( width / size)
tmp_x = 0
tmp_y = 0
array = [[0 for i in range(size_rect)] for j in range(size_rect)]

#class rectangle
class point:
	def __init__(self, x, y, color):
		self.x = x 
		self.y = y 
		self.color = color
	def position():
		return self.x, self.y

#Array Functions
def create_array(size, width, height, array):
	x = 0
	y = 0
	for i in range(size):
		for j in range(size):
			if y == width:
				y = 0
			array[i][j] = point(x, y, red)
			y += 20
		x += 20	
def draw_array(array, size, screen):
	for i in range(size):
		for j in range(size):
			pygame.draw.rect(screen, array[i][j].color, (array[i][j].x, array[i][j].y, 20, 20),1)
	

def show_array(array):
	for x in array:
		print(x)


#main loop
create_array(size, width, height, array)
draw_array(array, size, screen)

start = True
while start:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			start = False
		elif event.type == pygame.KEYDOWN:
			if event.key == K_ESCAPE:
				start = False


	pygame.display.flip()



