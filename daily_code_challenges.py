# 1) Given a list of numbers and a number k,
# return if any two numbers from the list can add up to k.

# Iterative O(N) Solution
def daily_code_sum_list(a, k):
    b = [k - num for num in a if k-num in a]
    return len(b) > 0

'''
a = [10, 15, 3, 2, 2 ]
k = 17
print (daily_code_sum_list(a,k))
'''
# Now return the number of sets that add to K, for that lest look second solution using memoization
def dp(arr, total, i, mem):
    key = str(total)+":"+str(i)
    if key in mem:
        return mem[key]
    if total == 0:
        return 1
    elif total < 0:
        return 0
    elif i < 0:
        return 0
    elif total < arr[i]:
        to_return = dp(arr, total, i-1, mem)
    else:
        to_return = (dp(arr, total-arr[i], i-1, mem)+dp(arr, total, i-1, mem))
    mem[key] = to_return
    return to_return

def count_sets_dp(arr,total):
    mem = {}
    return dp(arr, total, len(arr)-1, mem)

'''
print (count_sets_dp(a,k))
'''


# 2) Given a list of numbers and a number k,
# return true if the multiplication of any two numbers from the list can be k.

# Iterative O(N) Solution
def daily_code_multiply(a, k):
    b = [num for num in a if k/num in a]
    return len(b) >0
'''
a = [10, 15, 3, 7,10, 2 ]
k = 20
print (daily_code_multiply(a,k))
'''


# 3) return the factorial of a number n

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

# recursive memoization answer:

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
#for i in range(1,100001):
#    print("recursive_memoization_factorial:",i,":",recursive_memoization_factorial(i))

# 4) make a fibonacci series

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

# recursive memoization solution:
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

# 5) Given a number, find the number of possible pairs of letters which can be add to make the number
# keep in mind that each letter have a value, a is equal to 1, b to 2, c to 3 and so
# for example given the number 12 the output will be "ab" or "l" because a=1, b=2 or l=12

def num_helper(data,k,memo):
    if k == 0:
        return 1
    s = len(data) - k
    if data[s] == 0:
        return 0
    if memo[k] != 0:
        return memo[k]
    result = num_helper(data,k-1,memo)
    if k >= 2 and int(data[s:s+2]) <= 26:
        result+= num_helper(data, k-2, memo)
    memo[k] = result
    return result

def num_to_letters(data):
    memo = [0]*(len(data)+1)
    return num_helper(data, len(data), memo)


#print(num_to_letters('111111'))


# 6) given a number of stairs draw a stair of #

def staircase(num_stairs):
    for stairs in range(1, num_stairs + 1):
        print(('#' * stairs).rjust(num_stairs))

#staircase(10)


# 7 ) given a N number of stairs return the number of ways you can go up through the stair
# by 1 or 2 steps:
# for example if N = 4 the number of ways is 5

# for the first solution, we use recursive and memoization approach O(2N) = O(N):

def num_ways(n, memo):
    if n <= 1:
        return 1
    if n in memo:
        return memo[n]
    else:
        result = num_ways(n-1,memo)+num_ways(n-2,memo)
    memo[n]= result
    return result
'''
memo={}
print('memoization:',num_ways(9,memo))
print(memo)
'''

# For second solution for a stair problem, we using bottom up method O(N):

def num_ways_bottom_up(n):
    if n == 0 or n == 1:
        return 1
    nums = [0]*(n+1)
    nums[0], nums[1] = 1, 1
    for i in range(2, n+1):
        nums[i] = nums[i-1] + nums[i-2]
    return nums[n]


#print('bottom up:',num_ways_bottom_up(9))


# Now imagine that you only can step up by X numbers, this is a O(NlogN)
# because de sort() method use O(NlogN) and the rest of the algorithm is linear

def num_ways_X_bottom_up(n,X):
    if n == 0:
        return 1
    nums = [0]*(n+1)
    nums[0] = 1
    X.sort()
    for i in range(1, n+1):
        total = 0
        for j in X:
            if i-j >= 0:
                total += nums[i-j]
        nums[i] = total
    return nums[n]

