# Weekly Task for Week 07 - write a program that reads in a text file and outputs the number of e's it contains
# The program should take the filename from an argument on the command line
# Author: Gillian Kane-McLoughlin

# See README file for references

import sys # this will provide access to the command-line arguments

def letterFrequency(letter): 
    # open file in read text mode 
    with open(sys.argv[1], 'rt') as f: # taking the file name from the command line
        text = f.read() 
        # declare count variable of zero to begin with
        count = 0
        # for loop - check each character & increase count if letter is found
        for char in text: 
            if char == letter: 
                count += 1
  
    return count 
  
  
# call the function and display the count of letter 'e' (I interpreted the instructions literally as lower case e)
print(letterFrequency('e')) 