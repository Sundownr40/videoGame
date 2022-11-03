# content from kids can code http://kidscancode.org/blog/
# timer from https://stackoverflow.com/questions/30720665/countdown-timer-in-pygame
# more timer information http://cs.roanoke.edu/Fall2013/CPSC120A/pygame-1.9.1-docs-html/ref/time.html 
###############################################################################################################
# Goal: Collide with all pink boxes before the timer runs out!
# Rules: 12 second timer, one 700x700 grid. Player must collide with all pink boxes before the timer expires
# Feedback: Game will state wether or not you have impacted a pink block, as well as provide some messaging post-finish.
# Freedom: User may use WASD + Arrow Keys to move, subtract from (cancel out), or compound the speed if you're up to the challenge!

#Note to Mr. Cozort:
#Hello Mr. Cozort! I sincrerely hope you enjoy my game and that I make my programming thought processes clear in my comments.
#Originally, I wanted this game to be a sort of top-down shooter where you would have to dodge bullets, but after some
#editing and messing around with the collision models, I decided I wanted to create a time-based race game in a similar way 
#to how you might colect coins in some of those Mario levels. I actually stumbled on the delete-post-collision feature by accident!
# Anyways, I intend on incorperating some of this knowledge I've learned into my Final Project, which will likely be a platformer
#game as I watched some youtube videos which use a lot of what I've discussed below. 

#Thank you for reading this and I hope you enjoy my game!

# Here I import libraries and modules
import pygame as pg
from pygame.sprite import Sprite
from random import randint
#set vector
vec = pg.math.Vector2

#Game settings. One 700x700 black grid operating at 60fps.
WIDTH = 700
HEIGHT = 700
FPS = 60

#hello


#Define colors - I personally like having a lot of variety
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
ORANGE = (255, 100, 10)
ORANGEII = (255,128,0)
PINK = (255,20,147)
DARKGREEN = (85,107,47)

#Sprites. Setting classes (player as Orange) as well as creating characterisitcs for all
class Player(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = pg.Surface((25, 25))
        self.image.fill(ORANGE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2)
        self.pos = vec(WIDTH/2, HEIGHT/2)
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        self.yvel = 0
        self.xvel = 0
        print(self.rect.center)

#Setting the movement controlls. 
#I have intentionally made it so that by pressing on the "W" key and simultaneously the "up arrow" the player's movement will double!
#If you have great hand-eye cordination, this will generate an advantage for you.
    def controls(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_a]:
            self.rect.x -=5
        if keys[pg.K_d]:
            self.rect.x +=5
        if keys[pg.K_w]:
            self.rect.y -=5
        if keys[pg.K_s]:
            self.rect.y +=5
        if keys[pg.K_LEFT]:
            self.rect.x -=5
        if keys[pg.K_RIGHT]:
            self.rect.x +=5
        if keys[pg.K_UP]:
            self.rect.y -=5
        if keys[pg.K_DOWN]:
            self.rect.y +=5
#Setting movement boundaries so that the Orange Square cannot infinitely contunue out of bounds. That would be zero fun.
    def check_bounds(self):
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.x + 25 > WIDTH:
            self.rect.x = WIDTH - 25
        if self.rect.y + 25 > HEIGHT:
            self.rect.y = HEIGHT - 25
        if self.rect.y < 0:
            self.rect.y = 0

#If the Orange square hits the pink squares, delete the pink ones and print a message in the terminal
    def update(self):
        hits = pg.sprite.spritecollide(self, all_walls, all_pobjects, False)
        if hits:
            print("Only a few more blocks left to go!")

       #EXAMPLE: #mobhits = pg.sprite.spritecollide(self, all_walls, mob, False)
        #if hits:
           # print("hit by a mob")

        self.controls()
        self.check_bounds()
        #Ensures Orange box stays within the 700x700 grid

#Creating the Platform class and assigning certain charicteristics to them. I.E. pink
class Platform(Sprite):
    def __init__(self, x, y, w, h):
        Sprite.__init__(self)
        self.image = pg.Surface((w,h))
        self.image.fill(PINK)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y 

#Note to self: REMEMBER - CONTROL, UPDATE, RENDER!!!!!!!

# init pygame and create a window
pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT)) #In this case, it is 700px x 700px

