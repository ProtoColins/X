import pygame
import sys
import random


pygame.init()

Head = pygame.image.load( r'D:\#CXNOVA\UNI-STOCK\Codes\X\python\study\pyGame\Chead.png' ).convert()


class BouncingObject():
    ''' Objects that bounce around the window '''

    def __init__( self , image ):
        '''write the parms'''
        self.image = image
        self.rect = image.get_rect()
        self.pos = random.randint(0 , 720)

    def move( self , speed ):
        '''move around the window , also attach a bouncing effect'''
        self.rect = self.rect.move( speed )

        #if self.
