import pygame 
pygame.init()

#colors
black = [0, 0, 0]
red = [255, 0, 0]
green = [0,255,0]
blue = [0,0,255]

#screen settings
screen_size = width, height = 800, 800
screen = pygame.display.set_mode(screen_size)
screen.fill(black)

#rectangle
size = 20
size_rect =int( width / size)
test = 5

#class rectangle
class point:
	x = 0
	y = 0

	def __init__(self,color):
		self.color = color

	def set_position(self, x, y):
		self.x = x
		self.y = y

	def position(self):
		return self.x, self.y
	
	def position_x(self):
		return self.x
	
	def position_y(self):
		return self.y

	def change_color(self, col):
		self.color = col

	def return_color():
		return self.color

#create array of objects and input informations 
array_of_objects = [[point(red) for j in range(test)] for i in range(test)]

def start_point():
	x = int(input("Give point x: "))
	y = int(input("Give point y: "))
	return x,y

def quit_point():
	x = int(input("Give point x: "))
	y = int(input("Give point y: "))
	return x,y

start_points = start_point()
quit_points = quit_point()

print("Start points: ",start_points)
print("Quit points: ",quit_points)

#save data in rectangle objects
tmpx = 0
tmpy = 0
for i in array_of_objects:
	for z in i:
		z.set_position(tmpx,tmpy)	

		if z.position() == start_points:
			z.change_color(green)
		elif z.position() == quit_points:
			z.change_color(blue)

		tmpx += 20
	if(tmpx == 100):
		tmpy += 20
		tmpx = 0




#main loop
start = True
while start:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			start = False
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				start = False

	#draw rectaangles
	for z in array_of_objects:
		for c in z:
			pygame.draw.rect(screen, c.color, (c.x,c.y,20,20),1)
		
	pygame.display.flip()




