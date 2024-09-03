from MathHelpers import IsBinaryArray


def AddBinaryIntegers(A: list[int], B: list[int], n: int) -> list[int]:
	"""
	Take two arrays of length n, representing binary integers, and adds them together.

	-Parameters:
		A: A list of length n of 0s and 1s representing a binary integer

		B: A list of length n of 0s and 1s representing a binary integer

		n: The length of the arrays A and B

	-Returns:
		an int array of length n+1 representing a binary integer
			calculated by adding A and B together.
	"""

	if not IsBinaryArray(A, n):
		raise ValueError("Paramter A must be a binary array.")
	if not IsBinaryArray(B, n):
		raise ValueError("Parameter B must be a binary array.")

	C = [0 for i in range(n+1)]
	carry = 0
	i = n-1
	while i > -1:
		sum = A[i] + B[i] + carry
		carry = 1 if sum > 1 else 0
		C[i+1] = sum % 2
		i = i - 1
	C[i+1] = carry
	return C