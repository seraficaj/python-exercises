# Write a function to compute the `factorial` of a number.
# Given a whole number n, a factorial is the product of all
# whole numbers from 1 to n.
# 5! = 5 * 4 * 3 * 2 * 1
#
# Example function call
#
# factorial(5)
#
# > 120
#
def factorial(n):
    if n == 1: 
        return 1
    return n * factorial(n-1)

# Call the function
print(factorial(5))