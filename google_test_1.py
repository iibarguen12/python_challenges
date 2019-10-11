# given an array of numbers between 0 and 9, add 1 to the las item of the array, if the result of that
# sum is 10, then put 0 and add one to the next item at the left

import random
from time import time

def add_one(given_array):
    str_num = "".join(str(e) for e in given_array)
    nex_num = int(str_num) + 1
    ret_arr = []
    for num in str(nex_num):
        ret_arr.append(int(num))
    return ret_arr


def add_one_v2(given_array):
    carry = 1
    result = [0]* (len(given_array))
    for i in reversed(range(len(given_array))):
        total = given_array[i] + carry
        if total == 10:
            carry = 1
        else:
            carry = 0
        result[i] = total % 10
    if carry == 1:
        result = [0]* (len(given_array) +1)
        result[0] = 1
    return result

a = []
for i in range(1000000):
    a.append(random.randint(0,9))

print(a[len(a)-5:len(a)])

inicio = time()
resutlt_1 = add_one(a)
fin = time() - inicio
print(resutlt_1[len(a)-5:len(a)])
print('timepo v1:',fin)

inicio = time()
resutlt_2 = add_one_v2(a)
fin = time() - inicio
print(resutlt_1[len(a)-5:len(a)])
print('timepo v2:',fin)
