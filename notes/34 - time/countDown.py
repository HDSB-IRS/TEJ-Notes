#-----------------------------------------------------------------------------
# Name:        Time Example - Counting Down (countDown.py)
# Purpose:     To provide examples of how to count backwards using the time library.
#
# Author:      Mr. Brooks
# Created:     26-Oct-2021
# Updated:     12--04-2023
#-----------------------------------------------------------------------------
import time

#Store the current time
startTime = time.time()

#Store our end time
endTime = startTime + 10;

#Loop until our end time is reached
while endTime > time.time():
    #Print the difference between the two values
    print(endTime - time.time())