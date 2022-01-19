import pygame
import time
import random
from pygame.locals import *


#Initialze pygame
pygame.init()

#Defining RGB values for colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (174, 182, 191)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
ORANGE = (255, 130, 0)
GOLD = (230, 215, 0)
YELLOW = (255,255,0)

font_comic = pygame.font.SysFont('Comic Sans MS', 40)
font_times = pygame.font.SysFont('Times New Roman', 40)
font_points = pygame.font.SysFont('Times New Roman', 20)

screen = pygame.display.set_mode((800,650)) #Initialzing display
pygame.display.set_caption('SPACE INVADER') 
clock = pygame.time.Clock()

score=0
try:
	file_highscore=open("highscore.txt",'r') #reads highscore from text file
	file_highscore.seek(0,0)
	highest_score=int(file_highscore.read())
	file_highscore.close()
except:
	highest_score=0

def WelcomeScreen(): #initial screen before the game begins
	global quit,game_state,invader1,invader2,invaderM,invader3
	mouse_pos=pygame.mouse.get_pos()
	mouse_click=pygame.mouse.get_pressed()
	screen.fill(GREY)

	logo = pygame.image.load('space-invaders-logo_transparent.png')
	screen.blit(logo,(30,40))

	screen.blit(invader1,(150,550))
	points1 = font_points.render(':- 10 POINTS', False, BLUE)
	screen.blit(points1,(200,550))
	screen.blit(invader2,(450,550))
	points1 = font_points.render(':- 20 POINTS', False, BLUE)
	screen.blit(points1,(500,550))
	screen.blit(invader3,(150,600))
	points1 = font_points.render(':- 30 POINTS', False, BLUE)
	screen.blit(points1,(200,600))
	screen.blit(invaderM,(450,600))
	points1 = font_points.render(':- Mystery (Hit Thrice)', False, BLUE)
	screen.blit(points1,(500,600))


	if ((mouse_pos[0]-400)**2 + (mouse_pos[1]-400)**2) <=8100 :
		pygame.draw.circle(screen, RED,(400,400),90)
		if mouse_click[0]:
			game_state = 1
			Game()
			
	else:
		pygame.draw.circle(screen, BLUE,(400,400),90)

	text_welcome = font_times.render('START', False, WHITE)
	screen.blit(text_welcome,(340,360))
	text_welcome = font_times.render('GAME', False, WHITE)
	screen.blit(text_welcome,(340,400))

def Game(): #The game has begin... initialize all classes and display
	global score,highest_score,ship,ship_x,ship_y,vel_ship,invader1a_list,invader1b_list,invader1c_list,invader2_list,invader3_list,invader_mys,obstruct1,obstruct2,obstruct3,obstruct4,invader1,invader2,invader3,invaderM,bullet,i1fire,i2fire,i3fire,i4fire,speed_invader1,speed_invader2,speed_invader3,speed_mys,bullet1,vel_bull,fire_alive

	background = pygame.image.load('background.png')
	screen.blit(background,(0,0))
	text_score = font_comic.render('SCORE:', False, GOLD)
	screen.blit(text_score,(150,25))
	text_score = font_comic.render(str(score), False, ORANGE)
	screen.blit(text_score,(270,25))
	text_score = font_comic.render('HIGH SCORE:', False, GOLD)
	screen.blit(text_score,(430,25))
	if highest_score<score:
		highest_score=score
		fo=open('highscore.txt','w')
		fo.write(str(highest_score))
		fo.close()
	text_score = font_comic.render(str(highest_score), False, ORANGE)
	screen.blit(text_score,(630,25))
	Spaceship()
	for i in range(len(invader1a_list)):
		if invader1a_list[i].isAlive:
			invader1a_list[i].Get_Invader()
		if invader1b_list[i].isAlive:
			invader1b_list[i].Get_Invader()
		if invader1c_list[i].isAlive:
			invader1c_list[i].Get_Invader()
	for i in range(len(invader2_list)):
		if invader2_list[i].isAlive:	
			invader2_list[i].Get_Invader()
		if invader3_list[i].isAlive:
			invader3_list[i].Get_Invader()
	if invader_mys.isAlive:
			invader_mys.Get_Invader()
	Move_Invader()
	for obstructs in obstruct1:
		if obstructs.isAlive:
			obstructs.Obs()
	for obstructs in obstruct2:
		if obstructs.isAlive:
			obstructs.Obs()
	for obstructs in obstruct3:
		if obstructs.isAlive:
			obstructs.Obs()
	for obstructs in obstruct4:
		if obstructs.isAlive:
			obstructs.Obs()
	Reach_bottom()
	Check_hit()
	if bullet1.isAlive:
		bullet1.bullet_y+=vel_bull
		bullet1.Get_Bullet()
		if bullet1.bullet_y<= 50:
			bullet1.isAlive=False
	firebyinvader()
	checkhit_invader()


			
