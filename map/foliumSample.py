import folium
import json
import pandas as pd

# json 파일 읽기
with open('./data/서울시 공공와이파이 위치정보_sample.json', 'r', encoding='utf-8') as file:
    json_data = json.load(file)

# json 파일 Dataframe
df = pd.DataFrame(json_data['DATA'])

# 위도, 경도 타입 변환
df['위도'] = pd.to_numeric(df.instl_y, errors='coerce')
df['경도'] = pd.to_numeric(df.instl_x, errors='coerce')

# 위도 중앙값
latitude = df['위도'].mean()
# 경도 중앙값
longitude = df['경도'].mean()

center = [latitude, longitude]
m = folium.Map(location=center, zoom_start=10)

for i in df.index:
    sub_lat = df.loc[i, '위도']
    sub_long = df.loc[i, '경도']

    title = df.loc[i, 'category']

    # 지도에 데이터 찍어서 보여주기
    folium.Marker([sub_lat, sub_long], tooltip=title).add_to(m)

m.save("index.html")

print('End')
