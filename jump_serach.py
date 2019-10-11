import math
def jump_search(given_array, num):
    pivot = int(math.sqrt(len(given_array)))
    print(pivot)
    if num < given_array[pivot]:
        print (given_array[0:pivot] )
        pivot += pivot
    return False

a = []
for i in range(100):
    a.append(i)

print(a)
print(jump_search(a, 50))