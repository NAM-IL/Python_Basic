from bs4 import BeautifulSoup as bs
import os
import json
import requests
from requests.exceptions import HTTPError
from tqdm import tqdm
import pandas as pd
import sqlite3
from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
import sqlalchemy as sqla


# [Python을 활용하여 Open API 불러오기]

class Crawling():

    def __init__(self, url='', params='', headers=''):
        self.url = url
        self.params = params
        self.headers = headers

    def get_page_data(self):
        try:
            # print(f"headers: {self.headers}\n")
            # 삼항 연산자
            # print(f'url: {self.url}\n params is empty') if self.params == '' else print(f'url: {self.url}\n params: {self.params}')
            if (self.headers != ''):
                response = requests.get(url=self.url, headers=self.headers) if self.params == '' else requests.get(url=self.url, params=self.params, headers=self.headers)
            else:
                response = requests.get(url=self.url) if self.params == '' else requests.get(url=self.url, params=self.params)
                
            # for i in tqdm(range(10000)):
            #     print(f"tqdl testing: {i}")
            page_txt = response.json() #.text #resp.json()
            resp_code = response.status_code
            print(f"resp_code: {resp_code}")

        except HTTPError as Err:
            print(f'HTTP 에러: {Err}')
            return ""

        else:
            print('성공!!')

        return page_txt

    def get_dataframe(self):
            event_name_list = []
            event_date_list = []

            try:
                # print(f"headers: {self.headers}\n")
                # 삼항 연산자
                # print(f'url: {self.url}\n params is empty') if self.params == '' else print(f'url: {self.url}\n params: {self.params}')
                if (self.headers != ''):
                    response = requests.get(url=self.url, headers=self.headers) if self.params == '' else requests.get(url=self.url, params=self.params, headers=self.headers)
                else:
                    response = requests.get(url=self.url) if self.params == '' else requests.get(url=self.url, params=self.params)

                # for i in tqdm(range(10000)):
                #     print(f"tqdl testing: {i}")
                page_txt = response.text #resp.json()
                resp_code = response.status_code
                print(f"resp_code: {resp_code}")

            except HTTPError as Err:
                print(f'HTTP 에러: {Err}')
                return ""

            else:
                print('성공!!')
                soup = bs(response.content, 'html.parser')
                # found_data = soup.find('div', class_='title ellipsis')
                # print(f"found_data: {found_data}")
                selected_event_info_list = soup.select('ul li article a div.event_info_area')
                # print(f"selected_event_info_list:\n{selected_event_info_list}")

                for event_info in selected_event_info_list:
                    # print(f"===> event_info:\n{event_info}")
                    event_name = (event_info.select('h5')[0].text).strip()
                    event_date = (event_info.select('.date')[0].text).strip()
                    print(f"===> test(event_name):\n{event_name}")
                    print(f"===> test(event_date):\n{event_date}\n\n")

                    event_name_list.append(event_name)
                    event_date_list.append(event_date)

                # print(f"event_name_list_size:{len(event_name_list)}")
                # print(f"event_data_list_size:{len(event_date_list)}")

                df_event = pd.DataFrame({'event_name': event_name_list, 'event_date': event_date_list})
                # print(f"df_event: {df_event.head()}")

            return df_event

    def save_df2db(self, dataframe):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        print(f"dir_path: {dir_path}")
        # conn = sqlite3.connect("data/mydata.db")
        engine = create_engine(f"sqlite:///{dir_path}/mydata.db")
        conn = engine.connect()
        dataframe.to_sql('event', con=conn, if_exists='replace')
        df_read = pd.read_sql("SELECT * from event", engine)
        print(f"read data form db:\n {df_read.head()}")

        return 0

def get_headers_as_dict(headers: str) -> dict:
    dic = {}
    for line in headers.split("\n"):
        if line.startswith(("GET", "POST")):
            continue
        point_index = line.find(":")
        dic[line[:point_index].strip()] = line[point_index+1:].strip()
    del dic['']
    return dic



