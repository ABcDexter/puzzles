########################
# imports
########################

import pygame, sys  # random
from pygame.locals import *
pygame.init()

########################
# intialising variables
########################
window_height = 600
window_width = 1200

blue = (0, 0, 255)
black = (0, 0, 0)
white = (255, 255, 255)

fps = 25  # this should not be set higher than 42, otherwise game speed and sensitivty increases
level = 0  # this tells the startting level
addnewflamerate = 20  # higher the value, slower the flame throwing rate

########################
# Classes
########################


class Dragon:
    """
    This class created a Dragon, and varies the dragon accordingly

    """

    global firerect, imagerect, Canvas
    up = False
    down = True
    velocity = 15  # 15 is the ideal speed for Dragon
    
    def __init__(self):
        self.image = load_image('dragon.png')
        self.imagerect = self.image.get_rect()
        self.imagerect.right = window_width
        self.imagerect.top = window_height//2

    def update(self):
        """
        alter the Dragon direction accordingly
        :return:
        """
        if self.imagerect.top < cactusrect.bottom:
            self.up = False
            self.down = True

        if self.imagerect.bottom > firerect.top:
            self.up = True
            self.down = False
            
        if self.down:
            self.imagerect.bottom += self.velocity

        if self.up:
            self.imagerect.top -= self.velocity

        Canvas.blit(self.image, self.imagerect)

    def return_height(self):
        """
        return hwo far the Dragon is from top
        :return:
        """
        h = self.imagerect.top
        return h


class Flames:
    """
    This is the Flames class, if Maryo touches this, he dies.
    """
    flamespeed = 20

    def __init__(self):
        self.image = load_image('fireball.png')
        self.imagerect = self.image.get_rect()
        self.height = Dragon.return_height() + 20
        self.surface = pygame.transform.scale(self.image, (20, 20))
        self.imagerect = pygame.Rect(window_width - 106, self.height, 20, 20)

    def update(self):
        self.imagerect.left -= self.flamespeed

    def collision(self):
        """
        detect collision with others
        :return:
        """
        if self.imagerect.left == 0:
            return True
        else:
            return False


