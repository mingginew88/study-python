import folium


m = folium.Map(location=[37.5575, 126.9850], zoom_start=13)

# 툴팁 지정
tooltip = "Name"
folium.Marker(location=[37.5575, 126.9850], tooltip=tooltip).add_to(m)

# 맵 내 타일 형태 옵션 지정
# tiles="Stamen Terrain"

# 위치 아이콘 설정
# icon=folium.Icon(icon="cloud"), icon=folium.Icon(color="green")
# icon=folium.Icon(color="red", icon="info-sign")

# 위치 범위 지정
# radius=50,
# popup="Laurelhurst Park",
# color="#3186cc",
# fill=True,
# fill_color="#3186cc",
folium.CircleMarker(
    location=[37.5575, 126.9850],
    radius=50,
    popup="Seoul",
    color="#3186cc",
    fill=True,
    fill_color="#3186cc",
).add_to(m)


# HTML 파일로 저장
m.save("index2.html")