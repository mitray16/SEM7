import random
import time

def deterministic_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return deterministic_quick_sort(less) + [pivot] + deterministic_quick_sort(greater)

def randomized_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = random.choice(arr)
        less = [x for x in arr if x < pivot]
        equal = [x for x in arr if x == pivot]
        greater = [x for x in arr if x > pivot]
        return randomized_quick_sort(less) + equal + randomized_quick_sort(greater)

# Input from the user
user_input = input("Enter a list of numbers separated by spaces: ")
arr = list(map(int, user_input.split()))

# Measure execution time of the deterministic quick sort
start_time = time.time()
sorted_array_deterministic = deterministic_quick_sort(arr[:])
deterministic_execution_time = time.time() - start_time

# Measure execution time of the randomized quick sort
start_time = time.time()
sorted_array_randomized = randomized_quick_sort(arr[:])
randomized_execution_time = time.time() - start_time

print("Deterministic Quick Sort:")
print(f"Sorted Array: {sorted_array_deterministic}")
print(f"Execution Time: {deterministic_execution_time} seconds\n")

print("Randomized Quick Sort:")
print(f"Sorted Array: {sorted_array_randomized}")
print(f"Execution Time: {randomized_execution_time} seconds")
