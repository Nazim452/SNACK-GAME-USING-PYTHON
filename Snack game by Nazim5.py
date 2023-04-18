import pygame
import random
import os

'''pygame.mixer.init()
pygame.mixer.music.load("bac.mp3")
pygame.mixer.music.play()'''


pygame.init()

#color

white = (255,255,255)
red= (255,0,0)
black= (0,0,0,)
screen_width = 900
screen_height = 600

#crerting window


gameWindow = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Game by Nazim")
pygame.display.update


clock = pygame.time.Clock()
font = pygame.font.SysFont(None,55)




def text_screen(text, color, x,  y):
    screen_text = font.render(text , True,color)          #antialiase
    gameWindow.blit(screen_text, [x,y])                  #blit - update screen

def plot_snake(gameWindow, color, snk_list, snake_size):
    print(snk_list)
    for x,y in snk_list:
         pygame.draw.rect(gameWindow, color , [x,y,  snake_size, snake_size])

def welcome():
    exit_game = False
    while not exit_game:
        gameWindow.fill((233,210,229))       #any random value for grtting colour      0 - means black ,   more value maeans -  more white
        text_screen("Snakes game develop by NAZIM", black, 160,250)
        text_screen("Press space bar for Play", black , 230,290)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                   gameLoop()



        pygame.display.update()
        clock.tick(60)
                   
# game loop
def gameLoop():
    #game specific variable
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
   
    velocity_x = 0
    velocity_y = 0
    
    snk_list = []
    snk_length= 1
    if (not os.path.exists("hisore.txt")):
        with open ("hiscore.txt" , "w") as f:
            f.write("0")
    
    with open ("hiscore.txt", "r") as f:
        hiscore = f.read()





    food_x = random.randint(10,screen_width/2)
    food_y= random.randint(10, screen_height/2)
    Score= 0
    init_velocity= 5
    snake_size= 30
    fps = 40


    
    while not exit_game:
        if game_over:
              with open ("hiscore.txt", "w") as f:
                f.write(str(hiscore))
              gameWindow.fill(white)
              text_screen("Game over! press Enter to continue", red , 100,300)
              text_screen("Game developer:- NAZIM KHAN", black,50,100 )
              for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game= True
                
                if event.type== pygame.KEYDOWN:
                    if event.key== pygame.K_RETURN:
                        gameLoop()

        else:
            


            for event in pygame.event.get():
           
                if event.type == pygame.QUIT:
                    exit_game= True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                         velocity_x =init_velocity 

                    velocity_y= 0 

                    if event.key == pygame.K_LEFT:
                        velocity_x= -init_velocity
                        velocity_y=0

                    if event.key == pygame.K_UP:
                        velocity_y= -init_velocity
                        velocity_x= 0
                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x=0

                  #  if event.key == pygame.K_q:
                  #     score+= 10
                 
            snake_x=snake_x+velocity_x
            snake_y=snake_y+velocity_y
            if abs(snake_x - food_x )<15 and abs (snake_y - food_y)<15:
                Score+= 10
                if Score>int(hiscore):
                    hiscore= Score
            #print("Score:" , Score*10)
        
                food_x = random.randint(10,screen_width/2)
                food_y= random.randint(10, screen_height/2)
                snk_length+=5








            gameWindow.fill(white)
            text_screen("Score:" + str(Score)+ "    hiscore:"+ str(hiscore),red , 5,5 )
            text_screen("Game developer:- NAZIM  KHAN", black, 20,500)
            pygame.draw.rect(gameWindow, red, [food_x, food_y ,snake_size, snake_size])



            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)
            if len(snk_list)>snk_length:
               del snk_list[0]
            
            if head in snk_list [ :-1]:
                game_over= True
            
            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y> screen_height:
                game_over=True
                
    

    #pygame.draw.rect(gameWindow, red, [food_x,food_y,  snake_size, snake_size])

            plot_snake(gameWindow, black , snk_list , snake_size)
   # pygame.draw.rect(gameWindow, red, [snake_x, snake_y , snake_size, snake_size])
        pygame.display.update()
        clock.tick(fps)











    pygame.quit()
    quit

welcome()