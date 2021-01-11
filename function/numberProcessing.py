
## val의 발생 횟수
def count_occurrences(lst, val):
    return len([x for x in lst if x == val and type(x) == type(val)])

### 확인
# print(count_occurrences([1, 1, 2, 1, 2, 3], 1))


## 특정 수의 자릿수 리스트화
def digitize(n):
    return list(map(int, str(n)))

### 확인
# print(digitize(56000))

