from microbit import *
import audio

print("Hello!")

multiple = 1 # initialise the counter

while True:
    if button_a.was_pressed(): # get the next multiple of the thirteen
        result = multiple * 13 # Calculate the result
        print("13 times " + str(multiple) + " is " + str(result)) # print the multiplication
        multiple = multiple + 1 # increment the multiple
    
    if button_b.was_pressed(): # Say Hello
        display.show(Image.HAPPY)
        audio.play(Sound.HAPPY)
        display.clear()
        
    sleep(10) # a 10 millisecond delay