'''
#Practice

1. Make the circle go up.
2. Make the circles move faster when you click the mouse button (Events)
3. Control the circles with a keyboard command
4. Challenge - Make the circles wrap around the screen (or bounce off the screen)
'''

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
    # Set up some data to describe a small circle and its color
    circlePos = [50,100]  #X and Y Values
    circleSize = 30  
    circleColor = (255, 0, 0)        # A color is a mix of (Red, Green, Blue)
    
    circlePos2 = [50,300]  #X and Y Values
    circleSize2 = 30  
    circleColor2 = (0, 0, 255)        # A color is a mix of (Red, Green, Blue)
    #-----------------------------Main Program Loop---------------------------------------------#
    while True:       
        #-----------------------------Event Handling-----------------------------------------#
        ev = pygame.event.poll()    # Look for any event
        if ev.type == pygame.QUIT:  # Window close button clicked?
            break                   #   ... leave game loop

        #-----------------------------Program Logic---------------------------------------------#
        # Update your game objects and data structures here...

        #Move the circles
        #circlePos[0] = circlePos[0] +1
        circlePos[0] += 1
        circlePos2[0] -= 1
        
        #-----------------------------Drawing Everything-------------------------------------#
        # We draw everything from scratch on each frame.
        
        mainSurface.fill((0, 200, 255)) # So first fill everything with the background color
        
        # Draw a circle on the surface
        pygame.draw.circle(mainSurface, circleColor, circlePos, circleSize)
        pygame.draw.circle(mainSurface, circleColor2, circlePos2, circleSize2)

        # Now the surface is ready, tell pygame to display it!
        pygame.display.flip()
        
        clock.tick(60) #Force frame rate to be slower

    pygame.quit()     # Once we leave the loop, close the window.

main()