def Left_press(): #increase velocity
	global vel_ship
	vel_ship=-10
	pass

def Right_press(): #increase velocity
	global vel_ship
	vel_ship=10
	pass

def Release_arrowkey(): #velocity=0
	global vel_ship
	vel_ship=0
	pass

def Game_end(): ##Increase size of font and positioning correctly left
	global quit,game_state
	mouse=pygame.mouse.get_pos()
	click=pygame.mouse.get_pressed()
	screen.fill(GOLD)
	myfont_win = pygame.font.SysFont('Comic Sans MS', 120)
	col=random.choice((1,2,3))
	if game_state==2:
		game_endtext='YOU LOST <_>..!!'
	if game_state == 3:
		game_endtext='YOU WONNN <_>..!!'
	if col==1:
		textsurface=myfont_win.render(str(game_endtext),False, BLUE)
		screen.blit(textsurface,(100,200)) 
	if col==2:
		textsurface=myfont_win.render(str(game_endtext),False, ORANGE)
		screen.blit(textsurface,(100,200))
	if col==3:
		textsurface=myfont_win.render(str(game_endtext),False, RED)
		screen.blit(textsurface,(100,200))
	if mouse[0] < 375 and mouse[0] > 200 and mouse[1] < 450 and mouse[1] > 400:
		pygame.draw.rect(screen, GREEN,(200, 400,125,50))
		if click[0]==1:
			quit=True
	else:
		pygame.draw.rect(screen,RED,(200,400,125,50))   
	textsurface = myfont_quit.render('QUIT', False, WHITE)
	screen.blit(textsurface,(222,410)) 
	if mouse[0] < 650 and mouse[0] > 430 and mouse[1] < 450 and mouse[1] > 400:
		pygame.draw.rect(screen, GREEN,(410,400,220,50))
		if click[0]==1:
			initial()
			game_state = 1	
			Game()
	else:
		pygame.draw.rect(screen,BLUE,(410,400,220,50))   
	textsurface = myfont_quit.render('PLAY AGAIN', False, WHITE)
	screen.blit(textsurface,(435,412))

def Fire_Spaceship(): #release a bullet from same x coordinate upwards
	global bullet1,vel_bull
	if bullet1.isAlive:
		pass
	else:
		bullet1=Bullet(bullet)
		bullet1.isAlive = True
		vel_bull=-15
	pass

def firebyinvader():
	global i1fire,i2fire,i3fire,i4fire,fire_alive,fire,fire_y,shooter,fire_x
	shot = [i1fire,i2fire,i3fire,i4fire]
	if fire_alive == False:
		fire = random.choice(shot)
		fire_alive = True
		if fire == i1fire:
			shooter = random.choice(invader1b_list)
			fire_y=shooter.invader_y
			fire_x=shooter.invader_x
		elif fire == i2fire:
			shooter = random.choice(invader3_list)
			fire_y=shooter.invader_y
			fire_x=shooter.invader_x
		elif fire == i3fire:
			shooter = random.choice(invader2_list)
			fire_y=shooter.invader_y
			fire_x=shooter.invader_x
		else:
			shooter = invader_mys
			fire_y=shooter.invader_y
			fire_x=shooter.invader_x

	screen.blit(fire,(fire_x,fire_y))
	fire_y+=7
	if fire_y > ship_y+5:
		fire_alive=False



