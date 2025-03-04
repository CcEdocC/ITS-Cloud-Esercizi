'''Functions/3: Exercise
Let’s try to define a function named subtract ourselves:
● It should take 2 parameters.
● Inside the function, it should subtract the two.
● Then, return the result.
After you defined it, call the function with some arguments!'''

def substract(a:int,b:int):
    result:int = a - b
    return result

myresult = substract(10, 3)
print(myresult)

myresult = substract(29, 7)
print(myresult)