'''
X = [1, 3, 5]
print('bottom up X ways:',num_ways_X_bottom_up(4,X))
'''

# 8 ) return the ways to represent N as sum of 1, 3 and 4
def sumCountWays(n):
    DP = [0 for i in range(0, n + 1)]

    # base cases
    DP[0] = DP[1] = DP[2] = 1
    DP[3] = 2

    # Iterate for all values from 4 to n
    for i in range(4, n + 1):
        DP[i] = DP[i - 1] + DP[i - 3] + DP[i - 4]

    return DP[n]

'''
# Driver code
n = 10
print(sumCountWays(n))
'''


# 9 ) given an array of numbers, add 1 to the last number of the array, if the result is greater than 9,
# the number will be 0 and the number at the left will be the number plus 1 and so

# solution one is an iterative solution, not much efficient O(A+B)
# where A and B are the length of the array:
def add_one_to_array(a):
    tot = ''
    for num in a:
        tot +=str(num)
    tot = int(tot)+1
    tot = [int(num) for num in str(tot)]
    return tot

#a=[1,2,3,4,5]  #[n for n in range(1,100000)]
#print(add_one_to_array(a))


# solution two with recursive programming O(N):
def add_one_recursive(a, n):
    if a[n-1] == 9:
        a[n-1] = 0
        if n-1 > 0:
            add_one_recursive(a, n-1)
        else:
            a = [0]*(len(a)+1)
            a[0] = 1
    else:
        a[n - 1] = a[n - 1] +1
    return a

'''
a=[1,2,3,4,5]
print(add_one_recursive(a, len(a)))
'''

# 10) return the smallest K numbers in an array

# sorting solution O(NlogN):
def sorting_smallers(n):
    return sorted(n)[0:3]

'''
a = [4,1,5,2,3,0,10]
print(sorting_smallers(a))
'''

import heapq
# heapq solution O(logN):
def heapq_smallers(n):
    heapq.heapify(n)
    return heapq.nsmallest(3,n)

'''
a = [4,1,5,2,3,0,10]
print(heapq_smallers(a))
'''

# 11) Given an array of integers, find the first missing positive integer in linear time
# and constant space. In other words, find the lowest positive integer that does not exist
# in the array. The array can contain duplicates and negative numbers as well.
#
# For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.
#
# You can modify the input array in-place.

# Iterative linear solution O(N) + sort() method O(NlogN) = O(NlogN):

def lowest_missing_int(arr):
    arr.sort()
    count = 0
    for i in range(0,len(arr)):
        if arr[i] > 0:
            count +=1
            if count not in arr:
                return count
    return count+1
'''
arr = [3, -4, -1, -1]
print('Result of the fisrt function: %s'%lowest_missing_int(arr))
'''

# second possible solution for the problem in a O(N) too

def lowest_missing_int_2(arr):
    result = [num for num in range(1, len(arr)) if num not in arr]
    if result == []:
        result.append(max(arr)+1)
    return result[0]
'''
print('Result of the second function: %s'%lowest_missing_int_2(arr))
'''

# 12) given a list of tuples which each one has a coordinates of locations,
# return the K closest points to the origin
# The euclidean distance between these two points will be: √{(x2-x1)2 + (y2-y1)2}
# O(NlogN)
def closest_points(points, K):
    points.sort(key=lambda K: K[0] ** 2 + K[1] ** 2)

    return points[:K]

'''
points = [[3, 3], [5, -1], [-2, 4], [1,4]]
K = 1
print(closest_points(points, K))
'''
# 13) return the longest common subsequence between two strings for example P = 'BATD' and q = 'ABACD'
# will return 'BAD':
def daily_code_subsequence(p,q):
    r = [letter for letter in p if letter in q]
    return "".join(r)


'''p = 'BATD'
q = 'ABACD'
print(daily_code_subsequence(p,q))'''

# 14) given a string of letters, return the FIRST repeated character of the string
# complex O(N)

