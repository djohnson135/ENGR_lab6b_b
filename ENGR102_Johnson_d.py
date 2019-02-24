# -*- coding: utf-8 -*-
"""
By submitting this assignment, I agree to the following:
“Aggies do not lie, cheat, or steal, or tolerate those who do”
“I have not given or received any unauthorized aid on this assignment”


Name : Dathan Johnson
Section : 409
Assignment : lab 6b-d
Date : 2-21-19
"""
#Series:
#Series are used to quickly estimate functions or values. The following summation can be used to
#estimate p. Using a for loop, estimate the value of p for the following number of terms, n: 1, 10,
#100, 1000, 1e6, 1e9. Print the estimated values along with the number of terms as well as the
#value of p from the math module.


# estimate pi using series

import math

# define guess_value
guess_val = 0
# for loop
for n in range(1000000001):
    num1 = (-1) ** n #the value of numerator
    den1 = (2*n +1) #the value of denominator
    guess_val = guess_val + (num1/den1)
    answer = guess_val * 4
    if n == 1: #If and elif statements to find certain values in the range
        print(answer,n) #output number of terms and the value
        continue
    elif n == 10:
        print(answer,n) #output number of terms and the value
        continue
    elif n == 100:
        print (answer,n) #output number of terms and the value
        continue
    elif n == 1000:
        print (answer,n) #output number of terms and the value
        continue
    elif n == 1000000:
        print(answer,n) #output number of terms and the value
        continue
    elif n == 1000000000: # My IDE can not handle this value
        print(answer,n) #output number of terms and the value
        break
    
print('Pi =',math.pi) #output pi
        
    
    

