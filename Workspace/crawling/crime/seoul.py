import os
import googlemaps.client
import numpy as np
import pandas as pd
import googlemaps
from geopy.geocoders import Nominatim

def get_data():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    crime_seoul_path = f"{dir_path}/data/02. crime_in_Seoul.csv"
    print(f"crime_seoul_path : {crime_seoul_path}")
    crime_alal_police = pd.read_csv(crime_seoul_path, thousands=',', encoding='euc-kr')
    crime_data = crime_alal_police.head()
    print(f"crime_in_Seoul : {crime_data}")

# 위도, 경도 반환하는 함수
def geocoding(address):
    try:
        geo_local = Nominatim(user_agent='South Korea')  #지역설정
        location = geo_local.geocode(address)
        geo = [location.latitude, location.longitude]
        return geo

    except:
        return [0,0]
    
def get_policesta_addr():
    # import googlemaps
    gmaps_key = "*******************************" # 자신의 key를 사용합니다.
    # gmaps = googlemaps.Client(key=gmaps_key)
    # myloc2 = gmaps.geocode('서울중부경찰서', language="ko")
    # myloc_test = geocoder.goole(서울중부경찰서)
    geo_local = Nominatim(user_agent='South Korea')  #지역설정
    myloc_test = geo_local.geocode("서울중부경찰서")

    myloc = [{'address_components': [{'long_name': '２７',
            'short_name': '２７',
            'types': ['premise']},
        {'long_name': '수표로',
            'short_name': '수표로',
            'types': ['political', 'sublocality', 'sublocality_level_4']},
        {'long_name': '을지로동',
            'short_name': '을지로동',
            'types': ['political', 'sublocality', 'sublocality_level_2']},        {'long_name': '중구',
            'short_name': '중구',
            'types': ['political', 'sublocality', 'sublocality_level_1']},
        {'long_name': '서울특별시',
            'short_name': '서울특별시',
            'types': ['administrative_area_level_1', 'political']},
        {'long_name': '대한민국',
            'short_name': 'KR',
            'types': ['country', 'political']},
        {'long_name': '100-032',
            'short_name': '100-032',
            'types': ['postal_code']}],
        'formatted_address': '대한민국 서울특별시 중구 을지로동 수표로 27',
        'geometry': {'location': {'lat': 37.5636465, 'lng': 126.9895796},
        'location_type': 'ROOFTOP',
        'viewport': {'northeast': {'lat': 37.56499548029149,
            'lng': 126.9909285802915},
            'southwest': {'lat': 37.56229751970849, 'lng': 126.9882306197085}}},
        'place_id': 'ChIJc-9q5uSifDURLhQmr5wkXmc',
        'types': ['establishment', 'point_of_interest', 'police']}]
    return myloc_test

if __name__ =="__main__":
    # get_data()
    loc = get_policesta_addr()
    print(f"loc: {loc}")
    

    