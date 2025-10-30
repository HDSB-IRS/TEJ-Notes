#How to use pygame transformations
#https://www.pygame.org/docs/ref/transform.html

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
 
    #Make the image 2x the size
    doubledWizardImage = pygame.transform.scale2x(wizardImage)

    scale = 2;
    #Increases the image size by a factor
    scaledWizardImage = pygame.transform.scale(wizardImage, (scale*wizardImage.get_width(), scale*wizardImage.get_height() ))
    
    #Increases the image size by a factor - smooths image after
    smoothScaledWizardImage = pygame.transform.smoothscale(wizardImage, (scale*wizardImage.get_width(), scale*wizardImage.get_height() ))
    
    #This helps if the image looks really bad after scaling
    alphaWizardImage = pygame.transform.smoothscale(wizardImage.convert_alpha(), (scale*wizardImage.get_width(), scale*wizardImage.get_height() ))
 
    #Flips the image
    flippedImage = pygame.transform.flip(doubledWizardImage, True, False)
    
    #Rotates the image
    rotateImage = pygame.transform.rotate(doubledWizardImage, 45)
#     pygame.Surface.fill(rotateImage, (255,0,0))

 
    while True:
#         print(pygame.mouse.get_pos())
        
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
        
        
        mainSurface.blit(doubledWizardImage, wizardPos  )
        mainSurface.blit(wizardImage, wizardPos  )

        mainSurface.blit(scaledWizardImage, (wizardPos[0]+50,wizardPos[1]))

        mainSurface.blit(smoothScaledWizardImage, (wizardPos[0]+100,wizardPos[1]))
       
        mainSurface.blit(alphaWizardImage, (wizardPos[0]+150,wizardPos[1]))

        mainSurface.blit(flippedImage, (wizardPos[0]+200,wizardPos[1]))
        
        mainSurface.blit(rotateImage, (wizardPos[0]+250,wizardPos[1]))




        # Now the surface is ready, tell pygame to display it!
        pygame.display.flip()
        
        clock.tick(60) #Force frame rate to be slower

    pygame.quit()     # Once we leave the loop, close the window.

main()
