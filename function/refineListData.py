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

print(filter_non_unique([1, 2, 3, 3, 4, 4, 5, 6]))


## 중복값이 없는 값들 필터 처리한 리스트 구성
def filter_unique(lst):
    return [item for item, count in Counter(lst).items() if count != 1]

print(filter_non_unique([1, 2, 3, 3, 4, 4, 5, 6]))


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