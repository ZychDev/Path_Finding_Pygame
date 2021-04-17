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
test = 5
array = [[0 for i in range(test)] for j in range(test)]

#class rectangle
class point:
	def __init__(self, x, y, color):
		self.x = x 
		self.y = y 
		self.color = color

	def position(self):
		return self.x, self.y

#functions
def create_array(array,width,size_rect,red):
	x = 0
	y = 0
	for i in array:
		for j in i:
			if y == width:
				y = 0
				print(hello)
			else:
				j = point(x,y,red)
				print(j.x , j.x)
				y += 20



#main loop

create_array(array, width, test, red)

start = True
while start:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			start = False
		elif event.type == pygame.KEYDOWN:
			if event.key == K_ESCAPE:
				start = False


	pygame.display.flip()



