import pygame

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
    circleColor = (255, 0, 0)        # A color is a mix of (Red, Green, Blue)
    circleSize = 20

    #-----------------------------Main Program Loop---------------------------------------------#
    while True:       
        #-----------------------------Event Handling-----------------------------------------#
        ev = pygame.event.poll()    # Look for any event
        if ev.type == pygame.QUIT:  # Window close button clicked?
            break                   #   ... leave game loop


        #-----------------------------Program Logic---------------------------------------------#
        # Update your game objects and data structures here...


        #-----------------------------Drawing Everything-------------------------------------#
        # We draw everything from scratch on each frame.
        # So first fill everything with the background color
        mainSurface.fill((0, 200, 255))

               
        # Draw a circle on the surface
        pygame.draw.circle(mainSurface, pygame.Color(255,0,0), (50,100), circleSize)
        #This doesn't work (although you might expect it to...)
        pygame.draw.circle(mainSurface, pygame.Color(255,0,0,10), (100,100), circleSize)
        
        #This is a functioning way to make transparent shapes in pygame
        s = pygame.Surface((circleSize*2,circleSize*2), pygame.SRCALPHA)   #Make sure this is big enough for your image - SCRALPHA - per-pixel alpha
        s.fill((255,255,255,0))                         # notice the alpha value in the color
        pygame.draw.circle(s, pygame.Color(255,0,0,125), (circleSize, circleSize), 20)        
        mainSurface.blit(s, (200,200))
        
        # Now the surface is ready, tell pygame to display it!
        pygame.display.flip()
        
        clock.tick(60) #Force frame rate to be slower


    pygame.quit()     # Once we leave the loop, close the window.

main()