## 아래와 같이 N개의 정수로 구성된 수열
## M개의 쿼리 정보가 주어짐
### 각 쿼리는 L과 R로 구성
### [L, R] 구간에 해당하는 데이터들의 합을 구하시오.
### [10, 20, 30, 40, 50]

rand_list = [10, 20, 30, 40, 50]
# query_dic_list = [(1, 3), (2, 4), (1, 4), (3, 5), (3, 4)]
left = 3
right = 4
sum_val = 0
for rand_val in range(left-1, right):
    sum_val += rand_list[rand_val]
print(sum_val)


'''
for value in query_dic_list:
    sum_val = 0
    for rand_val in range(value[0] - 1, value[1]):
        sum_val += rand_list[rand_val]

    print(sum_val)
'''



## 풀이
n = 5
data = [10, 20, 30, 40, 50]

summary = 0
prefix_sum = [0]
for i in data:
    summary += i
    prefix_sum.append(summary)

left = 3
right = 4
print(prefix_sum[right] - prefix_sum[left-1])