class Maryo:
    """
    This is the Maryo class.
    """
    global moveup, movedown, gravity, cactusrect, firerect
    speed = 10  # 10 is th ideal speed for optimal gameplay
    downspeed = 20  # 20 is the gravity, perfect for optimal experience

    def __init__(self):
        self.image = load_image('maryo.png')
        self.imagerect = self.image.get_rect()
        self.imagerect.topleft = (50,window_height//2)
        self.score = 0

    def update(self):
        
        if moveup and (self.imagerect.top > cactusrect.bottom):
            self.imagerect.top -= self.speed
            self.score += 1
            
        if movedown and (self.imagerect.bottom < firerect.top):
            self.imagerect.bottom += self.downspeed
            self.score += 1
            
        if gravity and (self.imagerect.bottom < firerect.top):
            self.imagerect.bottom += self.speed


########################
# functions
########################

def terminate():
    """
    To end the program
    :return:
    """
    pygame.quit()
    sys.exit()


def waitforkey():
    """
    To wait for user to start
    if the user presses the escape key,
        terminate()
    :return:
    """
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    terminate()
                return
            

def flamehitsmario(playerrect, flames):
    """
    to check if flame has hit mario or not

    :param playerrect:
    :param flames:
    :return:
    """
    for f in flame_list:
        if playerrect.colliderect(f.imagerect):
            return True
        return False


def drawtext(text, font, surface, x, y):
    """
    to display text on the screen

    :param text:
    :param font:
    :param surface:
    :param x:
    :param y:
    :return:
    """
    textobj = font.render(text, 1, white)
    textrect = textobj.get_rect()
    textrect.topleft = (int(x), int(y))
    surface.blit(textobj, textrect)


def check_level(score):
    """

    :param score:
    :return:
    """
    global window_height, level, cactusrect, firerect
    if score in range(0, 250):
        firerect.top = window_height - 50
        cactusrect.bottom = 50
        level = 1
    elif score in range(250, 500):
        firerect.top = window_height - 100
        cactusrect.bottom = 100
        level = 2
    elif score in range(500, 750):
        level = 3
        firerect.top = window_height-150
        cactusrect.bottom = 150
    elif score in range(750, 1000):
        level = 4
        firerect.top = window_height - 200
        cactusrect.bottom = 200


def load_image(imagename):
    """
    :param imagename:
    :return:
    """
    return pygame.image.load(imagename)

    
#########################
# initialiser
##########################

mainClock = pygame.time.Clock()
Canvas = pygame.display.set_mode((window_width,window_height))
pygame.display.set_caption('MARYO')

#########################################
# setting up font and sounds and images
#########################################
font = pygame.font.SysFont(None, 48)
scorefont = pygame.font.SysFont(None, 30)

fireimage = load_image('fire_bricks.png')
firerect = fireimage.get_rect()

cactusimage = load_image('cactus_bricks.png')
cactusrect = cactusimage.get_rect()

startimage = load_image('start.png')
startimagerect = startimage.get_rect()
startimagerect.centerx = window_width//2
startimagerect.centery = window_height//2

endimage = load_image('end.png')
endimagerect = startimage.get_rect()
endimagerect.centerx = window_width//2
endimagerect.centery = window_height//2

pygame.mixer.music.load('mario_theme.wav')
gameover = pygame.mixer.Sound('mario_dies.wav')

#############################
# getting to the start screen
##############################
drawtext('Mario', font, Canvas, (window_width/3), (window_height/3))
Canvas.blit(startimage, startimagerect)

pygame.display.update()
waitforkey()

#########################
# start for the main code
#########################

topscore = 0
Dragon = Dragon()

while True:
    flame_list = []
    player = Maryo()
    moveup = movedown = gravity = False
    flameaddcounter = 0

    gameover.stop()
    pygame.mixer.music.play(-1, 0.0)

    while True:
        #  the main game loop

        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()

            if event.type == KEYDOWN:
                
                if event.key == K_UP:
                    movedown = False
                    moveup = True
                    gravity = False

                if event.key == K_DOWN:
                    movedown = True
                    moveup = False
                    gravity = False

            if event.type == KEYUP:

                if event.key == K_UP:
                    moveup = False
                    gravity = True
                if event.key == K_DOWN:
                    movedown = False
                    gravity = True
                    
                if event.key == K_ESCAPE:
                    terminate()

        flameaddcounter += 1
        check_level(player.score)
        
        if flameaddcounter == addnewflamerate:

            flameaddcounter = 0
            newflame = Flames()
            flame_list.append(newflame)

        for f in flame_list:
            Flames.update(f)

        for f in flame_list:
            if f.imagerect.left <= 0:
                flame_list.remove(f)

        player.update()
        Dragon.update()

        Canvas.fill(black)
        Canvas.blit(fireimage, firerect)
        Canvas.blit(cactusimage, cactusrect)
        Canvas.blit(player.image, player.imagerect)
        Canvas.blit(Dragon.image, Dragon.imagerect)

        # write the score on the top of the screen
        drawtext('Score : %s | Top score : %s | Level : %s' %(player.score, topscore, level), scorefont, Canvas, 350, cactusrect.bottom + 10)
        
        for f in flame_list:
            Canvas.blit(f.surface, f.imagerect)

        if flamehitsmario(player.imagerect, flame_list):
            if player.score > topscore:
                topscore = player.score
            break
        
        if (player.imagerect.top <= cactusrect.bottom) or (player.imagerect.bottom >= firerect.top):
            if player.score > topscore:
                topscore = player.score
            break

        pygame.display.update()

        mainClock.tick(fps)
    
    pygame.mixer.music.stop()
    gameover.play()
    Canvas.blit(endimage, endimagerect)
    pygame.display.update()
    waitforkey()
#########################
# End of code
#########################
