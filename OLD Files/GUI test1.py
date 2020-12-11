#! /usr/bin/python
# _*_ coding: utf-8 _*_

import sys
import os
import pygame
import twisted


class YMMain:
    #main method for game
    
    def __init__ (self, width=640,height=480):
        #
        #Initialize
        
        pygame.init
        
        
        # Initialise screen
        pygame.init()
        screen = pygame.display.set_mode((650, 450))
        pygame.display.set_caption('Player Stats')
    
        # Fill background
        background = pygame.Surface(screen.get_size())
        background = background.convert()
        background.fill((250, 250, 250))
    
        # Display some text
        font = pygame.font.Font(None, 36)
        text = font.render("Hello There", 1, (10, 10, 10))
        textpos = text.get_rect()
        textpos.centerx = background.get_rect().centerx
        background.blit(text, textpos)
    
        # Blit everything to the screen
        screen.blit(background, (0, 0))
        pygame.display.flip()
    

        
    def MainLoop(self):
        #game Loop
        
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                

                    def main():
                        # Initialise screen
                        pygame.init()
                        screen = pygame.display.set_mode((150, 50))
                        pygame.display.set_caption('Basic Pygame program')
                    
                        # Fill background
                        background = pygame.Surface(screen.get_size())
                        background = background.convert()
                        background.fill((250, 250, 250))
                    
                        # Display some text
                        font = pygame.font.Font(None, 36)
                        text = font.render("Hello There", 1, (10, 10, 10))
                        textpos = text.get_rect()
                        textpos.centerx = background.get_rect().centerx
                        background.blit(text, textpos)
                    
                        # Blit everything to the screen
                        screen.blit(background, (0, 0))
                        pygame.display.flip()
                    
                        # Event loop
                        while 1:
                            for event in pygame.event.get():
                                if event.type == QUIT:
                                    return


if __name__ == "__main__":
    MainWindow = YMMain()
    MainWindow.MainLoop()