# -*- coding: utf-8 -*-
"""
By submitting this assignment, I agree to the following:
“Aggies do not lie, cheat, or steal, or tolerate those who do”
“I have not given or received any unauthorized aid on this assignment”


Name : Dathan Johnson
Section : 409
Assignment : lab 6b-e
Date : 2-21-19
"""

#Series:
#Rather than guess at the number of terms to use to estimate the value of p, one can utilize a
#tolerance value. Construct a while loop that utilizes the for loop from the previous problem that
#will estimate p using an increasing number of terms until the difference between successive
#estimates is less than 1e-6. Print the estimated value of p along with the number of terms as
#well as the value of p from the math module.


# estimate pi using series




import math
# user input
# input number of terms
num_terms = 5
answer = 0
tolerance = 1e-2
err = 100
answer = 0
while err >= tolerance:
    value = answer
    guess_val = 0
    for n in range(num_terms):
        num1 = (-1) **n
        den1 = (2*n +1)
        guess_val += (num1/den1)
    answer = guess_val * 4
    print('Iterations: ', num_terms,  ' Value: ', answer)
    num_terms += 1
    err = abs(value - answer)
print(answer)
print(err)   
# Output (guess, actual value)
print(answer,num_terms)
print(math.pi)