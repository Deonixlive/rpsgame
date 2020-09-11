#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pygame
from pygame.locals import *
import game

global aiwins,ties,playerwins
R = True
S = True
P = True
global pos1image
outcome = 0
aimove = None

#loading images of game results
tieimg = pygame.image.load("assets/tie.png")
aiwinimg = pygame.image.load("assets/aiwin.png")
playerwinimg = pygame.image.load("assets/playerwin.png")

#loading images of game states and adjusting size
paperimg = pygame.image.load("assets/Paper.png")
rockimg = pygame.image.load("assets/Rock.png")
scissorimg = pygame.image.load("assets/Scissor.png")
#default pic for pos1
pos1image = rockimg

size = (800,450)
grid = (100,100)

#with 1 being Rock, 2 Paper and 3 Scissor
pos1is = 0

def r(num):
    return round(num)
def relatg(xbox,ybox):
    return((xbox/grid[0]*size[0],ybox/grid[1]*size[1]))

#size which is depended on the position
sizeside = (29,3,29.3)
sizemiddle = (25,20)


#function to adjust size according to screen und values given
def adjust_size(image,scale):
    unround = relatg(scale[0],scale[1])
    return pygame.transform.scale(image, (r(unround[0]),r(unround[0])))
  

#Loading images of ki(v)w(y)is
#kiwi = pygame.image.load("assets/kiwi.gif")



    
ai = game.Selector(7,5)
    
aiwins = 0
ties = 0
playerwins = 0
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
orange = (230, 146, 11)    
    
pygame.init()   
size = (1600,900)
grid = (100,100)


def rockpress():
    global pos1is
    screen.blit(adjust_size(rockimg,sizeside), relatg(pos1[0],pos1[1])) 
    pos1is = 1
    gameround("R")
def paperpress():
    global pos1is
    screen.blit(adjust_size(paperimg,sizeside), relatg(pos1[0],pos1[1]))
    pos1is = 2
    gameround("P")
def scissorpress():
    global pos1is
    screen.blit(adjust_size(scissorimg,sizeside), relatg(pos1[0],pos1[1]))
    pos1is = 3
    gameround("S")
    
    


#pos of buttons
paperbuttonsize = relatg(23.3,10)
rockbuttonsize = relatg(23.3,10)
scissorbuttonsize = relatg(23.3,10)
rockbuttonpos = relatg(10,85)
paperbuttonpos = relatg(38.3,85)
scissorbuttonpos = relatg(66.3,85)


#getting pos of stats
playerwins_pos=relatg(15,5)
ties_pos = relatg(49,5)
aiwins_pos = relatg(77,5)
    
#pos of pictures
pos1 = (5,20)
pos2 = (37.3,25)
pos3 = (66.6,20)
def gameround(playermove):
    global aiwins,playerwins,ties,outcome,aimove
    aimove = ai.turn()
    ai.update(playermove)
    outcome = int(game.winner(playermove,aimove))
    if outcome == 1:
        aiwins += 1
        
    elif outcome == 2:
        playerwins += 1
    elif outcome == 3:
        ties += 1
