# Return the smaller positive number that doesn't appear in the array
from time import time
import random


def solution1(A):
    a = frozenset(sorted(A))
    m = max(a)
    if m > 0:
        for i in range(1, m):
            if i not in a:
                return i
        return m+1
    else:
        return 1


def solution2(A):
    a = set(A)
    i = 1
    while True:
        if i in A:
            i+=1
        else:
            return i
    return i


start_time = time()
a1 = []
for i in range(1, 100000):
    a1.append(i)

elapsed_time = time() - start_time
print('Tiempo de creacion de la lista:', elapsed_time, 'segundos')

start_time = time()
a1.remove(random.randint(1, 100000))
elapsed_time = time() - start_time
print('Tiempo de eliminacion registro aleatorio:', elapsed_time, 'segundos')

a2 = [1, 3, 6, 4, 1, 2]
a3 = [1, 2, 3]
a4 = [-1, -3]
start_time = time()
print(solution1(a1))
print(solution1(a2))
print(solution1(a3))
print(solution1(a4))
elapsed_time = time() - start_time
print('Tiempo con solucion 2:', elapsed_time, 'segundos')

'''
az=[]
for i in range(1,1000000):
    az.append(i)

print(az)'''