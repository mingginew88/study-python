from collections import Counter

## 중복값이 없는 리스트 구성 확인
def all_unique(lst):
    return len(lst) == len(set(lst))

x = [1, 2, 3, 4, 5, 6]
y = [1, 2, 2, 3, 4, 5]

## 확인
# print(all_unique(x))
# print(all_unique(y))

## 중복값이 있는 값들 필터 처리한 리스트 구성
def filter_non_unique(lst):
    return [item for item, count in Counter(lst).items() if count == 1]

# print(filter_non_unique([1, 2, 3, 3, 4, 4, 5, 6]))


## 중복값이 없는 값들 필터 처리한 리스트 구성
def filter_unique(lst):
    return [item for item, count in Counter(lst).items() if count > 1]

# print(filter_non_unique([1, 2, 3, 3, 4, 4, 5, 6]))


## falsy 값 제거 (False, None, 0, and "")
def compact(lst):
    return list(filter(None, lst))

### 확인
# print(compact([0, 1, False, 2, '', 3, 'a', 's', 34])) ### [ 1, 2, 3, 'a', 's', 34 ]


## 리스트 좌측에서 count 만큼 제거 , n=1 은 default value
def drop(a, n=1):
    return a[n:]

### 확인
# print(drop([1, 2, 3, 4, 5], 2))


## 리스트 우측에서 count 만큼 제거 , n=1 은 default value
def drop(a, n=1):
    return a[:-n]

### 확인
# print(drop([1, 2, 3, 4, 5], 2))


## 리스트에서 nth값만 추출
def every_nth(lst, nth):
    return lst[nth - 1::nth]

# print(every_nth([1, 2, 3, 4, 5, 6, 7, 8, 9], 3))

## 리스트의 함수실행
def for_each(itr, fn):
    for el in itr:
        fn(el)

# for_each([1, 2, 3], print)


## 리스트의 마지막값 부터 함수 실행
def for_each_right(itr, fn):
    for el in itr[::-1]:
        fn(el)

# for_each_right([1, 2, 3], print)


## 리스트의 중복값이 있는경우 True, 없는경우 False 반환
def has_duplicates(lst):
    return len(lst) != len(set(lst))

x = [1, 2, 3, 3]
y = [1, 2, 3, 4]
# print(has_duplicates(x))
# print(has_duplicates(y))


## 리스트의 head 값 가져오기
def head(lst):
    return lst[0]


## 리스트의 tail 값 가져오기
def tail(lst):
    return lst[-1]


## 마지막값 제외
def initial(lst):
    return lst[0:-1]


## 주어진 범위의 리스트 구성
def initialize_list_with_range(end, start=0, step=1):
    return list(range(start, end + 1, step))

# print(initialize_list_with_range(5))
# print(initialize_list_with_range(7, 3))
# print(initialize_list_with_range(9, 4, 2))


## 주어진 값으로 채워진 리스트 구성
def initialize_list_with_values(n, val=0):
    return [val for x in range(n)]

# print(initialize_list_with_values(5, 2))


## 사전 key 값 리스트 구성
def keys_only(flat_dict):
    return list(flat_dict.keys())

# ages = {'A': 10, 'B': 8, 'C': 6}
# print(keys_only(ages))


## 사전 values 값 리스트 구성
def values_only(flat_dict):
    return list(flat_dict.values())

# ages = {'A': 10, 'B': 8, 'C': 6}
# print(values_only(ages))


## 가장 많이 쓰이는 값 추출
def most_frequent(lst):
    return max(set(lst), key=lst.count)

# print(most_frequent([1, 2, 1, 1, 3, 3, 2, 2, 4, 2]))


## 주어진 개수를 리스트의 끝으로 구성
def offset(lst, offset):
    return lst[offset:] + lst[:offset]

# print(offset([1, 2, 3, 4, 5], 2))


## 두 리스트의 중복 값 반환
def similarity(a, b):
    return [item for item in a if item in b]

# print(similarity([1, 3, 5, 6], [1, 2, 3, 4]))


## 두 리스트 중 하나라도 존재하는 값 반환
def union(a, b):
    return list(set(a + b))

# print(union([1, 2, 3], [1, 3, 4]))


## 주어진 리스트의 중복값 제외한 리스트 반환
def unique_elements(lst):
    return list(set(lst))

# print(unique_elements([1, 2, 3, 2, 5, 6, 3, 1]))


## n개의 값으로 리스트 구성
def take(itr, n=1):
    return itr[:n]


## 리스트의 끝에서부터 n개의 값으로 리스트 구성
def take_right(itr, n=1):
    return itr[-n:]