
####Alex Pham - Snake Game MyVersion 2018.
####This game makes use to the PyGame package in Python and uses the Arrow keys to control the snake.
####This version of the snake game was modified from the tutorial posted by Syntec (on behalf of TheNewBoston.com)
####All modifications and changes were made by Kevin Lam and Alex Pham.

import pygame
import time
import random

pygame.init()

global difficulty #added global difficulty
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,155,0)
blue = (64,4,204)   #added blue
orange = (255,127,80)  #added orange

display_width = 800
display_height  = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Meow')   #changed caption
   
icon = pygame.image.load('tom.png')  #changed icon
pygame.display.set_icon(icon)

img = pygame.image.load('tom.png')   #changed to tom's head
appleimg = pygame.image.load('jerry.png')  #changed to a jerry mouse

clock = pygame.time.Clock()

AppleThickness = 30
block_size = 20
FPS = 25  #changed the fps

direction = "right"

smallfont = pygame.font.SysFont("Helvetica", 25)  #changed the fonts
medfont = pygame.font.SysFont("Helvetica", 50)
largefont = pygame.font.SysFont("Helvetica", 80)


def pause():

    paused = True
    message_to_screen("Paused",
                      black,
                      -100,
                      size="large")

    message_to_screen("Press C to continue or Q to quit.",
                      black,
                      25)
    pygame.display.update()

    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False

                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()

        #gameDisplay.fill(white)
        
        clock.tick(5)
                    

def score(score):
    text = smallfont.render("Score: "+str(score), True, black)
    gameDisplay.blit(text, [0,0])

def randAppleGen():
    randAppleX = round(random.randrange(0, display_width-AppleThickness))#/10.0)*10.0
    randAppleY = round(random.randrange(0, display_height-AppleThickness))#/10.0)*10.0

    return randAppleX,randAppleY


def game_intro():
    difficulty = 0
    intro = True

    while intro:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                #if event.key == pygame.K_c:
                    #intro = False
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
                if event.key == pygame.K_1:
                    gameLoop(10)
                    intro = False
                if event.key == pygame.K_2:
                    gameLoop(20)
                    intro = False
                if event.key == pygame.K_3:
                    gameLoop(30)
                    intro = False
 #changed the screen messages
 #made the intro orange background
        gameDisplay.fill(white)
        message_to_screen("Welcome to Tom and Jerry",
                          green,
                          -100,
                          "large")
        message_to_screen("The objective of the game is to eat that Jerry",
                          black,
                          -30)

        message_to_screen("The more Jerries you eat, the more of you there are",
                          black,
                          10)

        message_to_screen("If you run into yourself, or the edges, you die!",
                          black,
                          50)

        message_to_screen("Press P to pause or Q to quit.",
                          black,
                          180)
#added a difficulty choice
        message_to_screen("Pick a Difficulty by pressing 1 for easy, 2 for medium, and 3 for hard",
                      black,
                      220,
                      "small")    
        pygame.display.update()
        clock.tick(difficulty)      #the game will run as fast as you choose
        return difficulty           #return difficulty value
        


def snake(block_size, snakelist):

    if direction == "right":
        head = pygame.transform.rotate(img, 270)

    if direction == "left":
        head = pygame.transform.rotate(img, 90)

    if direction == "up":
        head = img

    if direction == "down":
        head = pygame.transform.rotate(img, 180)
        
    
    gameDisplay.blit(head, (snakelist[-1][0], snakelist[-1][1]))


#changed the color rectangle added when eating jerry
    for XnY in snakelist[:-1]:
        pygame.draw.rect(gameDisplay, blue, [XnY[0],XnY[1],block_size,block_size])

def text_objects(text,color,size):
    if size == "small":
        textSurface = smallfont.render(text, True, color)
    elif size == "medium":
        textSurface = medfont.render(text, True, color)
    elif size == "large":
        textSurface = largefont.render(text, True, color)

    
    return textSurface, textSurface.get_rect()
    
    
