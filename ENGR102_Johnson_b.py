# -*- coding: utf-8 -*-
"""
By submitting this assignment, I agree to the following:
“Aggies do not lie, cheat, or steal, or tolerate those who do”
“I have not given or received any unauthorized aid on this assignment”


Name : Dathan Johnson
Section : 409
Assignment : lab 6b-b
Date : 2-21-19
"""
#Averaging measurements:
#Assume that someone has collected a set of measurements and wants some statistical data
#about them. Write a program that asks a user for measurements and prints the average, the
#maximum, and the minimum measurement. Users should be allowed to enter as many
#measurements as they want, until entering a negative measurement. The negative
#measurement should not be processed, but is just used to indicate that the user has finished
#entering measurements. [Note: do not use a list to store the measurements.]
import math
# input for measurements
# variables to find average
meas = 0
total_num = 0
num = 0
max_num = 0
min_num = 0
def is_num(n):
    try:
        float(n)
    except ValueError:
        return False
    return True

# input for measurements
# input as a while loop
while meas >= 0:
    user_input = input('What is your measurement? (negative quits code) = ')
    if  not is_num(user_input):
        print('Please input a number')
        continue
    meas = float(user_input)
    if meas < 0:
        break
    if meas > max_num or num == 0:
        max_num = meas
    if meas < min_num or num == 0:
        min_num = meas
    total_num += meas
    num += 1
if num > 0:
    avg = total_num / num
    print('The maximum is: ', max_num)
    print('The minimum is: ', min_num)
    print('The average: ', avg)
print('Exit')

# if statements to find max and min

#print statement
