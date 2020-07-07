"""
Functions
"""

# 1. Defining a function
def my_function():
    print("Hello From My Function!")

my_function()

# 2. Receiving arguments
def my_function_with_args(username, greeting):
    print("Hello, %s , From My Function!, I wish you %s" %
          (username, greeting))

my_function_with_args("my_username_is_awesome", "Hi!")

# 3. Returning values
def sum_two_numbers(a, b):
    return a + b

sum_two_numbers(2, 2)