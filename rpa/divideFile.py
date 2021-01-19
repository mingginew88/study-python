import pandas as pd

## 파일 불러오기
file_path = '파일경로'
file_name = '파일명'
extension_name = '.txt'

## DataFrame 처리
data = pd.read_csv(file_path + file_name + extension_name, sep='\t', encoding='UTF8')

## 기준으로 나눌 수
denominator = 10000

for i in range(int(len(data) / denominator)):
    temp_data = data[int((i-1)*denominator):int(i*denominator)]
    temp_data.to_csv(file_path + file_name + '_' + str(i) + extension_name, sep='\t', index=False)

print('End')