if __name__ == "__main__":
    # Terminal을 clear
    os.system("clear")

    # dir_path = os.path.dirname(os.path.realpath(__file__))
    # target_url = 'https://section.blog.naver.com/Search/Post.nhn?pageNo=1&rangeType=ALL&orderBy=sim&keyword=%ED%8C%8C%EC%9D%B4%EC%8D%AC'
    # params = {
    #     'pageNo' : 1,
    #     'rangeType' : 'ALL',
    #     'orderBy' : 'sim',
    #     'keyword' : '파이썬'
    # }

    # my_crawling = Webscrapingex01(target_url, params=params)
    # target_url = "https://www.google.com"
    # target_url = 'https://kin.naver.com/search/list.nhn?query=%ED%8C%8C%EC?%9D%B4%EC%8D%AC'
    # target_url = 'https://wikidocs.net/135659'
    # headers_text = """
    #     Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
    #     Accept-Encoding: gzip, deflate, br, zstd
    #     Accept-Language: ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7,id-ID;q=0.6,id;q=0.5
    #     Cache-Control: max-age=0
    #     Connection: keep-alive
    #     Cookie: PHPSESSID=ud0ap9t5dsa24ecnarh119nie18jd3kb; OID=CpYCF2f97COkO9NpJBTiAg==; uid=eU7PhGf97COk++sjBD8NAg==; ch-veil-id=c1ba5371-f414-48f0-a420-19c713639995; ch-session-50540=eyJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJzZXMiLCJrZXkiOiI1MDU0MC02N2ZkZWMyNTIyNzRmNDk0YzgyOSIsImlhdCI6MTc0NDY5NTU1NSwiZXhwIjoxNzQ3Mjg3NTU1fQ.giGYIZKVUm1NePoBiI5iFOoVP_ADrNQSxA2fs3VvrSU
    #     Pragma: no-cache
    #     authority: onoffmix.com
    #     method: GET
    #     path: /event/main?s=%EA%B5%AD%EB%B9%84
    #     scheme: https
    #     priority: u=0, i
    #     referer: https://onoffmix.com/?srsltid=AfmBOoozzSsdfepBrCgGbxsTWeHLHcs2v1mjRnBi9rTRkQ8nDIvLsp4r
    #     user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36 Origin and script links for profile and function calls in Performance
    # """
    # target_url = 'https://onoffmix.com/event/main?s=%EA%B5%AD%EB%B9%84'
    # params = {
    #     's' : '국비'
    # }
    
    headers_text = """
        Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
        Accept-Encoding: gzip, deflate, br, zstd
        Accept-Language: ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7,id-ID;q=0.6,id;q=0.5
        Cache-Control: max-age=0
        Connection: keep-alive
        Cookie: PHPSESSID=ud0ap9t5dsa24ecnarh119nie18jd3kb; OID=CpYCF2f97COkO9NpJBTiAg==; uid=eU7PhGf97COk++sjBD8NAg==; ch-veil-id=c1ba5371-f414-48f0-a420-19c713639995; ch-session-50540=eyJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJzZXMiLCJrZXkiOiI1MDU0MC02N2ZkZWMyNTIyNzRmNDk0YzgyOSIsImlhdCI6MTc0NDY5NTU1NSwiZXhwIjoxNzQ3Mjg3NTU1fQ.giGYIZKVUm1NePoBiI5iFOoVP_ADrNQSxA2fs3VvrSU
        Pragma: no-cache
        authority: onoffmix.com
        method: GET
        path: /event/main?s=%EA%B5%AD%EB%B9%84
        scheme: https
        priority: u=0, i
        user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36 Origin and script links for profile and function calls in Performance
    """
    headers = get_headers_as_dict(headers_text)
  
  # [국토교통부_등산로 (XML, JSON)](https://www.data.go.kr/data/15057232/openapi.do)
    target_url = 'http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtFcst'

    key = '{인증키}'
    params_text = f"""
        ServiceKey: {key}
        pageNo: 2
        numOfRows: 1000
        dataType: JSON
        base_date: 20250416
        base_time: 1200
        nx: 55
        ny: 127
    """
    
    params = get_headers_as_dict(params_text)
    
    my_crawling = Crawling(url=target_url, params=params, headers=headers)
    page_data = my_crawling.get_page_data()
    print(f"scraping_data:\n {page_data}")

    with open(r'file_opapi_webpage.html', 'w', encoding='utf8') as f:
        f.write(page_data)

    
    # df_event = my_crawling.get_dataframe()
    # print(f"df_event: \n{df_event.head()}")
    # my_crawling.save_df2db(df_event)