def recurring_chr(str):
    existents = {}
    for n in str:
        if n in existents:
            return n
        else:
            existents[n] = 1
    return None

'''
str_in = 'ABCRGETA'
print(recurring_chr(str_in))
'''

# 15) Given a string, return the MOST repeated character

# First solution O(N):

str_in = "AABCDDBBBEA"

def most_repeated(str):
    letters = {}
    las_letter = ''
    for letter in str:
        if letter in letters:
            if letter == las_letter:
                letters[letter] = int(letters.get(letter)) +1
            else:
                letters[letter] = 1
        else:
            letters[letter] = 1
        las_letter = letter

    return max(letters, key=letters.get)
'''
print(most_repeated(str_in))
'''

# Second solution O(N):

def most_repeated_2(str):
    count = 0
    max_count = 0
    max_chr = ''
    previus_chr = ''
    for current in str:
        if previus_chr == current:
            count += 1
        else:
            count = 1
        if count > max_count:
            max_count = count
            max_chr = current
        previus_chr = current
    return {max_chr: max_count}
'''
print(most_repeated_2(str_in))
'''

# 16) Find the number of negative numbers in a column-wise / row-wise
# sorted matrix M[][]. Suppose M has n rows and m columns.
# Example:
#
# Input:  M =  [-3, -2, -1,  1]
#              [-2,  2,  3,  4]
#              [4,   5,  7,  8]
# Output : 4

# the first solution, is a brute force solution with O(n*m)
def countNegative(M, n, m):
    count = 0

    for i in range(n):
        for j in range(m):
            if M[i][j] < 0:
                count += 1
            else:
                break
    return count

# the second solution is mor optimal and takes O(n+m)

def countNegativeM(M,n,m):

    count = 0
    i = 0      # rows
    j = m - 1  # columns

    while j > 0 and i < n:
        if M[i][j] <0:
            count += (j+1)
            i += 1
        else:
            j -= 1
    return count

'''
M = [
      [-3, -2, -1,  1],
      [-2,  2,  3,  4],
      [4,   5,  7,  8]
    ]

print(countNegative(M, 3, 4))
print(countNegativeM(M, 3, 4))
'''

# 17) Return the possible subsets in an array
# for example: [1,2] should return [[], [1], [2], [1, 2]]

def getsubsets(inputset, n):
    temparr = []
    for i in range(len(inputset)):
        if i == 0:
            temparr.append([])
            temparr.append([inputset[0]])
        else:
            copy = temparr[:]
            for x in copy:
                temparr.append(x+[inputset[i]])
    return(temparr)

'''
myset = [1,2]
subsets = getsubsets(myset,len(myset)-1)
print(subsets)
'''

# 18) Find the Lowest Common Ancestor in a tree
# first we have to create a class for the tree

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

# Solution one:
# Now we make a function to return the path from the root to the element (the path in the tree to find X)

def pathToX(root, path, X):
    if root is None:
        return False

    path.append(root.key)

    if root.key == X:
        return True

    if ((root.left != None and pathToX(root.left, path, X)) or
            (root.right!= None and pathToX(root.right, path, X))):
        return True

    path.pop()
    return False


# Returns LCA if node n1 , n2 are present in the given
# binary tree otherwise return -1
def findLCA(root, n1, n2):

    path1 = []
    path2 = []

    if not pathToX(root, path1, n1) or not pathToX(root, path2, n2):
        return -1

    i = 0
    while i < len(path1) and i < len(path2):
        if path1[i] != path2[i]:
            break
        i += 1
    return path1[i - 1]

# test the function:
'''
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print("LCA(4, 5) = %d" % (findLCA(root, 4, 5, )))
print("LCA(4, 6) = %d" % (findLCA(root, 4, 6)))
print("LCA(3, 4) = %d" % (findLCA(root, 3, 4)))
print("LCA(2, 4) = %d" % (findLCA(root, 2, 4)))
'''

# Solution two: recursive solution in O(N)

