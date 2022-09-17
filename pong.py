import  pygame
pygame.init()

black = (0,0,0)
white = (255,255,255)

#open a window
size = (700, 500)
screen =  pygame.display.set_mode(size)
pygame.display.set_caption("Pong")

#stays on until player exits the game
stayOn = True

#the clock is used to control how fast the screen updates
clock = pygame.time.Clock()

#main
while stayOn:
    for event in pygame.event.get(): #user has done something
        if event.type == pygame.QUIT: #if user has closed the window
            stayOn = false # exits the loop

    # game logic

    #drawing
    #draw the screen black
    screen.fill(black)

    #draw the net
    pygame.draw.line(screen, white, [349, 0], [349, 500], 5)

    # update screen with what is drawn
    pygame.display.flip()

    # limit to 60 FPS
    clock.tick(60)

# exit
pygame.quit()
