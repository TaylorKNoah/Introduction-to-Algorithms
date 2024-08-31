
def InsertionSortAscending(listToSort: list[int], listSize: int) -> list[int]:
		sortedList = listToSort.copy()
		
		for i in range(1, listSize):
			key = sortedList[i]
			j = i-1
			while j > -1 and sortedList[j] > key:
				sortedList[j+1] = sortedList[j]
				j = j - 1
			sortedList[j+1] = key

		return sortedList

def InsertionSortDescending(listToSort: list[int], listSize: int) -> list[int]:
		sortedList = listToSort.copy()
		
		for i in range(1, listSize):
			key = sortedList[i]
			j = i-1
			while j > -1 and sortedList[j] < key:
				sortedList[j+1] = sortedList[j]
				j = j - 1
			sortedList[j+1] = key
		
		return sortedList