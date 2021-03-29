import random

# 1. 산술평균
# N개의 수의 합을 N으로 나눈 값

list_size = int(random.randint(1, 20))
value_list = []

for i in range(0, list_size):
    value_list.append(random.randint(1, 100))

print(value_list)

print('산술평균 값 :', round(sum(value_list) / list_size, 2))

# 2. 중앙값
# N개의 수들의 증가하는 순서로 나열하였을 경우 중앙에 위치하는 값

value_list.sort()
if list_size % 2 == 0:
    print('중앙값 :', (value_list[int(list_size/2) - 1] + value_list[int(list_size/2)]) / 2)
else:
    print('중앙값 :', value_list[int(list_size/2)])


# 3. 최빈값
# N개의 수들 중 가장 많이 나타나는 값

count_list = [0] * list




# 4. 범위
