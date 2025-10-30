import pygame
import math

def main():
    #-----------------------------Setup------------------------------------------------------#
    """ Set up the game and run the main game loop """
    pygame.init()      # Prepare the pygame module for use
    surfaceSize = 480   # Desired physical surface size, in pixels.
    
    clock = pygame.time.Clock()  #Force frame rate to be slower

    # Create surface of (width, height), and its window.
    mainSurface = pygame.display.set_mode((surfaceSize, surfaceSize))

    #-----------------------------Program Variable Initialization----------------------------#
    font = pygame.font.SysFont("Arial", 26)  #Create a font object

     
    #-----------------------------Main Program Loop---------------------------------------------#
    while True:
        #-----------------------------Event Handling-----------------------------------------#
        ev = pygame.event.poll()    # Look for any event
        if ev.type == pygame.QUIT:  # Window close button clicked?
            break                   #   ... leave game loop

        #-----------------------------Program Logic---------------------------------------------#
        words = "Hello Everyone!"  #The words to draw on the screen


        #-----------------------------Drawing Everything-------------------------------------#
        mainSurface.fill((0, 100, 0))  #Draw the background color
        
        #Create an image of the text using the font object
        renderedText = font.render(words, 1, pygame.Color("coral"))
        
        #Put the image on the mainSurface
        mainSurface.blit(renderedText, (10,0))

        pygame.display.flip()  #Display everything
     
    pygame.quit()

main()