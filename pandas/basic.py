# -*- coding: utf-8 -*-
"""
Created on Wed May 12 17:56:48 2021

@author: SEO
"""

import pandas as pd

# pandas cheat sheet
# https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf 참고

df = pd.read_csv('./files/transfermarkt50.csv')

# 데이터프레임 정보 확인
#df.info()
#print(df.shape)
(rows, columns) = df.shape
#print(rows)
#print(columns)


# 데이터 상위/하위 확인 - default : 5건, head(number) 건수 지정 가능
#print(df.head())
#print(df.tail())

# 데이터 확인
#print(df[0:3])
#print(df['name'].head())
#print(df[['number', 'name', 'nation']].head())

# 인덱싱 슬라이스 - iloc, loc
#print(df.iloc[0:2]) # 뒤에있는 숫자 앞자리까지 보여줌.
#print(df.loc[0:2]) # 뒤에있는 숫자까지 포함하여 보여줌.
#print(df.loc[0, 'name'])
#print(df.loc[0:3, ['name', 'team']])

# 조건 인덱싱
#print(df[df['age'] <= 20])
#print(df[df['team'] == 'FC Barcelona'])
#print(df.loc[df['age'] > 30,['name', 'value']])

# 정렬
#print(df.sort_index(ascending=False).head())
#print(df.sort_values('age', ascending=False).head())

# 인덱스 바꾸기
#print(df.set_index('number').head())

# 칼럼명 바꾸기
df.rename(columns = {'team':'club'}, inplace=True)
#print(df)

# 데이터 전처리
df['value'] = df['value'].str.replace('€', '')
df['value'] = df['value'].str.replace('m', '').astype('float')
#print(df.info())

# 칼럼 생성
df['시장가치(억)'] = df['value']*13
#print(df)

# 칼럼 삭제
df.drop(columns=['value'], inplace=True)     # inplace로 현재 df에 적용
#print(df)

# 통계분석
#print(df.describe())
#print(df['age'].mean())
#print(df['시장가치(억)'].sum())
#print(df['nation'].mode())
#print(df[df['nation'] == 'Germany'])


g = df.groupby('nation')
#print(g.size())
#print(g.count())
#print(g.sum())
#print(g['시장가치(억)'].sum())
#print(g['age'].mean())

c = df.groupby('club')
#print(c['시장가치(억)'].sum().sort_values(ascending=False))
