from math import pi

## degree -> radian 값 변경
def degrees_to_rads(deg):
    return (deg * pi) / 180.0

# print(degrees_to_rads(180))


## radian -> degree 값 변경
def rads_to_degrees(rad):
    return rad * 180.0 / pi

# print(rads_to_degrees(pi / 2))

## 두 집합의 차집합
def difference(a, b):
    _b = set(b)
    return [item for item in a if item not in _b]

# print(difference([1, 2, 3], [1, 3, 4]))


## 두 집합의 교집합
def intersection(a, b):
    _a, _b = set(a), set(b)
    return list(_a & _b)

# print(intersection([1, 2, 3, 4], [2, 4, 6, 8]))


## 세 집합의 교집합
def intersection2(a, b, c):
    _a, _b, _c = set(a), set(b), set(c)
    return list(_a & _b & _c)

# print(intersection2([1, 2, 3, 4], [2, 4, 6, 8], [4, 8, 12, 16]))


## 주어진 숫자가 범위내에 있는지 확인
def in_range(n, start, end=0):
    return start <= n <= end if end >= start else end <= n <= start

# print(in_range(2, 3, 5))
# print(in_range(3, 4))


## 나누어 떨어지는지 확인
def is_divisible(divided, divisor):
    return divided % divisor == 0


## 짝수 확인
def is_even(num):
    return num % 2 == 0


## 홀수 확인
def is_odd(num):
    return num % 2 != 0


## 중앙값 추출
def median(lst):
    lst.sort()
    if len(lst) % 2 == 0:
        return (lst[int((len(lst) / 2) - 1)] + lst[int(len(lst) / 2)]) / 2
    return lst[int(len(lst) / 2)]

# print(median([1, 2, 3, 4]))

