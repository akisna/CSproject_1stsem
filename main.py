from pickle import FALSE
import random # For generating random numbers
import sys # We will use sys.exit to exit the program
import pygame
from pygame.locals import * # Basic pygame imports

# Global Variables for the game
FPS = 32
LIFE=1
birdno=0
bgno=0
SCREENWIDTH = 289
SCREENHEIGHT = 511
SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
GROUNDY = SCREENHEIGHT * 0.8
GAME_SPRITES = {}
GAME_SOUNDS = {}
PLAYER = [ f'gallery/sprites/bird{i}.png' for i in range(1,4) ]
HEART = [ f'gallery/sprites/hearts{i}.png' for i in range(1,4) ]
background = [ f'gallery/sprites/background{i}.png' for i in range(1,4) ]
PIPE = [  f'gallery/sprites/pipe{i}.png' for i in range(1,4) ]
HS='gallery/sprites/highscore.png'
highscore=0
score=0
def selectlevel():
    global FPS
    levelx=int((SCREENWIDTH - GAME_SPRITES['level'].get_width())/2)
    levely=int((SCREENHEIGHT - GAME_SPRITES['level'].get_height())/2)
    nos=[K_1 , K_2 , K_3 , K_4,K_5 , K_6,K_7 , K_8,K_9 ]
    while True:
        for event in pygame.event.get():
            # if user clicks on cross button, close the game
            if event.type == QUIT or (event.type==KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            # If the user presses space or up key, start the game for them
            elif event.type==KEYDOWN and (event.key==K_SPACE or event.key == K_UP):
                return
            if event.type==KEYDOWN and event.key in nos:
                FPS=FPS-1
                FPS+=(nos.index(event.key) + 1)
                return  
            elif event.type==KEYDOWN and event.key in nos:
                FPS=FPS-1
                FPS+=(nos.index(event.key) + 1)
                return  
            else:
                SCREEN.blit(GAME_SPRITES['level'], (levelx,levely))
                pygame.display.update()    
                FPSCLOCK.tick(FPS)
    
def welcomeScreen():
    """
    Shows welcome images on the screen
    """
    global birdno
    playerx = int(SCREENWIDTH/5)
    playery = int((SCREENHEIGHT - GAME_SPRITES['player'][birdno].get_height())/2)
    messagex = int((SCREENWIDTH - GAME_SPRITES['message'].get_width())/2)
    messagey = int(SCREENHEIGHT*0.13)
    basex = 0
    while True:
        for event in pygame.event.get():
            # if user clicks on cross button, close the game
            if event.type == QUIT or (event.type==KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            # If the user presses space or up key, start the game for them
            elif event.type==KEYDOWN and (event.key==K_SPACE or event.key == K_UP):
                return
            else:
                SCREEN.blit(GAME_SPRITES['background'][bgno], (0, 0))    
                SCREEN.blit(GAME_SPRITES['player'][birdno], (playerx, playery))    
                SCREEN.blit(GAME_SPRITES['message'], (messagex,messagey ))    
                SCREEN.blit(GAME_SPRITES['base'][bgno], (basex, GROUNDY))    
                pygame.display.update()
                FPSCLOCK.tick(FPS)
def pickabird():
    """
    Shows welcome images on the screen
    """
    global birdno
    global LIFE
    playerx = int(SCREENWIDTH/2.2)
    playery = int((SCREENHEIGHT - GAME_SPRITES['player'][birdno].get_height())/2)
    avatarselectx = int((SCREENWIDTH - GAME_SPRITES['avatarselect'].get_width())/2)
    avatarselecty = int(SCREENHEIGHT*0.13)
    basex = 0
    LIFE = 1
    while True:
        for event in pygame.event.get():
            # if user clicks on cross button, close the game
            if event.type == QUIT or (event.type==KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            #changing birdno
            if event.type==KEYDOWN and event.key==K_RIGHT:
                birdno=(birdno+1)%3             
            if event.type==KEYDOWN and event.key==K_LEFT:
                birdno=(birdno-1)%3
            # If the user presses space or up key, start the game for them
            elif event.type==KEYDOWN and (event.key==K_SPACE or event.key == K_UP):
                return
            else:
                SCREEN.blit(GAME_SPRITES['background'][bgno], (0, 0))    
                SCREEN.blit(GAME_SPRITES['player'][birdno], (playerx, playery))    
                SCREEN.blit(GAME_SPRITES['avatarselect'], (avatarselectx,avatarselecty ))    
                #SCREEN.blit(GAME_SPRITES['base'], (basex, GROUNDY))    
                pygame.display.update()
                FPSCLOCK.tick(FPS)

def pickabg():
    """
    Shows welcome images on the screen
    """
    global bgno
    playerx = int(SCREENWIDTH/2.2)
    playery = int((SCREENHEIGHT - GAME_SPRITES['player'][birdno].get_height())/2)
    avatarselectx = int((SCREENWIDTH - GAME_SPRITES['avatarselect'].get_width())/2)
    avatarselecty = int(SCREENHEIGHT*0.13)
    basex = 0
    while True:
        for event in pygame.event.get():
            # if user clicks on cross button, close the game
            if event.type == QUIT or (event.type==KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            #changing birdno
            if event.type==KEYDOWN and event.key==K_RIGHT:
                bgno=(bgno+1)%3             
            if event.type==KEYDOWN and event.key==K_LEFT:
                bgno=(bgno-1)%3
            # If the user presses space or up key, start the game for them
            elif event.type==KEYDOWN and (event.key==K_SPACE or event.key == K_UP):
                return
            else:
                SCREEN.blit(GAME_SPRITES['background'][bgno], (0, 0))    
                #SCREEN.blit(GAME_SPRITES['player'][birdno], (playerx, playery))    
                SCREEN.blit(GAME_SPRITES['bgselect'], (avatarselectx,avatarselecty ))    
                #SCREEN.blit(GAME_SPRITES['base'], (basex, GROUNDY))    
                pygame.display.update()
                FPSCLOCK.tick(FPS)

def gameover():
    global birdno
    global highscore
    playerx = int(SCREENWIDTH/5)
    playery = int((SCREENHEIGHT - GAME_SPRITES['player'][birdno].get_height())/2)
    avatarselectx = int((SCREENWIDTH - GAME_SPRITES['hs'].get_width())/2)
    avatarselecty = int(SCREENHEIGHT*0.4)
    newx = int((SCREENWIDTH - GAME_SPRITES['new'].get_width())/2)
    basex = 0
    isithigh=False
    hsy=0.6
    if score>highscore:
        isithigh=True
        hsy=0.7
        highscore=score
    while True:
        for event in pygame.event.get():
            # if user clicks on cross button, close the game
            if event.type == QUIT or (event.type==KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            # If the user presses space or up key, start the game for them
            elif event.type==KEYDOWN and (event.key==K_SPACE):
                 # or event.key == K_UP):
                return
            else:
                SCREEN.blit(GAME_SPRITES['background'][bgno], (0, 0))    
               # SCREEN.blit(GAME_SPRITES['player'][birdno], (playerx, playery))
                if not isithigh:    
                 SCREEN.blit(GAME_SPRITES['hs'], (avatarselectx,avatarselecty ))
                else:     
                 SCREEN.blit(GAME_SPRITES['new'], (newx,SCREENHEIGHT*0.2 )) 
                myDigits = [int(x) for x in list(str(score))]
                width = 0

                
                for digit in myDigits:
                    width += GAME_SPRITES['numbers'][digit].get_width()
                    Xoffset = (SCREENWIDTH - width)/2

                for digit in myDigits:
                    if not highscore:
                        SCREEN.blit(GAME_SPRITES['numbers'][digit], (Xoffset, SCREENHEIGHT*0.12))
                    Xoffset += GAME_SPRITES['numbers'][digit].get_width()
                myDigitshs = [int(x) for x in list(str(highscore))]
                width = 0
                

                for digit in myDigitshs:
                    width += GAME_SPRITES['numbers'][digit].get_width()
                    Xoffset = (SCREENWIDTH - width)/2

                for digit in myDigitshs:
                    SCREEN.blit(GAME_SPRITES['numbers'][digit], (Xoffset, SCREENHEIGHT*hsy))
                    Xoffset += GAME_SPRITES['numbers'][digit].get_width()   
                pygame.display.update()
                FPSCLOCK.tick(FPS)
def mainGame(lastscore):
    global score
    global bgno
    global LIFE
    isheart = False
    if lastscore==0:
     isheart = True

    hearty=GAME_SPRITES['heart'].get_height()/2
    score = lastscore
    playerx = int(SCREENWIDTH/5)
    playery = int(SCREENWIDTH/2)
    basex = 0

    # Create 2 pipes for blitting on the screen
    newPipe1 = getRandomPipe()
    newPipe2 = getRandomPipe()

    # my List of upper pipes
    upperPipes = [
        {'x': SCREENWIDTH+200, 'y':newPipe1[0]['y']},
        {'x': SCREENWIDTH+200+(SCREENWIDTH/2), 'y':newPipe2[0]['y']},
    ]
    # my List of lower pipes
    lowerPipes = [
        {'x': SCREENWIDTH+200, 'y':newPipe1[1]['y']},
        {'x': SCREENWIDTH+200+(SCREENWIDTH/2), 'y':newPipe2[1]['y']},
    ]

    pipeVelX = -4

    playerVelY = -9
    playerMaxVelY = 10
    playerMinVelY = -8
    playerAccY = 1

    playerFlapAccv = -8 # velocity while flapping
    playerFlapped = False # It is true only when the bird is flapping


    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                if playery > 0:
                    playerVelY = playerFlapAccv
                    playerFlapped = True
                    GAME_SOUNDS['wing'].play()


        crashTest = isCollide(playerx, playery, upperPipes, lowerPipes) # This function will return true if the player is crashed
        
        if crashTest:
            LIFE=LIFE-1
            if LIFE==0:
             return
            mainGame(score)
            return   

        #check for score
        playerMidPos = playerx + GAME_SPRITES['player'][birdno].get_width()/2
        for pipe in upperPipes:
            pipeMidPos = pipe['x'] + GAME_SPRITES['pipe'][bgno][0].get_width()/2
            if pipeMidPos<= playerMidPos < pipeMidPos +4:
                score +=1
                #print(f"Your score is {score}") 
                GAME_SOUNDS['point'].play()


        if playerVelY <playerMaxVelY and not playerFlapped:
            playerVelY += playerAccY

        if playerFlapped:
            playerFlapped = False            
        playerHeight = GAME_SPRITES['player'][birdno].get_height()
        playery = playery + min(playerVelY, GROUNDY - playery - playerHeight)

        # move pipes to the left
        for upperPipe , lowerPipe in zip(upperPipes, lowerPipes):
            upperPipe['x'] += pipeVelX
            lowerPipe['x'] += pipeVelX

        # Add a new pipe when the first is about to cross the leftmost part of the screen
        if 0<upperPipes[0]['x']<5:
            newpipe = getRandomPipe()
            upperPipes.append(newpipe[0])
            lowerPipes.append(newpipe[1])

        # if the pipe is out of the screen, remove it
        if upperPipes[0]['x'] < -GAME_SPRITES['pipe'][bgno][0].get_width():
            upperPipes.pop(0)
            lowerPipes.pop(0)
        
        # Lets blit our sprites now
        SCREEN.blit(GAME_SPRITES['background'][bgno], (0, 0))
        for upperPipe, lowerPipe in zip(upperPipes, lowerPipes):
            SCREEN.blit(GAME_SPRITES['pipe'][bgno][0], (upperPipe['x'], upperPipe['y']))
            SCREEN.blit(GAME_SPRITES['pipe'][bgno][1], (lowerPipe['x'], lowerPipe['y']))
            #if score%9==0 and LIFE<3: 
             #   SCREEN.blit(GAME_SPRITES['heart'], (lowerPipe['x'], lowerPipe['y']-SCREENHEIGHT/6-hearty))

        SCREEN.blit(GAME_SPRITES['base'][bgno], (basex, GROUNDY))
        SCREEN.blit(GAME_SPRITES['life'][LIFE-1], (0,0)) #displays no of lifes left
        SCREEN.blit(GAME_SPRITES['player'][birdno], (playerx, playery))
        myDigits = [int(x) for x in list(str(score))]
        width = 0
        for digit in myDigits:
            width += GAME_SPRITES['numbers'][digit].get_width()
        Xoffset = (SCREENWIDTH - width)/2

        for digit in myDigits:
            SCREEN.blit(GAME_SPRITES['numbers'][digit], (Xoffset, SCREENHEIGHT*0.12))
            Xoffset += GAME_SPRITES['numbers'][digit].get_width()
        if score%10!=0:
            isheart = True
        if 0<LIFE<3 and isheart:
            if (score)%10==0 and score>1:
                LIFE+=1
                isheart=False
        
        pygame.display.update()
        FPSCLOCK.tick(FPS)

def isCollide(playerx, playery, upperPipes, lowerPipes):
    if playery> GROUNDY - 25  or playery<0:
        GAME_SOUNDS['hit'].play()
        return True
    
    for pipe in upperPipes:
        pipeHeight = GAME_SPRITES['pipe'][bgno][0].get_height()
        if(playery < pipeHeight + pipe['y'] and abs(playerx - pipe['x']) < (GAME_SPRITES['pipe'][bgno][0].get_width())/1.5):
            GAME_SOUNDS['hit'].play()
            return True

    for pipe in lowerPipes:
        if (playery + GAME_SPRITES['player'][birdno].get_height() > pipe['y']) and abs(playerx - pipe['x']) < (GAME_SPRITES['pipe'][bgno][0].get_width()/1.5):
            GAME_SOUNDS['hit'].play()
            return True

    return False

def getRandomPipe():
    """
    Generate positions of two pipes(one bottom straight and one top rotated ) for blitting on the screen
    """
    pipeHeight = GAME_SPRITES['pipe'][bgno][0].get_height()
    offset = SCREENHEIGHT/3
    y2 = offset + random.randrange(0, int(SCREENHEIGHT - GAME_SPRITES['base'][bgno].get_height()  - 1.2 *offset))
    pipeX = SCREENWIDTH + 10
    y1 = pipeHeight - y2 + offset
    pipe = [
        {'x': pipeX, 'y': -y1}, #upper Pipe
        {'x': pipeX, 'y': y2} #lower Pipe
    ]
    return pipe






if __name__ == "__main__":
    # This will be the main point from where our game will start
    pygame.init() # Initialize all pygame's modules
    FPSCLOCK = pygame.time.Clock()
    pygame.display.set_caption('Flappy Bird Plus')
    GAME_SPRITES['numbers'] = ( 
        pygame.image.load('gallery/sprites/0.png').convert_alpha(),
        pygame.image.load('gallery/sprites/1.png').convert_alpha(),
        pygame.image.load('gallery/sprites/2.png').convert_alpha(),
        pygame.image.load('gallery/sprites/3.png').convert_alpha(),
        pygame.image.load('gallery/sprites/4.png').convert_alpha(),
        pygame.image.load('gallery/sprites/5.png').convert_alpha(),
        pygame.image.load('gallery/sprites/6.png').convert_alpha(),
        pygame.image.load('gallery/sprites/7.png').convert_alpha(),
        pygame.image.load('gallery/sprites/8.png').convert_alpha(),
        pygame.image.load('gallery/sprites/9.png').convert_alpha(),
    )
    GAME_SPRITES['message'] =pygame.image.load('gallery/sprites/message.png').convert_alpha()
    GAME_SPRITES['avatarselect'] =pygame.image.load('gallery/sprites/avatarselect.png').convert_alpha()
    GAME_SPRITES['bgselect'] =pygame.image.load('gallery/sprites/bgselect.png').convert_alpha()
    GAME_SPRITES['hs'] =pygame.image.load(HS).convert_alpha()
    GAME_SPRITES['level'] =pygame.image.load('gallery/sprites/level.png').convert_alpha()
    GAME_SPRITES['heart'] =pygame.image.load('gallery/sprites/heart.png').convert_alpha()
    GAME_SPRITES['new'] =pygame.image.load('gallery/sprites/new.png').convert_alpha()
    GAME_SPRITES['base'] =[ pygame.image.load(f'gallery/sprites/base{i}.png').convert_alpha() for i in range(1,4) ]
    GAME_SPRITES['pipe'] =[(pygame.transform.rotate(pygame.image.load(PIPE[i]).convert_alpha(), 180), 
    pygame.image.load(PIPE[i]).convert_alpha()) for i in range(3) ]

    # Game sounds
    GAME_SOUNDS['die'] = pygame.mixer.Sound('gallery/audio/die.mp3')
    GAME_SOUNDS['hit'] = pygame.mixer.Sound('gallery/audio/hit.mp3')
    GAME_SOUNDS['point'] = pygame.mixer.Sound('gallery/audio/point.mp3')
    GAME_SOUNDS['swoosh'] = pygame.mixer.Sound('gallery/audio/swoosh.mp3')
    GAME_SOUNDS['wing'] = pygame.mixer.Sound('gallery/audio/wing.mp3')

    GAME_SPRITES['background'] = [ pygame.image.load(background[i]).convert() for i in range(3) ]
    GAME_SPRITES['player'] = [ pygame.image.load(PLAYER[i]).convert_alpha() for i in range(3) ]
    GAME_SPRITES['life'] = [ pygame.image.load(HEART[i]).convert_alpha() for i in range(3) ]

    selectlevel()

    while True:
        welcomeScreen() # Shows welcome screen to the user until he presses a button
        pickabird()
        pickabg()
        mainGame(8) # This is the main game function
        gameover() 