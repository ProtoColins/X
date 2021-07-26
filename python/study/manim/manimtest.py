from manim import *
import manim
#import everything

#constants: in 
manim.constants

class Hello_World (Scene):
    #inherit Scene (individual animation)
    def construct( self ):
        #construct method is vital ,like main() ?

        #making objects
        HelloWorld = Tex("Hello world" , color = RED)
      
        Hellomanim = Tex("Hello mainm" , color = RED)
     
        #positioning

        #display objects
        self.play(Write(HelloWorld))
        self.wait(1)
        self.play(Transform(HelloWorld,Hellomanim))
        self.play(Wiggle(Hellomanim))
        self.wait(1)
    