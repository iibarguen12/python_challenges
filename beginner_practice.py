# This is a series of examples that I done while following the CS Dojo Python course on YouTube

# 1) Arrays: Find the last positive number and then sum the rest of the negative numbers
def function_one():
    list = [7,5,4,4,3,1,-2,-3,-5,-7]
    length = len(list)
    mid = (0 + length) // 2
    while mid > 0 and mid < len(list)-1:
        if list[mid] < 0 and list[mid-1] < 0:
            mid = mid -1
        elif list[mid] > 0:
            mid = mid +1
        else:
            #last positive number
            total = sum(list[mid:length])
            break
    print(total)

# function_one()


# 2) List Comprehensions: make a lists with Python list comprehensions
def function_two():
    list = [1,4,6,8,10]
    double_list = [x * 2 for x in list]
    print(double_list)

    reverse_double = [x ** 2 for x in range(7,1,-1)] # or you can use reversed() python function

    print(reverse_double)

# function_two()


# 3) Dictionaries: make a dictionary and iterate through it
def function_three():
    dic = {}
    dic["Juan"] = 26
    dic["David"] = 28
    dic["Tefy"] = 29
    dic["Julian"] = 32

    for value, key in dic.items():
        print(value, 'tiene', key, 'años')

# function_three()


# 4) Sets: given a list, return the sum of the uniques elements
def function_four():
    list = [1,3,4,1,3,3,1,1,4,3,4,3,4,1,4]
    new_set = set(list)

    print(sum(new_set))

# function_four()

numbers=[2,1,2,3,4]
count=0
for number in numbers:
    if number % 2 == 0:
        count += 1
print(count)