def initial():
	global ship,ship_x,ship_y,vel_ship,invader1a_list,invader1b_list,invader1c_list,invader2_list,invader3_list,invader_mys,obstruct1,obstruct2,obstruct3,obstruct4,invader1,invader2,invader3,invaderM,bullet,i1fire,i2fire,i3fire,i4fire,speed_invader1,speed_invader2,speed_invader3,speed_mys,bullet1,score,fire_alive
	# Spaceship object and starting coordinates
	score=0
	ship = pygame.image.load('tank.png').convert_alpha()
	ship_y = screen.get_height() - 70
	ship_x = screen.get_width()/2 - ship.get_width()/2
	vel_ship=0
	fire_alive = False
	# Invader Class
	invader1 = pygame.image.load('i1.png').convert_alpha()
	invader2 = pygame.image.load('i3.png').convert_alpha()  
	invader3 = pygame.image.load('i2.png').convert_alpha()  
	invaderM = pygame.image.load('i4.png').convert_alpha()
	i1fire = pygame.image.load('i1fire.png')
	i2fire = pygame.image.load('i2fire.png')
	i3fire = pygame.image.load('i3fire.png')
	i4fire = pygame.image.load('i4fire.png')
	bullet = pygame.image.load('bullet.jpg')
	bullet1 = Bullet(bullet)
	bullet2 = Bullet(i1fire)
	bullet3 = Bullet(i2fire)
	bullet4 = Bullet(i3fire)
	bullet5 = Bullet(i4fire)
	speed_invader1 = 2
	speed_invader2 = -3
	speed_invader3 = 3
	speed_mys = 8
	##Initalise invaders
	invader1a_list=[Invader1(invader1,i,300) for i in range(200,650,50)]
	invader1b_list=[Invader1(invader1,i,265) for i in range(200,650,50)]
	invader1c_list=[Invader1(invader1,i,230) for i in range(200,650,50)]
	invader2_list=[Invader2(invader2,i,185) for i in range(220,680,50)]
	invader3_list=[Invader3(invader3,i,140) for i in range(220,590,40)]
	invader_mys=Invader_Mystery(invaderM,380,100)
	obstruct1 = [Obstruct(100+i,500+j) for j in range(0,30,10) for i in range (0,50,10)]
	obstruct2 = [Obstruct(300+i,500+j) for j in range(0,30,10) for i in range (0,50,10)]
	obstruct3 = [Obstruct(500+i,500+j) for j in range(0,30,10) for i in range (0,50,10)]
	obstruct4 = [Obstruct(700+i,500+j) for j in range(0,30,10) for i in range (0,50,10)]

# Function to change positon and display Spaceship
def Spaceship():
	global vel_ship,ship,ship_y,ship_x
	ship_x+=vel_ship
	if ship_x <= 0 + 5: #stop if hits left wall
		ship_x-=vel_ship
		vel_ship=0
	if ship_x >= 800 - ship.get_width(): #stop if hits right wall
		ship_x-=vel_ship
		vel_ship=0
	screen.blit(ship,(ship_x,ship_y))

class Invader1: #score=10
	def __init__(self,invader1,invader_x,invader1_y):
		self.invader1 = invader1
		self.invader_x = invader_x
		self.invader_y = invader1_y
		self.isAlive = True
	
	def Get_Invader(self):
		screen.blit(self.invader1,(self.invader_x,self.invader_y))

	def Invader_Attack(self):
		global score
		self.isAlive = False
		score += 10 #score=10

class Invader2: #score=20
	def __init__(self,invader2,invader_x,invader2_y):
		self.invader2 = invader2
		self.invader_x = invader_x
		self.invader_y = invader2_y
		self.isAlive = True
	
	def Get_Invader(self):
		screen.blit(self.invader2,(self.invader_x,self.invader_y))

	def Invader_Attack(self):
		global score
		self.isAlive = False
		score += 20 #score=20

class Invader3: #score=30
	def __init__(self,invader3,invader_x,invader3_y):
		self.invader3 = invader3
		self.invader_x = invader_x
		self.invader_y = invader3_y
		self.isAlive = True
	
	def Get_Invader(self):
		screen.blit(self.invader3,(self.invader_x,self.invader_y))

	def Invader_Attack(self):
		global score
		self.isAlive = False
		score += 30 #score=30

class Invader_Mystery: #needs to be attacked thrice to be killed and score =100
	def __init__(self,invader_m,invader_x,invaderM_y):
		self.invaderM = invader_m
		self.invader_x = invader_x
		self.invader_y = invaderM_y
		self.isAlive = True
		self.count=0
	
	def Get_Invader(self):
		screen.blit(self.invaderM,(self.invader_x,self.invader_y))

	def Invader_Attack(self):
		global score
		self.count+=1
		if self.count==3:
			self.isAlive = False 
			score += 100

class Bullet:
	global ship_x,ship_y
	def __init__(self,bullet):
		self.bullet = bullet
		self.bullet_x = ship_x + ship.get_width()/2 -5
		self.bullet_y = ship_y
		self.isAlive = False

	def Get_Bullet(self):
		screen.blit(self.bullet,(self.bullet_x,self.bullet_y))

# Invader Movement Function
def Move_Invader():
	global invader1a_list,invader2_list,invader1b_list,invader1c_list,invader3_list,invader_mys,speed_invader1,speed_invader2,speed_mys,speed_invader3
	
	left = 0
	right = -1
	flag_left,flag_right = 1,1
	while flag_left or flag_right: #to check the leftmost and rightmost alive row
		if invader1a_list[left].isAlive or invader1b_list[left].isAlive or invader1c_list[left].isAlive:
			flag_left=0
		else:
			left += 1
		if invader1a_list[right].isAlive or invader1b_list[right].isAlive or invader1c_list[right].isAlive:
			flag_right=0
		else:
			right -= 1

	if (invader1a_list[right].invader_x >= 750 or invader1a_list[left].invader_x <= 15) :
		speed_invader1 *= -1.05
	for invaders in invader1a_list:
		invaders.invader_x += speed_invader1
		invaders.invader_y += 0.13
	for invaders in invader1b_list:
		invaders.invader_x += speed_invader1
		invaders.invader_y += 0.13
	for invaders in invader1c_list:
		invaders.invader_x += speed_invader1
		invaders.invader_y += 0.13

	left = 0
	right = -1
	flag_left,flag_right = 1,1
	while flag_left or flag_right: #to check the leftmost and rightmost alive row
		if invader2_list[left].isAlive:
			flag_left=0
		else:
			left += 1
		if invader2_list[right].isAlive:
			flag_right=0
		else:
			right -= 1

	if (invader2_list[right].invader_x >= 750 or invader2_list[left].invader_x <= 15) :
		speed_invader2 *= -1.03
	for invaders in invader2_list:
		invaders.invader_x += speed_invader2
		invaders.invader_y += 0.13

	left = 0
	right = -1
	flag_left,flag_right = 1,1
	while flag_left or flag_right: #to check the leftmost and rightmost alive row
		if invader3_list[left].isAlive:
			flag_left=0
		else:
			left += 1
		if invader3_list[right].isAlive:
			flag_right=0
		else:
			right -= 1

	if (invader3_list[right].invader_x >= 750 or invader3_list[left].invader_x <= 15) :
		speed_invader3 *= -1.03
	for invaders in invader3_list:
		invaders.invader_x += speed_invader3
		invaders.invader_y += 0.13

	if (invader_mys.invader_x >= 740 or invader_mys.invader_x <=15 ):
		speed_mys *= -1.01
	invader_mys.invader_x += speed_mys
	invader_mys.invader_y += 0.1

class Obstruct:
	def __init__(self,x,y):
		self.x = x
		self.y = y
		self.isAlive = True

	def Obs(self):
		'''pygame.draw.rect(screen,GREY,(self.x,self.y,10,10))
								for i in range (0,4):
									pygame.draw.line(screen,BLACK,(self.x,self.y+2*(i+1)),(self.x+10,self.y+2*(i+1)))
									pygame.draw.line(screen,BLACK,(self.x+2*(i+1),self.y),(self.x+2*(i+1),self.y+10))'''
		obs_image=pygame.image.load('spray_10.jpg').convert_alpha()
		screen.blit(obs_image,(self.x,self.y))

	def Obs_Attack():
		self.isAlive = False

def Reach_bottom():
	global game_state
	for invader in invader1a_list:
		if invader.isAlive and (invader.invader_y>450):
			game_state=2
			return False
	for invader in invader1b_list:
		if invader.isAlive and (invader.invader_y>450):
			game_state=2
			return False
	for invader in invader1c_list:
		if invader.isAlive and (invader.invader_y>450):
			game_state=2
			return False
	for invader in invader2_list:
		if invader.isAlive and (invader.invader_y>450):
			game_state=2
			return False
	for invader in invader3_list:
		if invader.isAlive and (invader.invader_y>450):
			game_state=2
			return False
	if invader_mys.isAlive and (invader_mys.invader_y>410):
		game_state =2

def Check_hit():
	if bullet1.isAlive:
		for i in range(len(invader1a_list)):
			if invader1a_list[i].isAlive:
				if bullet1.bullet_x+3 >= invader1a_list[i].invader_x and bullet1.bullet_x+3 <= invader1a_list[i].invader_x + 28 and bullet1.bullet_y+9 >= invader1a_list[i].invader_y and bullet1.bullet_y+9 <= invader1a_list[i].invader_y + 26:
					bullet1.isAlive = False
					invader1a_list[i].Invader_Attack()
			if invader1b_list[i].isAlive:
				if bullet1.bullet_x+3 >= invader1b_list[i].invader_x and bullet1.bullet_x+3 <= invader1b_list[i].invader_x + 28 and bullet1.bullet_y+9 >= invader1b_list[i].invader_y and bullet1.bullet_y+9 <= invader1b_list[i].invader_y + 26:
					bullet1.isAlive = False
					invader1a_list[i].Invader_Attack()
			if invader1c_list[i].isAlive:
				if bullet1.bullet_x+3 >= invader1c_list[i].invader_x and bullet1.bullet_x+3 <= invader1c_list[i].invader_x + 28 and bullet1.bullet_y+9 >= invader1c_list[i].invader_y and bullet1.bullet_y+9 <= invader1c_list[i].invader_y + 26:
					bullet1.isAlive = False
					invader1a_list[i].Invader_Attack()
		for i in range(len(invader2_list)):
			if invader2_list[i].isAlive:	
				if bullet1.bullet_x+3 >= invader2_list[i].invader_x and bullet1.bullet_x+3 <= invader2_list[i].invader_x + 35 and bullet1.bullet_y+9 >= invader2_list[i].invader_y and bullet1.bullet_y+9 <= invader2_list[i].invader_y + 24:
					bullet1.isAlive = False
					invader2_list[i].Invader_Attack()
			if invader3_list[i].isAlive:
				if bullet1.bullet_x+3 >= invader3_list[i].invader_x and bullet1.bullet_x+3 <= invader3_list[i].invader_x + 28 and bullet1.bullet_y+9 >= invader3_list[i].invader_y and bullet1.bullet_y+9 <= invader3_list[i].invader_y + 26:
					bullet1.isAlive = False
					invader3_list[i].Invader_Attack()
		if invader_mys.isAlive:
				if bullet1.bullet_x+3 >= invader_mys.invader_x and bullet1.bullet_x+3 <= invader_mys.invader_x + 28 and bullet1.bullet_y+9 >= invader_mys.invader_y and bullet1.bullet_y+9 <= invader_mys.invader_y + 26:
					bullet1.isAlive = False
					invader_mys.Invader_Attack()

		for obstructs in obstruct1:
			if obstructs.isAlive:
				if bullet1.bullet_x+3 >= obstructs.x and bullet1.bullet_x+3 <= obstructs.x + 10 and bullet1.bullet_y+9 >= obstructs.y and bullet1.bullet_y+3 <= obstructs.y + 10:
					bullet1.isAlive = False
					obstructs.isAlive = False
		for obstructs in obstruct2:
			if obstructs.isAlive:
				if bullet1.bullet_x+3 >= obstructs.x and bullet1.bullet_x+3 <= obstructs.x + 10 and bullet1.bullet_y+9 >= obstructs.y and bullet1.bullet_y+3 <= obstructs.y + 10:
					bullet1.isAlive = False
					obstructs.isAlive = False
		for obstructs in obstruct3:
			if obstructs.isAlive:
				if bullet1.bullet_x+3 >= obstructs.x and bullet1.bullet_x+3 <= obstructs.x + 10 and bullet1.bullet_y+9 >= obstructs.y and bullet1.bullet_y+3 <= obstructs.y + 10:
					bullet1.isAlive = False
					obstructs.isAlive = False
		for obstructs in obstruct4:
			if obstructs.isAlive:
				if bullet1.bullet_x+3 >= obstructs.x and bullet1.bullet_x+3 <= obstructs.x + 10 and bullet1.bullet_y+9 >= obstructs.y and bullet1.bullet_y+3 <= obstructs.y + 10:
					bullet1.isAlive = False
					obstructs.isAlive = False
