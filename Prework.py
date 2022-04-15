#Question 1: Write a function to print "hello_USERNAME!" USERNAME is the input of the function. 
# The first line of the code has been defined as below.
import numbers
from string import digits


def hello_name(user_name):
    print("hello_" + user_name.upper() + "!")

hello_name('ashley')


#Question 2: Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing.
def first_odds(odd_numbers):
    odd_numbers = list(range(1,100))
    return odd_numbers(0)

print(first_odds)


#Question 3: Please write a Python function, max_num_in_list to return the max number of a given list. 
# The first line of the code has been defined as below.

def max_num_in_list(a_list):
    """Return the max number in a given list."""
    a_list= (1,3,8,12,35)
    for list in a_list:
            max(a_list)

print(max_num_in_list)   


#Question 4: Write a function to return if the given year is a leap year. 
# A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. 
# The return should be boolean Type (true/false).

def is_leap_year(a_year):
    """Return if the given year is a leap year."""
   # a_year % 4 = True and a_year
   # is_leap_year = % 4
    #is_leap_year != % 100 unless % 400 

#return = True 


#Question 5: Write a function to check to see if all numbers in list are consecutive numbers. 
# For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. 
# The return should be boolean Type.


