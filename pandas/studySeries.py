import numpy as np
import pandas as pd

# 버전 확인
# print(np.__version__)
# print(pd.__version__)

# 시리즈 생성
s1 = pd.Series([0, 0.25, 0.5, 0.75, 1.0])
# print(s1)
# print(s1.index)       # 인덱스
# print(s1.values)      # 값
# print(s1[1:4])

# 시리즈 인덱스 설정
s2 = pd.Series([0, 0.25, 0.5, 0.75, 1.0], index=['a', 'b', 'c', 'd', 'e'])

# print(s2['b':'d'])            # 특정 인덱스 범위 지정
# print(s2[['b', 'e', 'd']])    # 특정 인덱스 번호 지정
# print('b' in s2)              # 특정 인덱스 여부 파악


s3 = pd.Series([0, 0.25, 0.5, 0.75, 1.0], index=[1, 2, 3, 4, 5])
# print(s3[3])            # 특정 인덱스의 해당 값 추출
# print(s3[2:])           # 특정 인덱스 이후의 값들 추출


s4 = pd.Series([0, 0.2, 0.2, 0.75, 1.0], index=[1, 2, 3, 4, 5])
# print(s4.unique())          # 유니크한 값만 추출
# print(s4.value_counts())    # 값의 갯수 추출
# print(s4.isin([0.2]))       # 값의 여부 파악


# tuple을 이용한 Series
pop_tuple = {'서울특별시': 9720846, '인천광역시': 2947217, '대전광역시': 1471040, '부산광역시': 3404423, '광주광역시': 1455048}
population = pd.Series(pop_tuple)

# print(population)
# print(population['서울특별시'])
print(population.sort_values(ascending=False)[0:3])     # value값 기준 Top3 추출




