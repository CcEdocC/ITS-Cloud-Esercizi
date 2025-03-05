'''Exercise 1
Write a function check_value(), which takes a number as an argument.
Using if / else, the function should print whether the number is bigger, smaller, or equal to 5.
'''
def check_value(num):
    if num > 5:
        return(f"{num} is bigger than 5")
    elif num < 5:
        return(f"{num} is smaller than 5")
    else:
        return(f"{num} is equal to 5")

check_value(6)
check_value(14)
check_value(2)
