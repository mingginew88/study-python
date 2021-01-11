from math import pi

## degree -> radian 값 변경
def degrees_to_rads(deg):
    return (deg * pi) / 180.0

### 확인
# print(degrees_to_rads(180))


## 두 집합의 차집합
def difference(a, b):
    _b = set(b)
    return [item for item in a if item not in _b]

### 확인
# print(difference([1, 2, 3], [1, 3, 4]))
