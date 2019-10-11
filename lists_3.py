# Failing attempt to do a segmentation of an array and return the leader
from statistics import mode


def leader(A, l):
    numeral = [[A.count(nb), nb] for nb in A]
    numeral.sort(key=lambda x: x[0], reverse=True)
    r = (numeral[0][1])
    if A.count(r) > l // 2:
        return r
    return 0


def solution(K, M, A):
    ln = len(A)
    count = 0
    i = 0
    lead = 0
    result= []
    while K < ln:
        i = count
        for item in A[count:K]:
            A[i] = A[i] +1
            i += 1
        lead = leader(A, ln)
        if lead != 0:
            result.append(lead)
        i = count
        for item in A[count:K]:
            A[i] = A[i] -1
            i += 1
        count +=1
        K +=1
    return result


A = [2, 1, 3, 1, 2, 2, 3]
M = 5
K = 3

print('ejercicio1',solution(K,M,A))

A = [1, 2, 2, 1, 2]
M = 2
K = 4

print('ejercicio2',solution(K,M,A))