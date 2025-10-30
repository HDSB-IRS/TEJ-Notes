import pygame
import random
    
def main():
    """ Set up the game and run the main game loop """
    pygame.init()      # Prepare the pygame module for use
    surfaceSize = 480   # Desired physical surface size, in pixels.
    
    clock = pygame.time.Clock()  #Force frame rate to be slower

    # Create surface of (width, height), and its window.
    mainSurface = pygame.display.set_mode((surfaceSize, surfaceSize))
    
    wizardImage = pygame.image.load("images/dungeon/frames/wizzard_m_idle_anim_f0.png")
    wizardPos = [50,50]  #random.randrange(surfaceSize) would make it go to a random x pos
 
    #Make the image a bit bigger for the projector
#     wizardImage = pygame.transform.scale2x(wizardImage)
 
    while True:
        ev = pygame.event.poll()    # Look for any event
        if ev.type == pygame.QUIT:  # Window close button clicked?
            break                   #   ... leave game loop

        # Update your game objects and data structures here...

        #Move the wizard
#         wizardPos[0] += 0.5   #update the x
        
        
        
        # We draw everything from scratch on each frame.
        # So first fill everything with the background color
        mainSurface.fill((0, 200, 255))
        
        #Draw the wizards
        mainSurface.blit(wizardImage, wizardPos)

        # Now the surface is ready, tell pygame to display it!
        pygame.display.flip()
        
        clock.tick(60) #Force frame rate to be slower

    pygame.quit()     # Once we leave the loop, close the window.

main()