def message_to_screen(msg,color, y_displace=0, size = "small"):
    textSurf, textRect = text_objects(msg,color, size)
    textRect.center = (display_width / 2), (display_height / 2)+y_displace
    gameDisplay.blit(textSurf, textRect)


def gameLoop(difficulty):
    global direction
    
    direction = 'right'
    gameExit = False
    gameOver = False

    lead_x = display_width/2
    lead_y = display_height/2

    lead_x_change = 10
    lead_y_change = 0

    snakeList = []
    snakeLength = 1

    randAppleX,randAppleY = randAppleGen()
    
    while not gameExit:

        if gameOver == True:
            message_to_screen("Game over",
                              red,
                              y_displace=-50,
                              size="large")
            
            message_to_screen("Press C to play again or Q to quit",
                              black,
                              50,
                              size="medium")
            pygame.display.update()
            

        while gameOver == True:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver = False
                    gameExit = True
                    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        gameLoop(difficulty)        #makes the game with the difficulty player chooses

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    direction = "left"
                    lead_x_change = -block_size
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    direction = "right"
                    lead_x_change = block_size
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    direction = "up"
                    lead_y_change = -block_size
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    direction = "down"
                    lead_y_change = block_size
                    lead_x_change = 0

                elif event.key == pygame.K_p:
                    pause()

        if lead_x >= display_width or lead_x < 0 or lead_y >= display_height or lead_y < 0:
            gameOver = True
      

        lead_x += lead_x_change
        lead_y += lead_y_change
        
        gameDisplay.fill(white)#ingame background orange

        
        #pygame.draw.rect(gameDisplay, red, [randAppleX, randAppleY, AppleThickness, AppleThickness])

        gameDisplay.blit(appleimg, (randAppleX, randAppleY))


        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)

        if len(snakeList) > snakeLength:
            del snakeList[0]

        for eachSegment in snakeList[:-1]:
            if eachSegment == snakeHead:
                gameOver = True

        
        snake(block_size, snakeList)

        score(snakeLength-1)

        
        pygame.display.update()

        if lead_x > randAppleX and lead_x < randAppleX + AppleThickness or lead_x + block_size > randAppleX and lead_x + block_size < randAppleX + AppleThickness:

            if lead_y > randAppleY and lead_y < randAppleY + AppleThickness:

                randAppleX,randAppleY = randAppleGen()
                snakeLength += 1

            elif lead_y + block_size > randAppleY and lead_y + block_size < randAppleY + AppleThickness:

                randAppleX,randAppleY = randAppleGen()
                snakeLength += 1

            
            

        
            
        
        
        
        clock.tick(difficulty)
        
    pygame.quit()
    quit()



#player chooses difficulty    
difficulty = 0
intro = True

while intro:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.KEYDOWN:
            #if event.key == pygame.K_c:
                #intro = False
            if event.key == pygame.K_q:
                pygame.quit()
                quit()
            if event.key == pygame.K_1: #different difficulty levels
                difficulty = 10
                intro = False
            if event.key == pygame.K_2:
                difficulty = 20
                intro = False
            if event.key == pygame.K_3:
                difficulty = 30
                intro = False
#changed the screen messages

    gameDisplay.fill(white)
    message_to_screen("Welcome to Tom and Cat",
                      green,
                      -100,
                      "large")
    message_to_screen("The objective of the game is to eat that Jerry",
                      black,
                      -30)

    message_to_screen("The more Jerries you eat, the more of you there are",
                      black,
                      10)

    message_to_screen("If you run into yourself, or the edges, you die!",
                      black,
                      50)

    message_to_screen("Press P to pause or Q to quit.",
                      black,
                      180)
    message_to_screen("Pick a Difficulty by pressing 1 for easy, 2 for medium, and 3 for hard",
                  black,
                  220,
                  "small")    
    pygame.display.update()
    clock.tick(difficulty)
       

gameLoop(difficulty)