def checkhit_invader():
	global fire_alive,game_state
	if fire_alive==True:
		for obstructs in obstruct1:
			if obstructs.isAlive:
				if fire_x+3 >= obstructs.x and fire_x+3 <= obstructs.x + 10 and fire_y+9 >= obstructs.y and fire_y+3 <= obstructs.y + 10:
					fire_alive = False
					obstructs.isAlive = False
		for obstructs in obstruct2:
			if obstructs.isAlive:
				if fire_x+3 >= obstructs.x and fire_x+3 <= obstructs.x + 10 and fire_y+9 >= obstructs.y and fire_y+3 <= obstructs.y + 10:
					fire_alive = False
					obstructs.isAlive = False
		for obstructs in obstruct3:
			if obstructs.isAlive:
				if fire_x+3 >= obstructs.x and fire_x+3 <= obstructs.x + 10 and fire_y+9 >= obstructs.y and fire_y+3 <= obstructs.y + 10:
					fire_alive = False
					obstructs.isAlive = False
		for obstructs in obstruct4:
			if obstructs.isAlive:
				if fire_x+3 >= obstructs.x and fire_x+3 <= obstructs.x + 10 and fire_y+9 >= obstructs.y and fire_y+3 <= obstructs.y + 10:
					fire_alive = False
					obstructs.isAlive = False

		if (ship_x-5 < fire_x < ship_x + ship.get_width()-5) and (fire_y > ship_y):
			game_state=2
			Game_end()



##MAIN
initial()
WelcomeScreen() ## contains initial screen
## game state=0 means start page... =1 means game is going on... =2 means game lost... =3 means won the game
game_state=0 
quit=False
while not quit:
	if not game_state:
		WelcomeScreen()
	elif game_state==1:
		Game()
	elif game_state == 2:
		Game_end()
	elif game_state ==3:
		Game_end()

	for event in pygame.event.get(): 
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				Left_press()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RIGHT:
				Right_press()
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
				Release_arrowkey()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				Fire_Spaceship()
		if event.type == pygame.QUIT:
			quit = True
	
	clock.tick(20) #Sets FPS of the game
	pygame.display.update()

pygame.quit()