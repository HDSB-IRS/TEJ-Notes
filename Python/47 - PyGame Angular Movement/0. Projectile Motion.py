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

    # Create variables to control a ball
    pos = [50,300]                    #x and y posisitions of the ball
    size = 30                         #Size of the ball
    color = (255,0,0)                 #Color of the ball
    
    gravity = 0.10                    #How much the deltaY should change by
    theta = math.radians(45)          #Angle in degrees then converted to radians (don't forget to import math - see line 3)
    speed = 5                         #How fast the ball should travel
    deltaX = speed * math.cos(theta)  #Calculating the ball's motion in the x direction
    deltaY = -speed * math.sin(theta) #Calculating the ball's motion in the y direction
    
    while True:
        ev = pygame.event.poll()    # Look for any event
        if ev.type == pygame.QUIT:  # Window close button clicked?
            break                   #   ... leave game loop

        #Fill everything with the background color
        mainSurface.fill((0, 200, 255))

        #Move the circle
        pos[0] += deltaX  #Move the circle by the deltaY amount
        pos[1] += deltaY  #Move the circle by the deltaX amount
        
        deltaY += gravity #Decrease the deltaY to account for gravity
        
        # Draw the circle on the surface
        pygame.draw.circle(mainSurface, color, pos, size)

        # Now the surface is ready, tell pygame to display it!
        pygame.display.flip()
        
        clock.tick(60) #Force frame rate to 60FPS

    pygame.quit()     # Once we leave the loop, close the window.

main()
