# -*- coding: utf-8 -*-
"""
Created on Thu May 13 10:04:54 2021

@author: SEO
"""

import numpy as np
import pandas as pd
from collections import OrderedDict

#######################################################################
s1 = pd.core.series.Series( [1, 2, 3] )
s2 = pd.core.series.Series( ['one', 'two', 'three'] )

#df = pd.DataFrame(data=dict(num=s1, word=s2))
#print(df)

#######################################################################
friend_dict_list = [
    {'name': 'John', 'age': 25, 'job': 'student'},
    {'name': 'Nate', 'age': 40, 'job': 'teacher'},
    {'name': 'Andrew', 'age': 23, 'job': 'student'}
]

df = pd.DataFrame(friend_dict_list)
#print(df[['name', 'age', 'job']])

#######################################################################
friend_ordered_dict = OrderedDict(
    [
     ('name', ['John', 'Nate', 'Andrew']),
     ('age', [25, 40, 23]),
     ('job', ['student', 'teacher', 'student'])
    ]
)

df2 = pd.DataFrame(friend_ordered_dict)
#print(df2)

df3 = pd.DataFrame.from_dict(friend_ordered_dict)
#print(df3)

#######################################################################
friend_list = [
    ['John', 25, 'student'],
    ['Nate', 40, 'teacher'],
    ['Andrew', 23, 'student']
]

column_name = ['name', 'age', 'job']

df4 = pd.DataFrame.from_records(friend_list, columns=column_name)
#print(df4)

#######################################################################
friend_item_list = [
    ['name', ['John', 'Nate', 'Andrew']],
    ['age', [25, 40, 23]],
    ['job', ['student', 'teacher', 'student']]
]

df5 = pd.DataFrame.from_dict(dict(friend_item_list))
#print(df5)

#######################################################################


# 데이터 조회
#print(df2[1:3])
#print(df2.loc[ [0, 2] ])

# 조건을 이용한 데이터 조회
#print(df2[df2.age > 25])
#print(df2.query(('age>=25 and job=="student"')))
#print(df2[ (df2.age>=25) & (df2.job == 'student') ])

# 변수를 이용한 데이터 쿼리 조회
var_job = 'student'
var_age = 25
#print(df2.query(('age>=@var_age and job==@var_job')))

# 함수를 이용한 데이터 쿼리 조회
def max_age(x, y):
    return max(x, y)

#print(df2.query('age>=@max_age(10, 25) and job==@var_job'))

#######################################################################

# 데이터 필터
#print(df.iloc[0:2, 0:2])
#print(df[['age', 'job']])
#print(df.filter(items=['age', 'job']))
#print(df.filter(like='a', axis=1))
#print(df.filter(regex='b$', axis=1))


#######################################################################
# 칼럼 정보 추가
df['salary'] = 0
df['salary'] = np.where(df['job'] != 'student', 'yes', 'no')

#print(df)

def emotion(row):
    if row == 'yes':
        return "Thnks a lot"
    else:
        return "I need money"

df['result'] = 0
df.result = df.salary.apply(emotion)
#print(df)

df['date'] = ['2020-03-11', '2021-01-31', '2020-07-03']
def extract_year(row):
    return row.split('-')[0]

df['year'] = df['date'].apply(extract_year)
#df.year = df.date.apply(extract_year)
#print(df)

#######################################################################
# 그룹화
#df6 = pd.read_csv('./transfermarkt25.csv')

#groupby_nation = df6.groupby('nation')
#print(groupby_nation.groups)
#for nation, group in groupby_nation:
#    print(nation, ' : ', len(group))
#    print(group)
#print(groupby_nation.size())

#######################################################################
# 중복데이터 제거
person_dict_list = [
    {'name': 'John', 'age': 25, 'job': 'student', 'sex': 'male'},
    {'name': 'Nate', 'age': 40, 'job': 'teacher', 'sex': 'female'},
    {'name': 'Andrew', 'age': 23, 'job': 'student', 'sex': 'male'},
    {'name': 'Dean', 'age': 67, 'job': 'teacher', 'sex': 'male'},
    {'name': 'James', 'job': 'student', 'sex': 'female'},
    {'name': 'Andrew', 'age': 29, 'job': 'teacher', 'sex': 'male'},
    {'name': 'Andrew', 'job': 'teacher', 'sex': 'male'}
]

