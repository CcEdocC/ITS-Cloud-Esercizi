'''Suppose that you need to find the sum of integers from 1 to 10, 20 to 37, and 35 to 49. Write a Python program that
compute these three different sums.'''

sum:int = 0

for i in range(1,11):
    sum += i
    print("Sum from 1 to 10 is", sum)

sum:int = 0

for i in range (20,38):
    sum += i
    print("Sum from 20 to 37 is", sum)

sum:int = 0
for i in range(35,50):
    sum += i
    print("Sum from 35 to 49 is", sum)

