'''Program States allow you to control which section of your code is running through use of a state varaible'''
'''See a video explanation of this program here: https://drive.google.com/file/d/1GenlIgMC_mtQrsbsDHSdUKGkgHztPZHF/view?usp=sharing
'''
import pygame
import random
    
    
def main():
    """ Set up the game and run the main game loop """
    pygame.init()      # Prepare the pygame module for use
    surfaceSize = 480   # Desired physical surface size, in pixels.

    clock = pygame.time.Clock()  #Force frame rate to be slower

    # Create surface of (width, height), and its window.
    mainSurface = pygame.display.set_mode((surfaceSize, surfaceSize))

    programState = "start" #Set the program state to start on
    
    counter = 0 #A counter for demo purposes
    
    while True:
        print(f"Program Ticks: {pygame.time.get_ticks()} - programState: {programState}   counter: {counter}")
        ev = pygame.event.poll()    # Look for any event
        #Events that EVERY program state will need to use
        if ev.type == pygame.QUIT:  # Always need to do this, so needs to be outside the programState if statments!
            break                   #   ... leave game loop
        
        
        if programState == "start":
                #Check for events for the start screen
                if ev.type == pygame.MOUSEBUTTONUP:
                    programState = "initialize"
                        
                #Do the logic for the start screen
                            
                #Draw the stuff for the start screen
                mainSurface.fill((0, 200, 255))
            
        
        elif programState == "initialize": #Sometimes it's useful to separate out initialization code into a programState
            #That will only run once when called and then change the state to something else.
            #Check for events
            
            #Logic
            counter = 0 #Reset the counter
            programState = "pink screen"
            
            #Draw
            
        elif programState == "pink screen":
            #Events

            #Logic
            counter += 1
            if counter > 500:
                programState = "start"
            
            #Draw
            mainSurface.fill((255, 200, 255))
            
        
        else:
            print(f"Error - The program tried to load programState: {programState}.  Resetting back to start")
            programState = "start"

        

        


        # Now the surface is ready, tell pygame to display it!
        pygame.display.flip()
        
        clock.tick(60) #Force frame rate to be slower

    pygame.quit()     # Once we leave the loop, close the window.

main()
