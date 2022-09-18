import pygame
black = (0,0,0)
class Paddle(pygame.sprite.Sprite):
    #this is the class for the paddle sprite

    def __init__(self, color, width, height):
        #calling the Sprite contstructor
        super().__init__()

        #pass in the color of the paddle
        self.image = pygame.Surface([width, height])
        self.image.fill(black)

        #drawing the paddle
        pygame.draw.rect(self.image, color, [0, 0, width, height])

        #grab the rectangle object that has the dimensions of the image
        self.rect = self.image.get_rect()



