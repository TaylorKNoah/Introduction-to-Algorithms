from typing import Optional

def LinearSearch(array: list[int], n: int, x: int) -> Optional[int]:
	"""
	array:
		An array of integers
	n:
		the length of the array
	x:s
		an integer to search for in the array

	returns:
		None if x is not in array
		The index of the array at which x is first located
	"""
	
	index = None
	i = 1
	while i < n+1 and index == None:
		if array[i] == x:
			index = i
		i = i + 1
	return index