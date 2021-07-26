import pygame
import os,sys
from pygame.locals import *
import random

#still no friendly hints

Height , Width = 720 , 1080


class Chead (pygame.sprite.Sprite):
    '''Create a bouncing object that would fade upon cliking'''
    
    def  __init__( self , Image = pygame.image.load( r'D:\#CXNOVA\UNI-STOCK\Codes\X\python\study\pyGame\Chead.png') ):
        self.image = Image
        self.clicked = False
        self.rect = Image.get_rect()
        self.speed = [3,4]
        self.posX = random.randint( 0 , Width )
        self.posY = random.randint( 0 , Height)
    def update ( self ):
        if self.clicked == False:
            self.bounce
            self.move
        else :
            self.fade()


    def fade ( self ) :
        pass
    def bounce( self ):
        if self.rect.Top < 0 or self.Bottom > Height :
            self.speed[1] = -self.speed[1]
        if self.rect.left < 0 or self.right > Width : 
            self.speed[0] = -self.speed[1]
    def move( self ):
        self.rect = self.rect.move( self.speed )
    
def main():
    # Initialise screen
    pygame.init()
    screen = pygame.display.set_mode((150, 50))
    pygame.display.set_caption('Basic Pygame program')

    # Fill background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((250, 250, 250))

    

    # Blit everything to the screen
    screen.blit(background, (0, 0))
    pygame.display.flip()

    # Event loop
    while 1:
        for event in pygame.event.get():
            if event.type == QUIT:
                return

        screen.blit(background, (0, 0))
        pygame.display.flip()



if __name__ == '__main__': main()