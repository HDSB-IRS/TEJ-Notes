import pygame
import random
import math
    
def main():
    """ Set up the game and run the main game loop """
    pygame.init()      # Prepare the pygame module for use
    surfaceSize = 480   # Desired physical surface size, in pixels.

    clock = pygame.time.Clock()  #Force frame rate to be slower

    # Create surface of (width, height), and its window.
    mainSurface = pygame.display.set_mode((surfaceSize, surfaceSize))

    # Create the the size, position, speed and color for a circle
    circlePos  = [200,200]  #[x,y] position
    circleSize = 30         #Radius of the circle
    circleColor = (255,0,0) #Color of the circle
    circleSpeed = [1,2.5]   #Speed in the x and y directions
    

    
    while True:
        ev = pygame.event.poll()    # Look for any event
        if ev.type == pygame.QUIT:  # Window close button clicked?
            break                   #   ... leave game loop
        
           
        # Update your game objects and data structures here...
           
        circlePos[0] += circleSpeed[0]
        circlePos[1] += circleSpeed[1]
        
        if circlePos[0] >= surfaceSize:  #Right Side
            circleSpeed[0] = circleSpeed[0]*-1
        elif circlePos[0] <= 0:          #Left Side
            circleSpeed[0] = circleSpeed[0]*-1
        
        if circlePos[1] >= surfaceSize:  #Top Side
            circleSpeed[1] = circleSpeed[1]*-1
        elif circlePos[1] <= 0:          #Bottom Side
            circleSpeed[1] = circleSpeed[1]*-1
        
        # We draw everything from scratch on each frame.
        # So first fill everything with the background color
        mainSurface.fill((0, 200, 255))

        pygame.draw.circle(mainSurface, circleColor, circlePos, circleSize) #Draw Circle
        #pygame.draw.circle(mainSurface, mouseCircleColor, mouseCirclePos, mouseCircleSize) #Draw mouseCircle
        

        # Now the surface is ready, tell pygame to display it!
        pygame.display.flip()
        
        clock.tick(60) #Force frame rate to be slower

    pygame.quit()     # Once we leave the loop, close the window.

main()
