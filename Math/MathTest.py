from AddBinaryIntegers import AddBinaryIntegers
from MathHelpers import BinaryToInt
from random import randint
from time import time

n = 2**12
a1_bin = [randint(0,1) for i in range(n)]
b1_bin = [randint(0,1) for i in range(n)]
a1_int = BinaryToInt(a1_bin, n)
b1_int = BinaryToInt(b1_bin, n)
print(f'Given ints {a1_int} and {b1_int}')
print(f'We should expect a binary array output that equals {a1_int+b1_int}')

start = time()
c_bin = AddBinaryIntegers(a1_bin, b1_bin, len(a1_bin))
end = time()
addTime = (end - start) * 10 ** 3

c_int = BinaryToInt(c_bin, len(c_bin))
print(f'Output is {c_int}')
print(f'Finished in {addTime} ms')