'''Exercise 2
Write a function check_length(), which takes a string as an argument.
Using if / else, check if the length of the string is bigger, smaller, or equal to 10 characters.
'''

def check_length(string):
    if len(string) > 10:
        return(f"{string} is longer than 10 characters")
    elif len(string) < 10:
        return(f"{string} is shorter that 10 characters")
    else:
        return(f"string is 10 characters long")
    
check_length("come va sta sera?")
check_length("che bel cane!") 
check_length("eila ciao")


