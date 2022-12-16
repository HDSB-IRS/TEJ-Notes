#Practice

#1. Apply this technique to your circle program

import pygame
import random
import copy

def main():
    """ Set up the game and run the main game loop """
    pygame.init()      # Prepare the pygame module for use
    surfaceSize = 480   # Desired physical surface size, in pixels.

    clock = pygame.time.Clock()  #Force frame rate to be slower

    # Create surface of (width, height), and its window.
    mainSurface = pygame.display.set_mode((surfaceSize, surfaceSize))

    # Set up some data to describe a small rect and its color
    playerPos = pygame.Rect([50,100, 30, 30])  #X and Y Values
    prevPlayerPos = copy.copy(playerPos)
    playerColor = (255, 0, 0)        # A color is a mix of (Red, Green, Blue)
    playerSpeed = [0,0]
    accel = 4
    
    
    rectPosList = []
    rectColorList = []
    numRects = 5
    
    #Create a block that isn't random
    rectPosList.append( pygame.Rect(90,120,50,50)) 
    rectColorList.append( (random.randint(0,255),random.randint(0,255),random.randint(0,255)))

    #Create the blocks
    for count in range(numRects):
        rectPosList.append( pygame.Rect([random.randint(0,480),random.randint(0,480),50,50]) )
        rectColorList.append( (random.randint(0,255),random.randint(0,255),random.randint(0,255)))
    

    while True:
        ev = pygame.event.poll()    # Look for any event
        if ev.type == pygame.QUIT:  # Window close button clicked?
            break                   #   ... leave game loop
        elif ev.type == pygame.KEYDOWN:  #KEYDOWN has the attributes: key, mod, unicode, scancode
            # print('A Key was pressed down.  ', end='')
            # print(f'key: {ev.key}, mod: {ev.mod}, unicode: {ev.unicode}, scancode: {ev.scancode}')
            if ev.key == pygame.K_a:
                playerSpeed[0] -= accel
            elif ev.key == pygame.K_d:
                playerSpeed[0] += accel
            elif ev.key == pygame.K_w:
                playerSpeed[1] -= accel
            elif ev.key == pygame.K_s:
                playerSpeed[1] += accel

        elif ev.type == pygame.KEYUP:  #KEYDOWN has the attributes: key, mod, unicode, scancode
            # print('A Key was pressed down.  ', end='')
            # print(f'key: {ev.key}, mod: {ev.mod}, unicode: {ev.unicode}, scancode: {ev.scancode}')
            
            if ev.key == pygame.K_a:
                playerSpeed[0] += accel
            elif ev.key == pygame.K_d:
                playerSpeed[0] -= accel
            elif ev.key == pygame.K_w:
                playerSpeed[1] += accel
            elif ev.key == pygame.K_s:
                playerSpeed[1] -= accel
        # Update your game objects and data structures here...



        
        #Save the last player position
        prevPlayerPos = copy.copy(playerPos)
        playerPos[0] += playerSpeed[0]
        playerPos[1] += playerSpeed[1]
        #TODO: Add Gravity
              

        

        
        
        for count in range(numRects):
            pygame.draw.rect(mainSurface, rectColorList[count], rectPosList[count])

            #Check for collision
            if playerPos.colliderect(rectPosList[count]):
                print(f'Collision with {rectPosList[count]}')

                #Determine Direction Axis and then reposition as appropriate
                
                #           top down                                 top left
                if prevPlayerPos[1] < rectPosList[count][1]  and prevPlayerPos[1]+prevPlayerPos[3] <= rectPosList[count][1]: 
                    print("top")
                    playerPos[1] = rectPosList[count][1]-playerPos[3]
                    
                elif prevPlayerPos[0] >= rectPosList[count][0] +rectPosList[count][3] :
                    print("right")
                    playerPos[0] = rectPosList[count][0] +rectPosList[count][2]

                elif prevPlayerPos[0] <= rectPosList[count][0] and prevPlayerPos[1] < rectPosList[count][1]+rectPosList[count][3]:
                    print("left")
                    playerPos[0] = rectPosList[count][0] - playerPos[2]
                else:
                    print("bottom")
                    playerPos[1] = rectPosList[count][1]+rectPosList[count][3]


           

            
        # Draw a rect on the surface
        mainSurface.fill((0, 200, 255))
        pygame.draw.rect(mainSurface, playerColor, playerPos)
        
        #Draw all the boxes to collide with
        for count in range(numRects):
            pygame.draw.rect(mainSurface, rectColorList[count], rectPosList[count])

        # Now the surface is ready, tell pygame to display it!
        pygame.display.flip()
        
        clock.tick(60) #Force frame rate to be slower

    pygame.quit()     # Once we leave the loop, close the window.

main()