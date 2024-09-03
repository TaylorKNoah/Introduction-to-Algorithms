
def IntToBinary(x: int) -> list[int]:
	"""
	Converts an int into a array of ints representing the binary representation

	x: an int to convert into binary
	"""
	if x == 0:
		return 0
	
	binary_representation = []

	i = x
	while i > 0:
		remainder = i % 2
		binary_representation.append(remainder)
		i //= 2

	return binary_representation

def BinaryToInt(A: list[int], n: int):
	"""
	Converts a Binary array into an int
	A: A binary array
	"""
	if not IsBinaryArray(A, n):
		raise ValueError("Parameter A must be a binary array.")
	
	result = 0
	for i in range(n):
		bit = A[i]
		power = n - 1 - i
		result += bit * (2**power)
	return result

def IsBinaryArray(A: list[int], n: int) -> bool:
	"""
	A: A list of integers
	n: the length of A
	"""
	for i in range(n):
		if A[i] != 0 and A[i] != 1:
			return False
	return True