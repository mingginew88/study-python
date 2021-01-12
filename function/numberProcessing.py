from random import randint

## val의 발생 횟수
def count_occurrences(lst, val):
    return len([x for x in lst if x == val and type(x) == type(val)])

# print(count_occurrences([1, 1, 2, 1, 2, 3], 1))


## 특정 수의 자릿수 리스트화
def digitize(n):
    return list(map(int, str(n)))

# print(digitize(56000))


## 가장 큰 값의 인덱스 추출
def max_element_index(arr):
    return arr.index(max(arr))

# print(max_element_index([1, 5, 3, 2, 4]))


## 가장 큰 순서로 값 추출
def max_n(lst, n=1):
    return sorted(lst, reverse=True)[:n]

# print(max_n([1, 2, 13, 5, 10], 2))


## 가장 작은 순서로 값 추출
def min_n(lst, n=1):
    return sorted(lst, reverse=False)[:n]

# print(min_n([1, 2, 13, 5, 10], 2))


## 최대값 추출
def max_by(lst, fn):
    return max(map(fn, lst))

# print(max_by([{'n': 4}, {'n': 2}, {'n': 6}, {'n': 8}], lambda v: v['n']))


## 최솟값 추출
def min_by(lst, fn):
    return min(map(fn, lst))


## 주어진 함수의 각 합계 추출
def sum_by(lst, fn):
    return sum(map(fn, lst))

# print(sum_by([{'n': 4}, {'n': 2}, {'n': 6}, {'n': 8}], lambda v: v['n']))

## 랜덤값 추출
def random_num(lst):
    return lst[randint(0, len(lst) - 1)]

# print(random_num([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))

