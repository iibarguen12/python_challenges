# 2019/10/09 Given a list of numbers and a number k,
# return whether any two numbers from the list add up to k.
def daily_code1(a, k):
    b = [k - num for num in a if k-num in a]
    return len(b) >0


'''a = [10, 15, 3, 7 ]
k = 17
print (daily_code1(a,k))'''

# longest common subsequence between two strings:
def daily_code2(p,q):
    r = [letter for letter in p if letter in q]
    return "".join(r)


'''p = 'BATD'
q = 'ABACD'
print(daily_code2(p,q))'''

# given an array and a number, find the number of subsets into the array which the sum be the number

#def daily_code3()


# return the factorial of a number n

# linear iteration answer:
def factorial(n):
    if n <= 1:
        return 0
    result = 1 * n
    while n > 1:
        result *= n-1
        n -= 1
    return result

# print(factorial(4))

# recursive answer:

def recursive_factorial(n):
    if n < 1:
        return 1
    else:
        return n * recursive_factorial(n-1)


# print(recursive_factorial(4))

# recursive answer:

def recursive_memoization_factorial(n):
    if n in mem:
        return mem[n]
    elif n < 1:
        return 1
    else:
        value = n * recursive_memoization_factorial(n-1)
    mem[n] = value
    return value

mem = {}
#for i in range(1,1001):
#    print("recursive_factorial:",i,":",recursive_factorial(i))
for i in range(1,100001):
    print("recursive_memoization_factorial:",i,":",recursive_memoization_factorial(i))

def fibonacci(n):
    siguiente, actual, temporal = 1, 0, 0
    if n < 3:
        return 1
    else:
        for i in range(n):
            temporal = actual
            actual = siguiente
            siguiente += temporal
        return actual

#print (fibonacci(6))

def recursive_memoization_fibonacci(n):
    if n in cached:
        return cached[n]
    elif n < 3:
        return 1
    else:
        value = recursive_memoization_fibonacci(n-1) + recursive_memoization_fibonacci(n-2)

    cached[n] = value
    return value

cached = {}
#for i in range(1,10001):
#    print(i, ":",recursive_memoization_fibonacci(i))


