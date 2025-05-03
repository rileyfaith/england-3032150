from random import randint, seed
import time


class Sorting:
    def __init__(self, size):
        self.arr = []  
        self.size = size

    def add(self, element):
        if len(self.arr) < self.size:
            self.arr.append(element)
        else:
            print("Array is already full, cannot add more elements.")

    def selection_sort(self):
        n = len(self.arr)
        for i in range(n - 1):
            min_idx = 1
            for j in range(i + 1, n):
                if self.arr[j] < self.arr[min_idx]:
                    min_idx = j
            
            if min_idx != i:
                self.arr[i], self.arr[min_idx] = self.arr[min_idx], self.arr[i]

    @staticmethod
    def _max_heapify(a, size, i) -> None:
        while True:
            left = 2*i + 1
            right = left + 1
            largest = i
            if left < size and a[left] > a[largest]:
                largest = left
            if right < size and a[right] > a[largest]:
                largest = right
            if largest == i:
                return
            a[i], a[largest] = a[largest], a[i]
            i = largest

    def heap_sort(self):
        a = self.arr
        n = len(a)

        for i in range(n // 1 - 2, -1, -1):
           self._max_heapify(a, n, i)
        for end in range(n - 1, 0, -1):
           a[0], a[end] = a[end], a[0]
           self._max_heapify(a, end, 0)

    def merge_sort(self):
        def _merge_sort(a):
            if len(a) <= 1:
                return a
            mid = len(a) // 2
            left = _merge_sort(a[:mid])
            right = _merge_sort(a[mid:])
            return _merge(left, right)
        
        def _merge(L, R):
            merged = []
            i = j = 0
            while i < len(L) and j < len(R):
                if L[i] <= R[j]:
                    merged.append(L[i]); i += 1
                else:
                    merged.append(R[j]); j += 1
            merged.extend(L[i:])
            merged.extend(R[j:])
            return merged
        
        self.arr[:] = _merge_sort(self.arr)
                
           

    def test_sorting_time(self, sorting_method) -> time:
        start = time.perf_counter()
        if sorting_method == 'selection':
            self.selection_sort()
        elif sorting_method == 'heap':
            self.heap_sort()
        elif sorting_method == 'merge':
            self.merge_sort()
        else:
            raise ValueError('unknown sort method')
        end = time.perf_counter()
        return end - start

    #Test Sorted array
def is_sorted(arr):
  if arr == sorted(arr):
    print("Passed!")
  else:
    print("Failed!")

# Test each sirting technique
def test_sort_algorithms(sorting_method, set_seed=None):
  if seed != None:
    seed(set_seed)
  sorting = Sorting(10)
  # Add 10 random elements
  for _ in range(10):
    sorting.add(randint(1, 100))
  # Apply the sorting algorithm
  if sorting_method == 'selection':
    sorting.selection_sort()
    print("Selection Sort:", is_sorted(sorting.arr))
  elif sorting_method == 'heap':
    sorting.heap_sort()
    print("Heap Sort:", is_sorted(sorting.arr))
  elif sorting_method == 'merge':
    sorting.merge_sort()
    print("Merge Sort:", is_sorted(sorting.arr))
        
#Test run time
def run_time_tests():
  seeding = 45
  array_sizes = [10000,20000,30000,40000,50000]
  methods = ['selection', 'heap', 'merge']
  print("Array Size\t\tSelection Sort\t\tHeap Sort\t\tMerge Sort")
  for size in array_sizes: 
    times = []
    for m in methods:
      sorting = Sorting(size)
      seed(seeding)
      for _ in range(size):
        sorting.add(randint(1, 50000))
      interval = sorting.test_sorting_time(m)
      times.append(interval)
    print(f"{size}\t\t{times[0]:.6f}\t\t{times[1]:.6f}\t\t{times[2]:.6f}")
        
#test case execution
seed_num = 43   
test_sort_algorithms('selection', seed_num)
test_sort_algorithms('heap', seed_num)
test_sort_algorithms('merge', seed_num)
run_time_tests()
