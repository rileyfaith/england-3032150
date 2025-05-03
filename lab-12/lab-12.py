from random import randint, seed
import time

class Sorting:
	def __init__(self, size):
		self.arr = []  # Initialize an empty list
		self.size = size

	def add(self, element):
		if len(self.arr) < self.size:
			self.arr.append(element)
		else:
			print("Array is already full, cannot add more elements.")
		
	def quicksort(self, low, high):
			if low < high:
				pi = self.partition(low, high)  # Partitioning index
				self.quicksort(low, pi-1)  # Recursively sort elements before partition
				self.quicksort(pi+1, high)  # Recursively sort elements after partition

	def partition(self, low, high):
			pivot_idx = self.median_of_three(low, high)
			self.arr[pivot_idx], self.arr[high] = self.arr[high], self.arr[pivot_idx]
			pivot = self.arr[high]

			i = low - 1
			for j in range(low, high):
				 if self.arr[j] <= pivot:
						i += 1
						self.arr[i], self.arr[j] = self.arr[j], self.arr[i]

			self.arr[i+1], self.arr[high] = self.arr[high], self.arr[i+1]
			return i + 1 

	def median_of_three(self, low, high):
			low, high = int(low), int(high)
			mid = (low + high) // 2
			a, b, c = self.arr[low], self.arr[mid], self.arr[high]

			if a < b:
				if b < c:
					return mid
				return high if a < c else low
			else:
				if a < c:
					return low
				return high if b < c else mid

def counting_sort(arr, exp):
	n = len(arr)
	output = [0]*n
	count = [0] * 10

	for num in arr:
		count[(num // exp) % 10] += 1

	for i in range(1, 10):
		count[i] += count[i - 1]

	for i in range(n - 1, -1, -1):
		digit = (arr[i] // exp) % 10
		output[count[digit] - 1] = arr[i]
		count[digit] -= 1

	arr[:] = output


def radix_sort(arr):
	if not arr:
		return
	max_num = max(arr)
	exp = 1
	while max_num // exp > 0:
		counting_sort(arr, exp)
		exp *= 10

# Test quick sorting technique
def is_sorted(arr):
	if arr == sorted(arr):
		return "Passed!"
	else:
		return "Failed!"


def test_quicksort():
	"""Test the Quicksort algorithm"""
	seed_num = 43   
	seed(seed_num)  # Set the seed for reproducibility
	sorting = Sorting(10)
	for _ in range(10):
		sorting.add(randint(1, 100))

	sorting.quicksort(0, len(sorting.arr) - 1)  # Apply the Quicksort algorithm
	print("Quick Sort:", is_sorted(sorting.arr))


# Test radix sorting technique
def test_radix_sort():
	# Test case 1
	arr1 = [234, 34, 34, 2, 1, 0, 2, 3422]
	radix_sort(arr1)
	assert arr1 == [0, 1, 2, 2, 34, 34, 234, 3422], f"Test case 1 failed: {arr1}"

	# Test case 2
	arr2 = [329, 457, 657, 839, 436, 720, 355]
	radix_sort(arr2)
	assert arr2 == [329, 355, 436, 457, 657, 720, 839], f"Test case 2 failed: {arr2}"

	# Test case 3
	arr3 = [1, 200, 3, 400, 5]
	radix_sort(arr3)
	assert arr3 == [1, 3, 5, 200, 400], f"Test case 3 failed: {arr3}"

	# Test case 4 (empty array)
	arr4 = []
	radix_sort(arr4)
	assert arr4 == [], f"Test case 4 failed: {arr4}"

	# Test case 5 (array with one element)
	arr5 = [42]
	radix_sort(arr5)
	assert arr5 == [42], f"Test case 5 failed: {arr5}"

print("All test cases passed!")

# Test case execution
test_quicksort()
# Run the test cases
test_radix_sort()


# Example usage
arr = [234, 34, 34, 2, 1, 0, 2, 3422]
radix_sort(arr)
print("Sorted array:", arr)
# Sorted array: [0, 1, 2, 2, 34, 34, 234, 3422]