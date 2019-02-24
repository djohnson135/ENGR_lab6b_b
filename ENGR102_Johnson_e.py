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
def estimate_pi(n):
    # define guess_value
    guess_val = 0
    num_loops = 0
    # for loop
    for k in range(n):
        num_loops += 1
        num1 = 4 * (-1) ** k #the value of numerator
        den1 = (2*k +1) #the value of denominator
        guess_val = guess_val + (num1/den1)
    return guess_val

current_tolerance = 10000
wanted_tolerance = 1e-4
k = 1
current_estimate = estimate_pi(k)
while current_tolerance >= wanted_tolerance:
    next_estimate = estimate_pi(k+1)
    current_tolerance = abs(current_estimate - next_estimate)
    k += 1
    current_estimate = next_estimate
print('Tolerance: ', current_tolerance)
print('Previous estimate: ', current_estimate)
print('Current estimate: ', next_estimate,'Iterations: ', k)

print('Pi: ', math.pi)