df7 = pd.DataFrame(person_dict_list)
#df7 = df7.drop_duplicates(['name'], keep='first')
#print(df7)

#print(df7.shape)
# NaN 찾기위한 방법
#print(df7.info())
#print(df7.isna())
#print(df7.isnull())

# NaN 값 변경
#df7.age = df7.age.fillna(0)
#df7.age.fillna(df7.groupby('job')['age'].transform('median'), inplace=True)
#print(df7)

# 데이터프레임 map 적용
df7['value'] = 0
df7.value = df7.job.map({'student':1, 'teacher':2})
#print(df7)

# 데이터프레임 전체에 map 적용
num_list = [
    [-0.7, 1.4, 2.5],
    [2.3, -1.5, 0.9],
    [1.6, 2.6, -1.1]
]
df8 = pd.DataFrame.from_records(num_list, columns=['x', 'y', 'z'])
df8 = df8.applymap(np.around)
#print(df8)


# 데이터프레임 unique 적용
job_dict_list = [
    {'name': 'John', 'age': 25, 'job': 'student', 'sex': 'male'},
    {'name': 'Nate', 'age': 40, 'job': 'developer', 'sex': 'female'},
    {'name': 'Andrew', 'age': 23, 'job': 'lawyer', 'sex': 'male'},
    {'name': 'Dean', 'age': 67, 'job': 'teacher', 'sex': 'male'},
    {'name': 'James', 'job': 'student', 'sex': 'female'},
    {'name': 'Andrew', 'age': 29, 'job': 'professor', 'sex': 'male'},
    {'name': 'Andrew', 'job': 'teacher', 'sex': 'male'},
    {'name': 'Andrew', 'job': 'banker', 'sex': 'male'},
    {'name': 'Andrew', 'job': 'designer', 'sex': 'male'},
    {'name': 'Andrew', 'job': 'developer', 'sex': 'male'},
    {'name': 'Andrew', 'job': 'student', 'sex': 'male'}
]
df9 = pd.DataFrame(job_dict_list)

#print(df9.job.unique())
#print(df9.job.value_counts())


data1_dict_list = [{'name':'John', 'job':'teacher'},
                   {'name':'Andrew', 'job':'student'},
                   {'name':'Nate', 'job':'developer'}]
data2_dict_list = [{'name':'Evan', 'job':'student'},
                   {'name':'James', 'job':'banker'},
                   {'name':'Dean', 'job':'developer'}]
data3_dict_list = [{'age':25, 'nation':'U.S'},
                   {'age':36, 'nation':'China'},
                   {'age':42, 'nation':'South Korea'}]
data4_dict_list = [{'name':'Andrew', 'age':21},
                   {'name':'John', 'age':25},
                   {'name':'Nate', 'age':30}]

# 행 합치기
df10 = pd.DataFrame(data1_dict_list, columns = ['name', 'job'])
df11 = pd.DataFrame(data2_dict_list, columns = ['name', 'job'])
df12 = pd.concat([df10, df11], ignore_index=True)
df13 = df10.append(df11, ignore_index=True)
#print(df13)

# 열 합치기
df14 = pd.DataFrame(data1_dict_list, columns = ['name', 'job'])
df15 = pd.DataFrame(data3_dict_list, columns = ['age', 'nation'])
df16 = pd.concat([df14, df15], axis=1)
#print(df16)

# 조인하여 합치기
df17 = pd.DataFrame(data1_dict_list, columns = ['name', 'job'])
df18 = pd.DataFrame(data4_dict_list, columns = ['name', 'age'])
df19 = pd.merge(df17, df18, left_on='name',right_on='name', how='inner')
#print(df19)


