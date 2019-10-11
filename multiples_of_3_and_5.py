# given a range of two numbers min and max, print 'Fizz' for each multiple of 3,
# print 'Buzz' for each multiple of 5 and print 'FizzBuzz' for each multiple of 3 and 5 at time

def linear_solution(min, max):
    for i in range(min,max):
        if i % 3 == 0 and i % 5 == 0:
            print(i,':', 'FizzBuzz')
        elif i % 3 == 0:
            print(i, ':', 'Fizz')
        elif i % 5 == 0:
            print(i, ':', 'Buzz')


linear_solution(1,100)
