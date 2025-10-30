import pygame
import random
    
    
def main():
    """ Set up the game and run the main game loop """
    pygame.init()      # Prepare the pygame module for use
    surfaceSize = 480   # Desired physical surface size, in pixels.

    clock = pygame.time.Clock()  #Force frame rate to be slower

    # Create surface of (width, height), and its window.
    mainSurface = pygame.display.set_mode((surfaceSize, surfaceSize))
    
    # Set up a variable to count the number of frames
    frameCount = 0

    # Create the circle lists
    circlePosList = []
    circleSizeList = []
    circleColorList = []
    numCircles = 5
    
    # Add Circles to the list
    for count in range(numCircles):
        circlePosList.append( [random.randint(0,480),random.randint(0,480)] )
        circleSizeList.append( random.randint(5, 50))
        circleColorList.append( (random.randint(0,255),random.randint(0,255),random.randint(0,255)))

    while True:
        ev = pygame.event.poll()    # Look for any event
        if ev.type == pygame.QUIT:  # Window close button clicked?
            break                   #   ... leave game loop

        # Update your game objects and data structures here...
        #Move the circles
        for count in range(len(circlePosList)): #Get the actual length of list instead of relying on numCircles
            circlePosList[count][0] += 1   

        #Increment the frame counter for every game loop
        frameCount += 1
        print(frameCount)
        
        #Add a circle if the frame counter is big enough
        if frameCount % 60 ==0:  #ie.  Once every second since 60 fps
            circlePosList.append( [20,random.randint(0,480)] )
            circleSizeList.append( random.randint(5, 50))
            circleColorList.append( (random.randint(0,255),random.randint(0,255),random.randint(0,255)))
            #It would be better to do the above 3 lines in a function to save code repetition.
            
            #Reset the frame counter so we can do it all over again
            frameCount = 0
            
        # Draw Everything
        # Fill everything with the background color
        mainSurface.fill((0, 200, 255))

        #Draw all the circles
        for count in range(len(circlePosList)):
            pygame.draw.circle(mainSurface, circleColorList[count], circlePosList[count], circleSizeList[count])

        # Now the surface is ready, tell pygame to display it!
        pygame.display.flip()
        
        clock.tick(60) #Force frame rate to be slower

    pygame.quit()     # Once we leave the loop, close the window.

main()
