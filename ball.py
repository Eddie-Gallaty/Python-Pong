import pygame
from random import randint
black = (0,0,0,)

class Ball(pygame.sprite.Sprite):
    #represnts a ball and is derived from the Sprite class in pygame

    def __init__(self, color, width, height):
        #call Sprite
        super().__init__()
        
        #pass in the color of the ball, width, height
        #set BG color and set it to be transparent
        self.image = pygame.Surface([width, height])
        self.image.fill(black)
        self.image.set_colorkey(black)

        #draw the ball
        pygame.draw.rect(self.image, color, [0, 0, width, height])

        self.velocity = [randint(4,8), randint(-8,8)]

        #grab the rectangle object with the same dimensions of the image
        self.rect = self.image.get_rect()
    
    #update the screen with the location of ball
    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]
    
    #adding bounce
    def bounce(self):
        self.velocity[0] = - self.velocity[0]
        self.velocity[1] = randint(-8, 8)