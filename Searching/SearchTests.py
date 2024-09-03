from LinearSearch import LinearSearch
from random import randint
from time import time

n = 10000
array = [randint(0, 100) for i in range(n)]
array.append(101)
x = 101

start = time()
index = LinearSearch(array, n, x)
end = time()

searchTime = (end - start) * 10 ** 3

print(f'{x} found in array at index {index}')
print(f' Search time: {searchTime} ms')