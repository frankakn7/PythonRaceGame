import pygame
import time
import random

pygame.init()

display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

crashed = False

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("A bit Racey")
clock = pygame.time.Clock()

myFont = pygame.font.Font(None, 40)

carImg = pygame.image.load('/Volumes/MBoss/Code/Python/RaceCare.png')
carImg = pygame.transform.scale(carImg, (50,75))

back1Img = pygame.image.load('/Volumes/MBoss/Code/Python/Background1.png')
back2Img = pygame.image.load('/Volumes/MBoss/Code/Python/Background2.png')
back3Img = pygame.image.load('/Volumes/MBoss/Code/Python/Background3.png')

class playerCar:
	def createVariables(self,x,y):
		self.x = x
		self.y = y
		self.width = 50
		self.height = 75
		self.spd = 5
		self.img = carImg
	def draw(self):
		gameDisplay.blit(self.img,(self.x,self.y))

class enemyCar:
	def createVariables(self,lane):
		self.width = 50
		self.height = 75
		self.lane = lane
		self.x = ((self.lane * 80) - 40)-(self.width*0.5)
		self.y = 0
		self.spd = random.randint(4,8)
		self.img = carImg
	def draw(self):
		gameDisplay.blit(self.img,(self.x,self.y))
	def move(self):
		self.y += self.spd
		self.draw()
	def detect(self,obj):
		if self.y >= display_height:
			self.createVariables(self.lane)
		if self.x <= obj.x + obj.width and obj.x <= self.x + self.width and self.y <= obj.y + obj.height and obj.y <= self.y + self.height:
			print("Hello")
			crashed = True
			pygame.quit()
			quit()

cars = []

for i in range(0,10):
	cars.append(enemyCar())
	cars[i].createVariables(i+1)

x = (display_width * 0.45)
y = (display_height * 0.7)

player = playerCar()
player.createVariables(x,y)


x_change = 0
y_change = 0

LeftKeyDown = False
RightKeyDown = False
UpKeyDown = False
DownKeyDown = False

Number = 1;

Score = 0;
scoreOutput = myFont.render("Score: "+str(Score), 1, black)

def drawBackground():
	global Number
	if (Number % 8) == 0:
		gameDisplay.blit(back1Img,(0,0))
		Number = 1
	elif (Number % 4) == 0:
		gameDisplay.blit(back2Img,(0,0))
		Number += 1
	else:
		gameDisplay.blit(back3Img,(0,0))
		Number += 1

while not crashed:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			crashed = True

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				LeftKeyDown = True
				RightKeyDown = False
			elif event.key == pygame.K_RIGHT:
				LeftKeyDown = False
				RightKeyDown = True
			
			if event.key == pygame.K_UP:
				UpKeyDown = True
				DownKeyDown = False
			elif event.key == pygame.K_DOWN:
				UpKeyDown = False
				DownKeyDown = True

		if event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT:
				LeftKeyDown = False
			if event.key == pygame.K_RIGHT:
				RightKeyDown = False
			if event.key == pygame.K_UP:
				UpKeyDown = False
			if event.key == pygame.K_DOWN:
				DownKeyDown = False

	if LeftKeyDown:
		x_change = -7
	elif RightKeyDown:
		x_change = 7
	else:
		x_change = 0
	
	if UpKeyDown:
		y_change = -7
	elif DownKeyDown:
		y_change = 7
	else:
		y_change = 0

	player.x += x_change
	
	if player.y + player.height <= display_height and player.y >= 0:
		player.y += y_change
	else:
		player.y -= y_change * 2

	if player.x + player.width  <= 0:
		player.x = display_width - player.width
	elif player.x >= display_width:
		player.x = 0 

	#gameDisplay.fill(white)
	drawBackground()
	player.draw()
	for i in range(0,len(cars)):
		cars[i].move()
		cars[i].detect(player)
	#print(crashed)
	Score += 1
	scoreOutput = myFont.render("Score: "+str(Score), 1, black)
	gameDisplay.blit(scoreOutput, ((display_width/2)-75,30))
	pygame.display.update()
	clock.tick(60)

pygame.quit()
quit()