import time

## 자연수로 이루어진 수열의 합이 5인 부분 연속 수열의 갯수를 구하여라.
## 1, 2 ,3 ,2, 5 ....

start_time = time.time()
# rand_list = [1, 2, 3, 2, 5]
rand_list = [1, 2, 3, 2, 5, 3, 2, 5, 3, 1,
             4, 2, 4, 2, 1, 3, 2, 2, 1, 1,
             2, 4, 3, 2, 2, 1, 1, 1, 3, 2,
             4, 2, 1, 5, 2, 3, 4, 2, 2, 2,
             3, 1, 2, 3, 4, 2, 1, 3, 2, 5,
             2, 3, 4, 2, 3, 2, 3, 2, 3, 1]

cnt = 0

for idx, value in enumerate(rand_list):
    std_val = value
    if std_val == 5:
        cnt += 1
    for i in range(idx + 1, len(rand_list)):
        std_val += rand_list[i]
        if std_val == 5:
            cnt += 1
            break
        elif std_val < 5:
            continue
        elif std_val > 5:
            std_val = 0
            break

print('건수1 : ', cnt)
print('측정시간1 : ', time.time() - start_time)




start_time = time.time()

## 데이터 개수 : n , 구하고자 하는 합 : m
# n, m = 5, 5
n, m = 60, 5
# data = [1, 2, 3, 2, 5]
data = [1, 2, 3, 2, 5, 3, 2, 5, 3, 1,
        4, 2, 4, 2, 1, 3, 2, 2, 1, 1,
        2, 4, 3, 2, 2, 1, 1, 1, 3, 2,
        4, 2, 1, 5, 2, 3, 4, 2, 2, 2,
        3, 1, 2, 3, 4, 2, 1, 3, 2, 5,
        2, 3, 4, 2, 3, 2, 3, 2, 3, 1]


result = 0
summary = 0
end = 0

for start in range(n):
    # end를 가능한 만큼 이동
    while summary < m and end < n:
        summary += data[end]
        end += 1
    if summary == m:
        result += 1
    summary -= data[start]

print('건수2 : ', result)
print('측정시간2 : ', time.time() - start_time)







