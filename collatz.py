# Weekly Task for Week 04
# Author: Gillian Kane-McLoughlin

posint = int(input("Please enter a positive integer: "))
while posint !=1: 
    if posint % 2 ==0:
        print (posint)
        posint = (posint // 2) # divide by 2, result should be an integer
    else: 
        print (posint)
        posint = (posint * 3) + 1 # multiple x 3 first and then add 1
print (1) # as per the example provided, we should also include 1 in the output