def text_objects(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.SysFont('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((size[0]/2),(size[1]/2))
    screen.blit(TextSurf, TextRect)
    

    pygame.display.update()
    
def text_to_screen(screen, text, x, y, size = 20,
            color = white, font_type = 'comicsansms'):

    text = str(text)
    font = pygame.font.SysFont(font_type, size)
    text = font.render(text, True, color)
    screen.blit(text, (x, y))


    
    
def button(msg,x,y,w,h,ic,ac,action=None):
    x = r(x)
    y = r(y)
    w = r(w)
    h = r(h)
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    pygame.draw.rect(screen, ic,(x,y,w,h))
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(screen, ac,(x,y,w,h))

        if click[0] == 1 and (action != None):
            pygame.draw.rect(screen, white,(x,y,w,h))
            action()         
    #else:
     #   pygame.draw.rect(screen, ic,(x,y,w,h))

    smallText = pygame.font.SysFont("comicsansms",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( r((x+(w/2))), (r(y+(h/2))))
    screen.blit(textSurf, textRect)
    
def game_loop():
    gameExit = False
    
def drawpos1():
    if int(pos1is) == 1:
        screen.blit(adjust_size(rockimg,sizeside), relatg(pos1[0],pos1[1]))

    elif pos1is == 2:
        screen.blit(adjust_size(paperimg,sizeside), relatg(pos1[0],pos1[1]))
    elif pos1is == 3:
        screen.blit(adjust_size(scissorimg,sizeside), relatg(pos1[0],pos1[1]))
    else:
        pass

def drawpos2():
    if outcome == 1:
        screen.blit(adjust_size(aiwinimg,sizemiddle), relatg(pos2[0],pos2[1]))
    elif outcome == 2:
        screen.blit(adjust_size(playerwinimg,sizemiddle), relatg(pos2[0],pos2[1]))
    elif outcome == 3:
        screen.blit(adjust_size(tieimg,sizemiddle), relatg(pos2[0],pos2[1]))
    
def drawpos3():
    if aimove == "R":
        screen.blit(adjust_size(rockimg,sizeside), relatg(pos3[0],pos3[1])) 
    elif aimove == "P":
        screen.blit(adjust_size(paperimg,sizeside), relatg(pos3[0],pos3[1])) 
    elif aimove == "S":
        screen.blit(adjust_size(scissorimg,sizeside), relatg(pos3[0],pos3[1]))        
# PyGame template.
 
# Import standard modules.
import sys
 
# Import non-standard modules.

def update(dt):

  # Go through events that are passed to the script by the window.
    for event in pygame.event.get():
    # We need to handle these events. Initially the only one you'll want to care
    # about is the QUIT event, because if you don't handle it, your game will crash
    # whenever someone tries to exit.
        if event.type == QUIT:
            pygame.quit() # Opposite of pygame.init
            sys.exit() # Not including this line crashes the script on Windows. Possibly
      # on other operating systems too, but I don't know for sure.
    # Handle other events as you wish.
def draw(screen):
    screen.fill((0, 0, 0)) # Fill the screen with black.
    
    button("Rock",rockbuttonpos[0],rockbuttonpos[1],rockbuttonsize[0],rockbuttonsize[1],red,orange,rockpress)    
    button("Paper",paperbuttonpos[0],paperbuttonpos[1],paperbuttonsize[0],paperbuttonsize[1],red,orange,paperpress)    

    button("Scissor",scissorbuttonpos[0],scissorbuttonpos[1],scissorbuttonsize[0],scissorbuttonsize[1],red,orange,scissorpress)
    
    text_to_screen(screen,f"Player wins: {playerwins}", playerwins_pos[0],playerwins_pos[1])
    text_to_screen(screen,f"Ties: {ties}", ties_pos[0],ties_pos[1])
    text_to_screen(screen,f"AI wins: {aiwins}", aiwins_pos[0],aiwins_pos[1])

    drawpos1()
    drawpos2()
    drawpos3()
    pygame.display.flip()
   # screen.blit(rockimg, (x,y))
    
  # Redraw screen here.
  
  # Flip the display so that the things we drew actually show up.

def runPyGame():
    global screen,fps

    
    pygame.init()
    screen = pygame.display.set_mode((size[0], size[1]), pygame.FULLSCREEN)#pygame.FULLSCREEN
  # Set up the clock. This will tick every frame and thus maintain a relatively constant framerate. Hopefully.
    fps = 10
    fpsClock = pygame.time.Clock()
  
  # Set up the window.



  
  # screen is the surface representing the window.
  # PyGame surfaces can be thought of as screen sections that you can draw onto.
  # You can also draw surfaces onto other surfaces, rotate surfaces, and transform surfaces.
  
  # Main game loop.
    dt = 1/fps # dt is the time since last frame.

    while True: # Loop forever!

        

        update(dt) # You can update/draw here, I've just moved the code for neatness.
        draw(screen)
        
        
        
   
        dt = fpsClock.tick(fps)
    
    
        
     


# In[2]:


runPyGame()
  


# In[ ]:




