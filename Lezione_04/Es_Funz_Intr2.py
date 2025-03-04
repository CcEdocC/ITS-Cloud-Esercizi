'''We can rewrite this code simplifying it using functions.
Suppose that you need to find the sum of integers from 1 to 10, 20 to 37, and 35 to 49. Write a Python program that
compute these three different sums.
Expected Output:
Sum of integers from 1 to 10 is 55
Sum of integers from 20 to 37 is 513
Sum of integers from 35 to 49 is 630
'''

def SumInRange(a:int, b:int):
    result:int = 0
    for i in range(a, b+1):
        result = result + i
    return result

mysum = SumInRange(1,10)
mysum = SumInRange(20,37)
mysum = SumInRange(35,49)

print(f"Sum from 1 to 10 is {SumInRange(1,10)}")
print(f"Sum from 20 to 37 is {SumInRange(20,37)}")
print(f"Sum from 35 to 49 is {SumInRange(35,49)}")
