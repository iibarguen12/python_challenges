# Stair problem: There's a staircase with N steps, and you can climb 1 or 2 steps at a time.
# Given N, write a function that returns the number of unique ways you can climb the staircase.
# The order of the steps matters.
#
# For example, if N is 4, then there are 5 unique ways:
#
# 1, 1, 1, 1
# 2, 1, 1
# 1, 2, 1
# 1, 1, 2
# 2, 2

# Recursive solution: this is really slow (O(2^N))
def recursive_staircase(n):
    if n <= 1:
        return 1
    return recursive_staircase(n - 1) + recursive_staircase(n - 2)


# Iterative solution: faster O(N)
def iterative_staircase(n):
    a, b = 1, 2
    for _ in range(n - 1):
        a, b = b, a + b
    return a

# print(iterative_staircase(5))

# adding an X variable to be more difficult: O(N * |X|) time and O(N) space

def staircase(n, X):
    cache = [0 for _ in range(n + 1)]
    cache[0] = 1
    for i in range(1, n + 1):
        cache[i] += sum(cache[i - x] for x in X if i - x >= 0)
    return cache[n]


#stairs = 4
#X = {1, 3, 5}
#print(staircase(stairs, X))

def fib(n):
    if n in cache:
        return cache[n]
    elif n < 3:
        val = 1
    elif type(n) == int:
        val = fib(n-1) + fib(n-2)
    else:
        raise TypeError("n must be a positive int")
    cache[n] = val
    return val

cache ={}

print(fib(82))

