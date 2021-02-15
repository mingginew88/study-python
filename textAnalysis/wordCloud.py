from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt



#####################################
# WordCloud Option
# font_path : 한글 깨지지 않게 글자 경로 지정
# background_color : 배경색 지정
# stopwords : 불용어 지정
#####################################

text = '파이썬이 최고 언어중에 최고 늘 짜릿해 파이썬 파이썬 파이썬이 제일이야'
# 불용어 처리
stop_words = set(STOPWORDS)
stop_words.add('파이썬')

word_cloud = WordCloud(font_path='./font/NanumGothic.ttf', stopwords=stop_words, background_color='white').generate(text)

# 사이즈 지정
plt.figure(figsize=(12, 6))
# 이미지 부드러움 정도
plt.imshow(word_cloud, interpolation='lanczos')
# x, y축 숫자 제거
plt.axis('off')
plt.show()
plt.savefig()



