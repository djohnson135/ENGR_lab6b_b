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
n = int(1e9)
num_loops = 0
# for loop
for k in range(n):
    num_loops += 1
    num1 = 4 * (-1) ** k #the value of numerator
    den1 = (2*k +1) #the value of denominator
    guess_val = guess_val + (num1/den1)
    if num_loops == 1e0: #If and elif statements to find certain values in the range
        print(guess_val,num_loops) #output number of terms and the value
        continue
    elif num_loops == 1e1:
        print(guess_val,num_loops) #output number of terms and the value
        continue
    elif num_loops == 1e2:
        print (guess_val,num_loops) #output number of terms and the value
        continue
    elif num_loops == 1e3:
        print (guess_val,num_loops) #output number of terms and the value
        continue
    elif num_loops == 1e6:
        print(guess_val,num_loops) #output number of terms and the value
        continue
    elif num_loops == 1e9: # My IDE can not handle this value
        print(guess_val,num_loops) #output number of terms and the value
        break
    
print('Pi =',math.pi) #output pi
        
    
    