def findLCA2(root, n1, n2):
    if root == None:
        return None
    if root.key == n1 or root.key == n2:
        return root

    left = findLCA2(root.left,n1,n2)
    right = findLCA2(root.right,n1,n2)

    if left != None and right != None:
        return root
    if left == None and right == None:
        return None

    return left if left is not None else right

    # test the function:
'''
root2 = Node(3)

root2.left = Node(6)
root2.left.left = Node(2)
root2.left.right = Node(11)
root2.left.right.left = Node(9)
root2.left.right.right = Node(5)

root2.right = Node(8)
root2.right.right = Node(13)
root2.right.right.left = Node(7)
lca_node = findLCA2(root2, 8, 7)
print("Result:",lca_node.key)

'''


# 19) Find the maximum sub array in an array

# First we make an slow solution with iterative answer O(N^2)

def max_subarr_iterative(input_array):
    global_max = 0
    indices = []
    for x in range(len(input_array)+1):
        for j in range(len(input_array)+1):
            if input_array[x:j]:
                current_max = sum(input_array[x:j])
                if current_max > global_max:
                    global_max = current_max
                    indices.append((input_array[x], input_array[j-1]))
    if len(indices) == 0:
        indices.append(max(input_array))
        global_max = sum(indices)
    return global_max, indices.pop()
'''
a =[-17, -3, -2, -1]
print("The maximum sum is: %s from the sub array %s "%(max_subarr_iterative(a)))
'''

# lets take a look at other answer using dynamic programming  O(N)

def maxSubArraySum(a, size):
    max_so_far = a[0]
    curr_max = a[0]

    for i in range(1, size):
        curr_max = max(a[i], curr_max + a[i])
        max_so_far = max(max_so_far, curr_max)

    return max_so_far

'''
a = [-2, -3, -4, -1, -2, 4, -5, -3]
print("Maximum contiguous sum is" , maxSubArraySum(a,len(a)))
'''

# 20) Reorder an array in a random order in O(N) only using random(0,1) and floor method:
import math
import random
def reorder(a):
    n = len(a)
    for i in range(n-1, 1,-1):
        pick = math.floor((i+1)*random.random())
        temp = a[pick]
        a[pick] = a[i]
        a[i] = temp

'''
a = [1,2,3,4,5,6,7,8]
print(a)
reorder(a)
print('='*30)
print(a)
'''



# 21) Tower Hopper Problem: given an array of integers that represents the high of the towers
# in each position, and express how far we can jump from a certain tower, we have to return whether
# there's a way to get from tower[0] (0 indexed) to outside of the array.

def is_hoppable(towers):
  current = 0
  while True:
    if current >= len(towers):
      return True
    if towers[current] == 0:
      return False
    current = next_steps(current, towers)

def next_steps(i, _towers):
  start = i +1
  finish = i + _towers[i] +1
  if finish >= len(_towers): return finish
  towers = _towers[start:finish]
  m = 0
  for (index, value) in enumerate(towers):
    if towers[index] >= towers[m]:
      m = index
  return m + start

'''
towers = [4,2,0,1,2,0]
print(is_hoppable(towers))
'''

# 22) Iterative Letter Combinations of a Phone Number
# Given an integer array containing digits from [0, 9], the task is to print all possible
# letter combinations that the numbers could represent.
# A mapping of digit to letters (just like on the telephone buttons)
# 2="abc", 3="def", 4="ghi", 5="jkl", 6="mno", 7="pqrs", 8="tuv", 9="wxyz"

def letterCombinations(number):
    table = ["", "", "abc", "def", "ghi", "jkl",
             "mno", "pqrs", "tuv", "wxyz"]

    list = []
    temporal_list = []
    numbers = [int(x) for x in str(number)]
    n = len(numbers)
    temporal_list.append("")

    while len(temporal_list) != 0:
        s = temporal_list.pop()

        if len(s) == n:
            list.append(s)
        else:

            for letter in table[numbers[len(s)]]:
                temporal_list.append(s + letter)

    return list


number = 23
print(letterCombinations(number))
