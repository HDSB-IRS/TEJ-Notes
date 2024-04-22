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

    # Create the the size, position and color for a circle
    rectangleDimensions  = [200,200,100,30] #x, y, width, height
    rectangle = pygame.Rect(rectangleDimensions)
    rectangleColor = (255,0,0)
    

    
    while True:
        ev = pygame.event.poll()    # Look for any event
        if ev.type == pygame.QUIT:  # Window close button clicked?
            break                   #   ... leave game loop
        
           
        # Update your game objects and data structures here...
        mousePos = pygame.mouse.get_pos()
        pointX = mousePos[0]
        pointY = mousePos[1]
        
        if(pointX > rectangle.x and pointX < rectangle.x + rectangle.width):
            if(pointY > rectangle.y and pointY < rectangle.y + rectangle.height):
                rectangleColor = (100,0,0)
            else:
                rectangleColor = (255,0,0)
                #the point is inside the rectangle
                
        
        # We draw everything from scratch on each frame.
        # So first fill everything with the background color
        mainSurface.fill((0, 200, 255))

        #Draw Rectangle  
        pygame.draw.rect(mainSurface, rectangleColor, rectangle)       

        # Now the surface is ready, tell pygame to display it!
        pygame.display.flip()
        
        clock.tick(60) #Force frame rate to be slower

    pygame.quit()     # Once we leave the loop, close the window.

main()
