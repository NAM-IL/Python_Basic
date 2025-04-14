import os
import googlemaps.client
import numpy as np
import pandas as pd
import googlemaps
from geopy.geocoders import Nominatim

def get_police_sta_data():
    print("get_police_sta_data 함수")
    dir_path = os.path.dirname(os.path.realpath(__file__))
    crime_seoul_path = f"{dir_path}/data/02. crime_in_Seoul.csv"
    print(f"crime_seoul_path : {crime_seoul_path}")
    df_crime_alal_police = pd.read_csv(crime_seoul_path, thousands=',', encoding='euc-kr')
    df_crime_data = df_crime_alal_police.head(100)
    print(f"crime_in_Seoul : {df_crime_data}")
    return df_crime_alal_police

# 위도, 경도 반환하는 함수
def geocoding(address):
    print("geocoding 함수")
    try:
        geo_local = Nominatim(user_agent='South Korea')  #지역설정
        location = geo_local.geocode(address)
        geo = [location.latitude, location.longitude]
        return geo
    except:

        return [0,0]

def add_police_sta_addr_col(dataframe):
    print("add_police_sta_addr_col 함수")
    df_new = dataframe
    sta_name_new = f"{df_new['관서명']}"[-1]+"경찰서"
    
    #[파이썬으로 위도,경도 찾기(geocoder, geocoding API, 구글 스프레드시트)](https://velog.io/@ejc9501/%ED%8C%8C%EC%9D%B4%EC%8D%AC%EC%9C%BC%EB%A1%9C-%EC%9C%84%EB%8F%84%EA%B2%BD%EB%8F%84-%EC%B0%BE%EA%B8%B0geocoder-geocoding-API-%EA%B5%AC%EA%B8%80-%EC%8A%A4%ED%94%84%EB%A0%88%EB%93%9C%EC%8B%9C%ED%8A%B8)
    geo_local = Nominatim(user_agent='South Korea')  #지역설정
    
    police_sta_addr = geo_local.geocode(sta_name_new)
    print(f"name: {police_sta_addr}, police_sta_addr: {police_sta_addr}")
    
    df_new["경찰서명"] = df_new['관서명']
    df_new["경찰서명"] = df_new["경찰서명"].apply(lambda name: f"{name}"[:-1]+"경찰서")
    df_new["주소"] = df_new["경찰서명"].apply(get_police_sta_addr) 
    
    return df_new
    
def get_police_sta_addr(police_sta_name):
    print(f"get_police_sta_addr 함수")
    # import googlemaps
    # gmaps_key = "*******************************" # 자신의 key를 사용합니다.
    # gmaps = googlemaps.Client(key=gmaps_key)
    # myloc2 = gmaps.geocode('서울중부경찰서', language="ko")
    # myloc_test = geocoder.goole(서울중부경찰서)


    #[파이썬으로 위도,경도 찾기(geocoder, geocoding API, 구글 스프레드시트)](https://velog.io/@ejc9501/%ED%8C%8C%EC%9D%B4%EC%8D%AC%EC%9C%BC%EB%A1%9C-%EC%9C%84%EB%8F%84%EA%B2%BD%EB%8F%84-%EC%B0%BE%EA%B8%B0geocoder-geocoding-API-%EA%B5%AC%EA%B8%80-%EC%8A%A4%ED%94%84%EB%A0%88%EB%93%9C%EC%8B%9C%ED%8A%B8)
    geo_local = Nominatim(user_agent='South Korea')  #지역설정
    # myloc_test = geo_local.geocode("서울중부경찰서")

    police_sta_addr = geo_local.geocode(police_sta_name)
    print(f"경찰서명: {police_sta_name}, 주소: {police_sta_addr}")
    return police_sta_addr

if __name__ =="__main__":
    # 1.
    dataframe = get_police_sta_data()

    # 2.
    df_police_sta = add_police_sta_addr_col(dataframe)
    print(f"\ndf_police_sta:\n{df_police_sta.head()}")
