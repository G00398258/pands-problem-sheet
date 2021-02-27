# Weekly Task for Week 06
# program that takes a positive floating-point number as input and outputs an approximation of its square root
# Author: Gillian Kane-McLoughlin

# Newton’s Method:
# Let N be any number then the square root of N can be given by the formula:
# root N = 0.5 * (X + (N / X)) where X is any guess which can be assumed to be N or 1.
# Ref: https://www.geeksforgeeks.org/find-root-of-a-number-using-newtons-method/#:~:text=Let%20N%20be%20any%20number,correct%20square%20root%20of%20N.

n = float(input("Please enter a positive floating point number: "))
guess = 0.5
approx = 0.5 * (guess + (n / guess))

# setting a parameter of +/-1 for the approximation
while approx * approx !=(n + 0.5) or approx * approx != (n - 0.5):
    guess += 0.5
    approx = 0.5 * (guess + (n / guess))

print ("The square root of", n, "is approximately", approx)



