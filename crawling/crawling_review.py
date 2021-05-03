# -*- coding: utf-8 -*-
"""
Created on Mon May  3 13:59:01 2021

@author: SEO
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
import warnings
import numpy as np
import time
import random

# header 설정
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"
}

# 상품ID
product_list = ['227331483', '344665368', '1719969991']
# 상품 리뷰 건수
count_list = ['12240', '5998', '1500']
# 크롤링 해올 데이터 규모
size = 100

warnings.filterwarnings("ignore", category=np.VisibleDeprecationWarning)

total_start_time = time.time()  # 전체 시작 시간

for idx, product in enumerate(product_list):

    start_time = time.time()  # 시작 시간

    df = pd.DataFrame()
    all_cnt = int(int(count_list[idx]) / size)

    for cnt in range(all_cnt):
        # time sleep 을 위한 난수
        rand_second = random.random() * 10

        url = 'https://www.coupang.com/vp/product/reviews?productId=' + product + '&page=' + str(
            cnt + 1) + '&size=' + str(size) + '&sortBy=ORDER_SCORE_ASC&ratings=&q=&viRoleCode=3&ratingSummary=true'

        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')

            reviews = soup.findAll("div", {"class": "sdp-review__article__list__review__content"})

            df = df.append(reviews)

        time.sleep(rand_second)

    df.to_csv(f'C:/Users/SEO/Desktop/coupang_review_{product}.csv', encoding='utf-8')

    end_time = time.time()  # 종료 시간

    print(f'{product} 걸린 시간 : ', end_time - start_time)

total_end_time = time.time()  # 전체 종료 시간

print('전체 걸린 시간 : ', total_end_time - total_start_time)



