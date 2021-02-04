# Weekly Task for Week 03 
# program will ask a user to input a string and outputs every second letter in reverse order
# Author: Gillian Kane-McLoughlin

sentence = input("Please enter a sentence: ")

# Use negative index and stride -2 to output that sentence in reverse order
# Ref: https://www.digitalocean.com/community/tutorials/how-to-index-and-slice-strings-in-python-3

print (sentence[::-2])