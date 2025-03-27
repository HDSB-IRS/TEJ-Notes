import pygame
import math

def update_fps(font, clock):
	fps = str(int(clock.get_fps()))
	fps_text = font.render(fps, 1, pygame.Color("coral"))
	return fps_text

def main():
    #-----------------------------Setup------------------------------------------------------#
    """ Set up the game and run the main game loop """
    pygame.init()      # Prepare the pygame module for use
    surfaceSize = 480   # Desired physical surface size, in pixels.
    
    clock = pygame.time.Clock()  #Force frame rate to be slower

    # Create surface of (width, height), and its window.
    mainSurface = pygame.display.set_mode((surfaceSize, surfaceSize))

    #-----------------------------Program Variable Initialization----------------------------#
    # Set up some data to describe a small circle and its color
    font = pygame.font.SysFont("Arial", 26)
 
    #-----------------------------Main Game Loop---------------------------------------------#
    while True:
        
        #-----------------------------Event Handling-----------------------------------------#
        ev = pygame.event.poll()    # Look for any event
        if ev.type == pygame.QUIT:  # Window close button clicked?
            break                   #   ... leave game loop


        #-----------------------------Program Logic---------------------------------------------#
        # Update your game objects and data structures here...
 
        #-----------------------------Drawing Everything-------------------------------------#
        mainSurface.fill((0, 200, 255))  #Draw the background color

        mainSurface.blit(update_fps(font,clock), (10,0))  #Draw the returned rendered text on the surface
        
        pygame.display.flip()  #Display everything
        
        print(clock.tick(60))  #Note - clock.tick returns the number of seconds since it was last called!


 
    pygame.quit()
    
main()