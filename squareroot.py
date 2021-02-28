# Weekly Task for Week 06
# program that takes a positive floating-point number as input and outputs an approximation of its square root
# Author: Gillian Kane-McLoughlin

# Newton’s Method: Let N be any number, then the square root of N can be given by the formula:
# root N = 0.5 * (X + (N / X)) where X is any guess which can be assumed to be N or 1
# Ref: https://www.geeksforgeeks.org/find-root-of-a-number-using-newtons-method/#:~:text=Let%20N%20be%20any%20number,correct%20square%20root%20of%20N

n = float(input("Please enter a positive number: "))

def sqrt():
    guess = 1
    approx = round(0.5 * (guess + (n / guess)), 1) # rounding to 1 decimal point as per the example provided
    
    # Logic: the value of approx squared should be equal or close to the value of n (within a set parameter
    # setting a parameter of +/-0.5 for the approximation
    lowerParameter = n - 0.5    
    upperParameter = n + 0.5

    # using while loop and if statement to check the current value and change the value of guess as necessary
    while approx**2 < lowerParameter or approx**2 > upperParameter:
        if approx **2 < lowerParameter:
            guess += 0.75 # decided to add/subtract 0.75 as I was getting a ZeroDivisionError with 0.5 & 1
            approx = round(0.5 * (guess + (n / guess)), 1)
        else:
            guess -= 0.75
            approx = round(0.5 * (guess + (n / guess)), 1)

    return abs(approx) # my first result was a negative number, so returning the absolute value

approx = sqrt()
print ("The square root of", n, "is approximately", approx)
