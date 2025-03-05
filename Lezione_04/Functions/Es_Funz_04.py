'''Exercise 4. Write a function check_each(), which takes a list of numbers as argument.
Using a for loop, iterate through the list.
For each number, print “bigger” if it’s bigger than 5, “smaller” if it’s smaller than 5, and “equal” if it’s equal to 5.
'''
def check_each(num_list):
    for element in num_list:
        if element > 5:
            return(f"{element} bigger than 5")
        elif element < 5:
            return(f"{element} smaller than 5")
        else:
            return(f"{element} equal to 5")

check_each(2, 8)
check_each(5, 13)
check_each(9, 15, 2)
