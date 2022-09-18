import pygame
from paddle import Paddle
pygame.init()

black = (0,0,0)
white = (255,255,255)

#open a window
size = (700, 500)
screen =  pygame.display.set_mode(size)
pygame.display.set_caption("Pong")

#left side paddle
paddle_a = Paddle(white, 10, 100)
paddle_a.rect.x = 20
paddle_a.rect.y = 200

#right side paddle
paddle_b = Paddle(white, 10, 100)
paddle_a.rect.x = 670
paddle_b.rect.y = 200

#list of all sprites used in this project
sprites_list = pygame.sprite.Group()

#add the paddles to sprites_list
sprites_list.add(paddle_a)
sprites_list.add(paddle_b)


#stays on until player exits the game
stayOn = True

#the clock is used to control how fast the screen updates
clock = pygame.time.Clock()

#main loop
while stayOn:
    for event in pygame.event.get(): #user has done something
        if event.type == pygame.QUIT: #if user has closed the window
            stayOn = False # exits the loop
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_x:
                stayOn = False
    
    #moving the paddles
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        paddle_a.moveUp(5)
    if keys[pygame.K_s]:
        paddle_a.moveDown(5)
    if keys[pygame.K_UP]:
        paddle_b.moveUp(5)
    if keys[pygame.K_DOWN]:
        paddle_b.moveDown(5)


    # game logic
    sprites_list.update()

    #drawing
    #draw the screen black
    screen.fill(black)

    #draw the net
    pygame.draw.line(screen, white, [349, 0], [349, 500], 5)

    #draw the sprites 
    sprites_list.draw(screen)

    # update screen with what is drawn
    pygame.display.flip()

    # limit to 60 FPS
    clock.tick(60)

# exit
pygame.quit()
