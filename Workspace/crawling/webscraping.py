import requests
from requests.exceptions import HTTPError
from bs4 import BeautifulSoup as bs
import json




class Webscrapingex01():

    def __init__(self, url='', params='', headers=''):
        self.url = url
        self.params = params
        self.headers = headers

    def get_data(self):
        """get web-site source code

        Returns:
            _type_: _description_
        """
        try:
            print(f"headers: {self.headers}\n")
            # 삼항 연산자
            print(f'url: {self.url}\n params is empty') if self.params == '' else print(f'url: {self.url}\n params: {self.params}')
            if (self.headers != ''):
                response = requests.get(url=self.url, headers=self.headers) if self.params == '' else requests.get(url=self.url, params=self.params, headers=self.headers)
            else:
                response = requests.get(url=self.url) if self.params == '' else requests.get(url=self.url, params=self.params)
                
            page_txt = response.text #resp.json()
            resp_code = response.status_code
            print(f"resp_code: {resp_code}")
            soup = bs(response.content, 'html.parser')
            # print(f"soup: {soup}")
        except HTTPError as Err:
            print(f'HTTP 에러: {Err}')
            return ""

        else:
            print('성공!!')

        # print(f"page_txt: {page_txt}")
        return page_txt
            

    
    