#sets display caption, i.e. "Pink Rush - CJB" is this game's title
pg.display.set_caption("Pink Rush - CJB. Eliminate all the pink in 12 seconds!")
clock = pg.time.Clock()
  
# create a group for all sprites
all_sprites = pg.sprite.Group()
all_walls = pg.sprite.Group()
all_pobjects = pg.sprite.Group()
all_boxes = pg.sprite.Group()

#Instantiate the player class
player = Player()
##### Platforms #####

#Here I have made a number of platforms and given them characteristics to spawn randomly in the grid. The smaller ones are more difficult to navagate towards.

plat = Platform(randint(0, WIDTH), randint(0, HEIGHT), 50, 50)
plat1 = Platform(randint(0, WIDTH), randint(0, HEIGHT), 40, 40)
plat2 = Platform(randint(0, WIDTH), randint(0, HEIGHT), 30, 30)
plat3 = Platform(randint(0, WIDTH), randint(0, HEIGHT), 20, 20)
plat4 = Platform(randint(0, WIDTH), randint(0, HEIGHT), 100, 100)
plat5 = Platform(randint(0, WIDTH), randint(0, HEIGHT), 75, 75)
plat6 = Platform(randint(0, WIDTH), randint(0, HEIGHT), 90, 90)
plat7 = Platform(randint(0, WIDTH), randint(0, HEIGHT), 10, 10)
plat8 = Platform(randint(0, WIDTH), randint(0, HEIGHT), 40, 40)
plat9 = Platform(randint(0, WIDTH), randint(0, HEIGHT), 50, 50)
plat10 = Platform(randint(0, WIDTH), randint(0, HEIGHT), 45, 45)
plat11 = Platform(randint(0, WIDTH), randint(0, HEIGHT), 80, 80)
plat12 = Platform(randint(0, WIDTH), randint(0, HEIGHT), 30, 30)
plat13 = Platform(randint(0, WIDTH), randint(0, HEIGHT), 20, 20)
plat14 = Platform(randint(0, WIDTH), randint(0, HEIGHT), 100, 100)
plat15 = Platform(randint(0, WIDTH), randint(0, HEIGHT), 75, 75)
plat16 = Platform(randint(0, WIDTH), randint(0, HEIGHT), 90, 90)
plat17 = Platform(randint(0, WIDTH), randint(0, HEIGHT), 10, 10)
plat18 = Platform(randint(0, WIDTH), randint(0, HEIGHT), 40, 40)
##### pobjects #####
pobject = Platform(randint(0, WIDTH), randint(0, HEIGHT), 20, 20)
pobject1 = Platform(randint(0, WIDTH), randint(0, HEIGHT), 20, 20)
##### boxes #####
box = Platform(randint(0, WIDTH), randint(0, HEIGHT), 90, 30)

# add player to all sprites group. I tried to find a more efficient method of accomplishing this.
all_sprites.add(player)
all_sprites.add(plat, plat1, plat2, plat3, plat4, plat5, plat6, plat7, plat8, plat9, plat10, plat11, plat12, plat13, plat14, plat15, plat16, plat17, plat18)
all_walls.add(plat, plat1, plat2, plat3, plat4, plat5, plat6, plat7, plat8, plat9, plat10, plat11, plat12, plat13, plat14, plat15, plat16, plat17, plat18)
all_pobjects.add(pobject, pobject1)
all_boxes.add(box)

timer_interval = 12000 # 12 seconds to complete the challenge
timer_event = pg.USEREVENT + 1
pg.time.set_timer(timer_event , timer_interval)

#Game loop
running = True
while running:
    #keep the loop running using clock
    clock.tick(FPS)

    for event in pg.event.get():
        #check for closed window
        if event.type == pg.QUIT:
            running = False
        if event.type == timer_event:
            #Feedback to user, stating facts and thanking them for playing my game!
            print("Timer done!")
            print("Thank you for playing my game!")
            player.kill()
        else: print("LETS GO! - ALMOST THERE!")
    
    ############ Update ##############
    # update all sprites
    all_sprites.update()

    ############ Draw ################
    # draw the background screen
    screen.fill(BLACK)
    # draw all sprites
    all_sprites.draw(screen)
    # buffer - after drawing everything, flip display
    pg.display.flip()

if timer_interval == 12000:
    pg.quit() #Quits PyGame