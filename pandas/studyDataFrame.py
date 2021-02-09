import numpy as np
import pandas as pd

df1 = pd.DataFrame([{'A': 2, 'B': 3, 'C': 4}, {'A': 1, 'B': 3, 'D': 8}])
# print(df1)


df2 = pd.DataFrame(np.random.rand(5, 5), columns=['A', 'B', 'C', 'D', 'E'], index=[1, 2, 3, 4, 5])
# print(df2)

male_tuple = {'서울특별시': 4720846,
              '인천광역시': 1447217,
              '대전광역시': 771040,
              '부산광역시': 1704423,
              '광주광역시': 755048}

female_tuple = {'서울특별시': 4950846,
                '인천광역시': 1507217,
                '대전광역시': 781622,
                '부산광역시': 1764420,
                '광주광역시': 770028}

male = pd.Series(male_tuple)
female = pd.Series(female_tuple)
# print(male)
# print(female)

korea_df = pd.DataFrame({'남자인구수': male, '여자인구수': female, '총인구수': male + female})
print(korea_df)
