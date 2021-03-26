from functools import reduce

# 피보나치 수열

# 0, 1, 1, 2, 3, 5, 8, 13, 21, ....
# 조건 : n >= 3
# n = (n - 2) + (n - 1)


# 방법1 : 재귀함수
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

#for i in range(1, 10):
#    print(fibonacci(i))


# 방법2 : List
fibonacci_list = []

for n in range(0, 10):
    if n < 2:
        fibonacci_list.append(1)
    else:
        fibonacci_list.append(fibonacci_list[n-2] + fibonacci_list[n-1])

# print(fibonacci_list)


# 방법3 : Nested List
nested_fib_list = [1, 1]
[nested_fib_list.append(nested_fib_list[i-2] + nested_fib_list[i-1]) for i in range(0, 10) if i >= 2]

# print(nested_fib_list)


# 방법4 : Nested List + Property
fib = [1, 1]
[fib.append(fib[-1] + fib[-2]) for i in range(0, 10)]
# 음수 인덱스는 가장 뒤에서부터 시작

# print(fib)


# 방법5 : Lambda
lambda_fibonacci = lambda n: n if n < 2 else lambda_fibonacci(n-1) + lambda_fibonacci(n-2)

#for i in range(1, 10):
#    print(lambda_fibonacci(i))


# 방법6 : Lambda + reduce
lambda_fib = lambda n: reduce(lambda x, n: [x[1], x[0] + x[1]], range(n), [0, 1])[0]

#for i in range(1, 10):
#    print(lambda_fib(i))
