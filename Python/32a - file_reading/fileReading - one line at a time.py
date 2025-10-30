#-----------------------------------------------------------------------------
# Name:        File Reading (fileReading - one line at a time.py)
# Purpose:     To provide examples of how to read from files.
#              Example from http://openbookproject.net/thinkcs/python/english3e/files.html
#
# Author:      Mr. Brooks
# Created:     21-Oct-2021
# Updated:     21-Oct-2021
#-----------------------------------------------------------------------------
file = open("fruit.txt", "r")   # Open the file
while True:                            # Keep reading forever
    theLine = file.readline()   # Try to read next line
    if len(theLine) == 0:              # If there are no more lines
        break                          # Leave the loop

    # Now process the line we've just read
    print(theLine, end="")

file.close() #Close the file for another program can use it