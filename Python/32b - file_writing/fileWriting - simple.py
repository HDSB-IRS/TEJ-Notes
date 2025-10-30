#-----------------------------------------------------------------------------
# Name:        File Writing (fileWriting - simple.py)
# Purpose:     To provide examples of how to read from files.
#              Example from http://openbookproject.net/thinkcs/python/english3e/files.html
#
# Author:      Mr. Brooks
# Created:     21-Oct-2021
# Updated:     21-Oct-2021
#-----------------------------------------------------------------------------

string = "This will be written to a file\r\n"

# Using a 'w' erases everything in the file that was already there
# Using a 'a' adds the content to the end of the file.
file = open('output.txt', 'a')
file.write(string)
file.close()