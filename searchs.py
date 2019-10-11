# Differences between a linear search and a binary search (iterative and recursive)

from time import time


# Linear Search
def linear_search(data, target):
    for i in range(len(data)):
        if data[i] == target:
            return True
    return False


# Iterative Binary Search
def binary_search_iterative(data, target):
    low = 0
    high = len(data) - 1

    while low <= high:
        mid = (low + high) // 2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            high = mid-1
        else:
            low = mid+1
    return False


# Recursive Binary Search
def binary_search_recursive(data, target, low, high):
    if low > high:
        return False

    while low <= high:
        mid = (low + high) // 2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            binary_search_recursive(data, target, low, mid-1)
        else:
            binary_search_recursive(data, target, mid+1, high)


data = []
target = 2
for i in range(1):
    data.append(i)

start_time = time()
print(linear_search(data, target))
elapsed_time = time() - start_time
print('Linear Search Time:', elapsed_time, 'seconds')

print('**********************************')

start_time = time()
print(binary_search_iterative(data, target))
elapsed_time = time() - start_time
print('Iterative Binary Search Time:', elapsed_time, 'seconds')

print('**********************************')

start_time = time()
print(binary_search_recursive(data, target, 0, len(data)-1))
elapsed_time = time() - start_time
print('Recursive Binary Search Time:', elapsed_time, 'seconds')