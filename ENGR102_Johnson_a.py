# -*- coding: utf-8 -*-
"""
By submitting this assignment, I agree to the following:
“Aggies do not lie, cheat, or steal, or tolerate those who do”
“I have not given or received any unauthorized aid on this assignment”


Name : Dathan Johnson
Section : 409
Assignment : lab 6b-a
Date : 2-21-19
"""

#test

# the collatz conjecture
#make input variables
posint = int(input('Enter a positive real number= '))
#list of variables used
#num val equals number of iterations to equal 1
num_val = 0
i = posint
odd = (3 * i) + 1

# if statements if applicable
#loop
print(i)
while i != 1:
    if i % 2 == 0:
        i /= 2
    else:
        odd = (3 * i) + 1
        i = odd
    print(i)
    num_val += 1
    
#Given a number, n, if n is even then the next number is n divided by 2
#If n is odd, then the next number is 3n+1


#print statement
print('Amount of iterations = ',num_val)  
#printing out all the numbers in the sequence, followed by a line stating how many
#iterations it took to reach the value 1