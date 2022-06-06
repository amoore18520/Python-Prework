# PYTHON PREWORK ASSIGNMENT

# QUESTION # 1 - Write a function to print "hello_USERNAME!" 
# ...is the input of the function.

def hello_name(username):
    """Display a simple greeting to a username."""
    print("\nHello, " + username.title())

hello_name('austin')

# QUESTION # 2 - Write a Python function, first_odds that prints
# ...the odd numbers from 1-100 and returns nothing.

def first_odds(num):
    odd_numbers = []
    for n in range(num): 
        if n % 2 == 1:
            odd_numbers.append(n)
    return odd_numbers

# QUESTION # 3 - Please write a Python function, max_num_in_list to return the
# ...max number given of a list. 

def max_num_in_list(a_list):
    max_num = a_list[0]
    for n in a_list:
        if n > max_num:
            max_num = n
    return max_num

a_list = [11, 23, 76, 101, 34, 98, 47, 202]
print("The max number is: ", max_num_in_list(a_list))

# QUESTION # 4 - Write a function to return if the given year is a leap year.
# ...A leap year is divisible by 4, but not divisible by 100, unless it is also
# ...divisible by 400.

def is_leap_year(a_year):
    leap = False
    if a_year % 4 == 0:
        leap = True
        if a_year % 4 == 0 and a_year % 100 == 0:
            leap = False
            if a_year % 400 == 0:
                leap = True
    return leap

year = int(input("Enter a year to check and see if it's a leap year: "))
leap = is_leap_year(year)

if leap:
    print(str(year) + " is a leap year!")
else:
    print(str(year) + " is not a leap year.")

# QUESTION # 5 - Write a function to check to see if all numbers in a list are
# ...consecutive numbers.

def is_consecutive(a_list):
    a_list = sorted(a_list)
    if a_list:
        return a_list == list(range(a_list[0], a_list[-1] + 1))
    else:
        return True

list1 = [1,3,5,7,6,8,2,4]
print(is_consecutive(list1))



















