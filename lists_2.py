# Returns the leader of an array

def solution(A):
    n = len(A)
    numeral = [[A.count(nb), nb] for nb in A]
    numeral.sort(key=lambda x: x[0], reverse=True)
    r = (numeral[0][1])
    if A.count(r) > n//2:
        return r
    return -1


a = [2, 2, 2, 2, 2, 4, 4, 4, 4, 4]
b = [3, 3, 3, 3, 50]
print(solution(a))
print(solution(b))

