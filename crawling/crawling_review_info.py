# -*- coding: utf-8 -*-
"""
Created on Mon May  3 13:59:01 2021

@author: SEO
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
from pandas import Series, DataFrame
import warnings
import numpy as np
import time
import random
import re

# header 설정
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"
}

# 상품ID
# 227331483 : 하림 IFF 닭가슴살 (냉동)
# https://www.coupang.com/vp/products/227331483?itemId=720227345&vendorItemId=4822351124&pickType=COU_PICK&q=%ED%95%98%EB%A6%BC+IFF&itemsCount=36&searchId=bf23440ee14b4be9a9c34c0b6546eeed&rank=1&isAddedCart=

# 1138891491 : 굽네 소스가 맛잇는 닭가슴살 슬라이스 화이트머쉬룸 120g x 4p + 레드크림커리 120g x 4p + 스파이시커리 120g x 4p 세트 (냉동)
# https://www.coupang.com/vp/products/1138891491?itemId=2109535018&vendorItemId=70108295142&sourceType=CATEGORY&categoryId=225417&isAddedCart=

# 346765263 : 곰곰 오리지날 닭가슴살 슬라이스 (냉동)
# https://www.coupang.com/vp/products/346765263?itemId=6256269216&vendorItemId=73551976156&sourceType=CATEGORY&categoryId=225417&isAddedCart=

# 344665368 : 하림펫푸드 더리얼 그레인프리 크런치 어덜트 강아지사료
# https://www.coupang.com/vp/products/68092?itemId=450693005&vendorItemId=4116327396&q=%EA%B7%B8%EB%A0%88%EC%9D%B8%ED%94%84%EB%A6%AC+%EC%96%B4%EB%8D%9C%ED%8A%B8+%EA%B0%95%EC%95%84%EC%A7%80%EC%82%AC%EB%A3%8C&itemsCount=36&searchId=c7c0d5c26f944be1a9d10fcc38ae4c10&rank=3&isAddedCart=

# 68092 : 나우 그레인프리 스몰브리드 어덜트 사료
# https://www.coupang.com/vp/products/68092?itemId=450693005&vendorItemId=4116327396&q=%EA%B7%B8%EB%A0%88%EC%9D%B8%ED%94%84%EB%A6%AC+%EC%96%B4%EB%8D%9C%ED%8A%B8+%EA%B0%95%EC%95%84%EC%A7%80%EC%82%AC%EB%A3%8C&itemsCount=36&searchId=c7c0d5c26f944be1a9d10fcc38ae4c10&rank=3&isAddedCart=

# 1120388104 : 내추럴발란스 어덜트 LID 닭고기 고구마 포뮬라 건식사료
# https://www.coupang.com/vp/products/1120388104?itemId=2086077016&vendorItemId=70085084389&pickType=COU_PICK&q=%EA%B7%B8%EB%A0%88%EC%9D%B8%ED%94%84%EB%A6%AC+%EC%96%B4%EB%8D%9C%ED%8A%B8+%EA%B0%95%EC%95%84%EC%A7%80%EC%82%AC%EB%A3%8C&itemsCount=36&searchId=4563fffd6def45f4ad57edc14d0d42ec&rank=0&isAddedCart=

# 62318395 : 탐사 6free 강아지 사료 연어 레시피
# https://www.coupang.com/vp/products/62318395?itemId=212802869&vendorItemId=70248727064&sourceType=CATEGORY&categoryId=445626&isAddedCart=

# 1719969991 : 외갓집 케이준 통살치킨텐더 & 소스 (냉동)
# https://www.coupang.com/vp/products/1719969991?itemId=2927391553&vendorItemId=70916014205&sourceType=srp_product_ads&q=%ED%95%98%EB%A6%BC+%EC%97%90%EC%96%B4%ED%94%84%EB%9D%BC%EC%9D%B4%EC%96%B4+%EC%88%9C%EC%82%B4%EC%B9%98%ED%82%A8&itemsCount=36&searchId=46e97cbfc85d41c3b377af971b12e7ad&rank=0&isAddedCart=

# 1119932700 : 곰곰 치킨 텐더(냉동)
# https://www.coupang.com/vp/products/1119932700?itemId=2085657339&vendorItemId=70084672842&sourceType=CATEGORY&categoryId=225417&isAddedCart=

# 116268186 : 마니커에프앤지 케이준치킨텐더 (냉동)
# https://www.coupang.com/vp/products/116268186?itemId=351198584&vendorItemId=3855800782&sourceType=CATEGORY&categoryId=225417&isAddedCart=

# 4567751809 :하림 치킨너겟 (냉동)
# https://www.coupang.com/vp/products/4567751809?itemId=5575412259&vendorItemId=72874737915&sourceType=CATEGORY&categoryId=486563&isAddedCart=

# product_list = ['227331483', '344665368', '1719969991']
product_list = ['116268186']

# 크롤링 해올 데이터 규모
size = 1

warnings.filterwarnings("ignore", category=np.VisibleDeprecationWarning)

total_start_time = time.time()  # 전체 시작 시간

for idx, product in enumerate(product_list):

    start_time = time.time()  # 시작 시간

    df = pd.DataFrame(columns=['상품명', '상품가격', '작성일자', '작성자', '리뷰내용', '리뷰평점', '도움건수', 'URL'])

    # 상품명 및 금액 Crawling
    main_url = 'https://www.coupang.com/vp/products/116268186?itemId=351198584&vendorItemId=3855800782&sourceType=CATEGORY&categoryId=225417&isAddedCart='

    response = requests.get(main_url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    product_name = soup.find('h2', {'class': 'prod-buy-header__title'})  # 상품명
    product_name = re.sub('<.+?>', '', str(product_name), 0).strip()
    product_price = soup.find('span', {'class': 'total-price'})  # 가격
    product_price = re.sub('<.+?>', '', str(product_price), 0).strip()

    # 상품평 정보 Crawling
    for cnt in range(1000):

        # time sleep 을 위한 난수
        rand_second = random.random() * 5

        url = 'https://www.coupang.com/vp/product/reviews?productId=' + product + '&page=' + str(
            cnt + 1) + '&size=' + str(size) + '&sortBy=ORDER_SCORE_ASC&ratings=&q=&viRoleCode=3&ratingSummary=true'

        response = requests.get(url, headers=headers)

        # 리뷰 정보 리스트
        review_list = [product_name, product_price]

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')

            # 작성일자
            created_date = soup.find("div", {"class": "sdp-review__article__list__info__product-info__reg-date"})
            created_date = re.sub('<.+?>', '', str(created_date), 0).strip()
            review_list.append(created_date)

            # 작성자
            writer = soup.find("span",
                               {"class": "sdp-review__article__list__info__user__name js_reviewUserProfileImage"})
            writer = re.sub('<.+?>', '', str(writer), 0).strip()
            review_list.append(writer)

            # 리뷰내용
            reviews = soup.find("div", {"class": "sdp-review__article__list__review__content"})
            reviews = re.sub('<.+?>', '', str(reviews), 0).strip()
            review_list.append(reviews)

            # 리뷰평점
            review_score = soup.find("div", {
                "class": "sdp-review__article__list__info__product-info__star-orange js_reviewArticleRatingValue"})[
                'data-rating']
            review_score = re.sub('<.+?>', '', str(review_score), 0).strip()
            review_list.append(review_score)

            # 도움건수
            helpful_cnt = soup.find("span", {"class": "js_reviewArticleHelpfulCount"})
            helpful_cnt = re.sub('<.+?>', '', str(helpful_cnt), 0).strip()
            review_list.append(helpful_cnt)

            # URL
            review_list.append(url)

            df = df.append(pd.Series(review_list, index=df.columns), ignore_index=True)

        time.sleep(rand_second)

    df.to_csv(f'C:/Users/SEO/Desktop/coupang_review_{product}.csv', encoding='utf-8-sig')

    end_time = time.time()  # 종료 시간

    print(f'{product} 걸린 시간 : ', end_time - start_time)

total_end_time = time.time()  # 전체 종료 시간

print('전체 걸린 시간 : ', total_end_time - total_start_time)