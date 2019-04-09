#----->my first game<-----#
#----->SNAKE_GAME<-----#

#----->language -Pyhton<------#
#----->modules used-> *pygame*, *random*, *sys*, *time* <------#

#----->By-Yashi Kesarwani<-----#
#-----> yashikesarwani092@gmail.com<-----#

import pygame
import time
import sys
import random

pygame.init()
clock = pygame.time.Clock()

#------------->constant declarations<-------------#

white = (255, 255, 255)
blue = (23, 32, 42)
black = (0,0,0)
red = (255,0,0)
green = (0, 155, 0)

background_width = 800
background_height = 600
unit_block_size = 10
frames_per_second = 15
points = 0

#---------------------->font declaration<-------------------------------------------------#

font = pygame.font.SysFont(None, 25)

#----------------->defining snake structure------------------------------#

def snake_structure(unit_block_size, snake_list):
    for element_x_y in (snake_list):
         pygame.draw.rect(gameDisplay,white,[element_x_y[0], element_x_y[1], unit_block_size ,unit_block_size])
         
#----------------->calculating total points at any stage of the game<-------------------#
         
def calculate_points():
    font = pygame.font.SysFont(None , 25)
    text = font.render("Points: " + str(points), True, white)
    gameDisplay.blit(text, (unit_block_size, unit_block_size))                 

#------------------>a message given to the user on the screen<-----------------------------#
    
def note_to_user(msg,color):
    on_screen_note = font.render(msg, True, color)
    gameDisplay.blit(on_screen_note,[background_width/6, background_height/2])

#--------------------->display and caption of the game<---------------------------------------#    

gameDisplay=pygame.display.set_mode((background_width,background_height)) 
pygame.display.set_caption('my_first_game_SNAKE_GAME')

#----------------------->defining main game loop of the code<------------------------------------#

def gameLoop():
    
#-------------------------------->terms declaration inside the main gameloop<---------------------------------------#
    
    start_x = background_width/2
    start_y = background_height/2
    start_x_change = 0
    start_y_change = 0

    snake_list = []
    snake_length = 1
    global points

    gameExit = False
    gameOver = False

    randomTarget_x = round(random.randrange(0, background_width - unit_block_size)/10.0)*10.0
    randomTarget_y = round(random.randrange(0, background_height - unit_block_size)/10.0)*10.0

#------------------------------------------------------------------------------------------------------------------------------#    
    
    while not gameExit:
        
#------------------------>setting the gameover screen<-----------------------------------------------------------------#
        
        while gameOver == True:
            gameDisplay.fill(red)
            note_to_user("you are done...game over!! Want to play again-Click C or Want to quit-Click Q!!",blue)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameExit = True
                    gameOver = False
                    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame. K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        gameLoop()
                    
            
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
                
#------------------------>making the snake move in continuous way along diferent directions<----------------------------#
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    start_x_change =- unit_block_size
                    start_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    start_x_change = unit_block_size
                    start_y_change = 0
                
                elif event.key == pygame.K_UP:
                    start_y_change =- unit_block_size
                    start_x_change = 0
                elif event.key == pygame.K_DOWN:
                    start_y_change = unit_block_size
                    start_x_change = 0        
       
        start_x += start_x_change
        start_y += start_y_change
        
#------------------------------->setting background and target colour<-----------------------------------------------#
        
        gameDisplay.fill(blue)
        pygame.draw.rect(gameDisplay , red , [randomTarget_x, randomTarget_y, unit_block_size, unit_block_size])

#----------------------------------------------------------------------------------------------------------------------------------#

        snake_head = []
        snake_head.append(start_x)
        snake_head.append(start_y)
        snake_list.append(snake_head)

        if len(snake_list) > snake_length:
            del snake_list[0]
            
#------------------------------->checking the gameover and loosing conditions of the game<-------------------------------------------#      
        for any_section in snake_list[:-1]:
            if any_section == snake_head:
                gameOver = True
                points = 0
                
        if start_x >= background_width or start_x < 0 or start_y >= background_height or start_y < 0:
            gameOver = True
            points = 0       

#----------------------------------------------------------------------------------------------------------------------------------------#
            
        snake_structure(unit_block_size, snake_list)  
        calculate_points()
         
        pygame.display.update()
        
#--------------------->checking whether the target is achieved<----------------------------------------------------#
        
        if start_x == randomTarget_x and start_y == randomTarget_y:
            randomTarget_x = round(random.randrange(0, background_width - unit_block_size)/10.0)*10.0
            randomTarget_y = round(random.randrange(0, background_height - unit_block_size)/10.0)*10.0
            snake_length += 1
            points += 1 
#-------------------------------------------------------------------------------------------------------------------------------#
            
        clock.tick(frames_per_second)
        
    note_to_user("you lose...this is done...!!",red)
    time.sleep(1)
    pygame.display.update()
    pygame.quit()
    quit()

gameLoop()
    
