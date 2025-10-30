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
    pos = [50,100]
    size = 30
    color = (255,0,0)
    xDirection = 0
    yDirection = 0
    speed = 1

    while True:
        ev = pygame.event.poll()    # Look for any event
        if ev.type == pygame.QUIT:  # Window close button clicked?
            break                   #   ... leave game loop
        elif ev.type == pygame.MOUSEBUTTONUP:          
            #Find the angle to the point clicked - stored in ev.pos
            clickedPos = ev.pos
            #Find change in x and y
            deltaX = clickedPos[0] - pos[0]
            deltaY = pos[1] - clickedPos[1]
            #Calculate the angle
            thetaRad = math.atan2(deltaY,deltaX)
            #Convert to degress (as most 11's don't know what a Radian is yet)
            thetaDeg = math.degrees(thetaRad)
            print(f'Angle: {thetaDeg} in degrees') 
            
            #set the direction
            xDirection = math.cos(thetaRad)
            yDirection = -math.sin(thetaRad)
            
 

        #Fill everything with the background color
        mainSurface.fill((0, 200, 255))

        #Move the circle
        pos[0] += speed * xDirection
        pos[1] += speed * yDirection
        
        # Draw the circle on the surface
        pygame.draw.circle(mainSurface, color, pos, size)

        # Now the surface is ready, tell pygame to display it!
        pygame.display.flip()
        
        clock.tick(60) #Force frame rate to 60FPS

    pygame.quit()     # Once we leave the loop, close the window.

main()