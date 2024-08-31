from InsertionSort import InsertionSortAscending, InsertionSortDescending
from random import randint
from time import time

size = 1000
unsortedList = [randint(0, 1000) for i in range(size)]
sortTimeStart = time()
sortedListAscending = InsertionSortAscending(unsortedList, len(unsortedList))
sortTimeEnd = time()
sortedListDescending = InsertionSortDescending(unsortedList, len(unsortedList))

print(f'Unsorted List: {unsortedList[:10]}')
print(f'Sorted List Ascending: {sortedListAscending[:10]}')
print(f'Sorted List Descending {sortedListDescending[:10]}')
sortTime = (sortTimeEnd - sortTimeStart) * 10 ** 3
print(f'InsertionSort Stats | Time for {size}: {sortTime} ms | {sortTime / size} ms / element')