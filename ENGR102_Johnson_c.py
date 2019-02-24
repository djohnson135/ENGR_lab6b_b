# -*- coding: utf-8 -*-
"""
By submitting this assignment, I agree to the following:
“Aggies do not lie, cheat, or steal, or tolerate those who do”
“I have not given or received any unauthorized aid on this assignment”


Name : Dathan Johnson
Section : 409
Assignment : lab 6b-c
Date : 2-21-19
"""

#Divisors:
#For numbers from 2 to 100, print a series of lines indicating which numbers are divisors of other
#numbers. For each, print out “X divides Y”, where X <= Y, and both X and Y are between 2 and
#100. The first few lines will be:
#2 divides 2
#3 divides 3
#2 divides 4
#4 divides 4
#5 divides 5
#etc.

#create variables

# make a for statement
for i in range(2, 101):
    for k in range(2,101):
        if i % k == 0 and i >= k: #if statement
            print(k, 'divides',i) #print statements
        


