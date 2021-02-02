import time

## 소수 판단하기
start_time = time.time()

value = 23
compare_value = 2
prime = True

## 방법 1
while value > 1:
    if compare_value < value and value % compare_value == 0:
        prime = False
        break
    elif compare_value == value:
        break
    compare_value += 1

if prime is True:
    print('value is prime')
else:
    print('value is not prime')

print('수행 시간1 : ', time.time() - start_time)


## 방법 2
### 에라토스테네스의 체
start_time = time.time()
n = 1000
a = [False, False] + [True]*(n-1)
primes = []

for i in range(2, n+1):
    if a[i]:
        primes.append(i)
        for j in range(2*i, n+1, i):
            a[j] = False
print(primes)

print('수행 시간2 : ', time.time() - start_time)
