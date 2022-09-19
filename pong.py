import pygame
from paddle import Paddle
from ball import Ball

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
paddle_a.rect.x = 690
paddle_b.rect.y = 200

#ball
ball = Ball(white, 10, 10)
ball.rect.x = 345
ball.rect.y = 195

#list of all sprites used in this project
sprites_list = pygame.sprite.Group()

#add the paddles to sprites_list
sprites_list.add(paddle_a)
sprites_list.add(paddle_b)
sprites_list.add(ball)


#stays on until player exits the game
stayOn = True

#the clock is used to control how fast the screen updates
clock = pygame.time.Clock()

#players score
scoreA = 0
scoreB = 0

player1 = "Player 1"
player2 = "Player 2"

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

    #check if ball is bouncing
    if ball.rect.x >= 690:
        scoreA += 1
        ball.velocity[0] = - ball.velocity[0]
    if ball.rect.x <= 0:
        scoreB += 1
        ball.velocity[0] = - ball.velocity[0]
    if ball.rect.y > 490:
        ball.velocity[1] = - ball.velocity[1]
    if ball.rect.y < 0:
        ball.velocity[1] = - ball.velocity[1]
    
    #detect if ball is bouncing off paddle a or b
    if pygame.sprite.collide_mask(ball, paddle_a) or pygame.sprite.collide_mask(ball, paddle_b):
        ball.bounce()
    #drawing
    #draw the screen black
    screen.fill(black)

    #draw the net
    pygame.draw.line(screen, white, [350, 0], [350, 500], 5)

    #draw the sprites 
    sprites_list.draw(screen)
    
    #display names
    font = pygame.font.Font(None, 30)
    text = font.render(player1, 1, white)
    screen.blit(text, (225, 10))
    text = font.render(player2, 1, white)
    screen.blit(text, (400, 10))

    #display scores
    font = pygame.font.Font(None, 74)
    text = font.render(str(scoreA), 1, white)
    screen.blit(text, (250,35))
    text = font.render(str(scoreB), 1, white)
    screen.blit(text, (420,35))

    # update screen with what is drawn
    pygame.display.flip()

    # limit to 60 FPS
    clock.tick(60)

# exit
pygame.quit()
