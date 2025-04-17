# selenium의 webdriver를 사용하기 위한 import
from selenium import webdriver

# selenium으로 키를 조작하기 위한 import
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# 페이지 로딩을 기다리는데에 사용할 time 모듈 import
import time

import os


class CrawlingSelen():
    
    def __init__(self, option=None, target_url=''):
        self.url = target_url
        
        user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36 Origin and script links for profile and function calls in Performance"
        options = webdriver.ChromeOptions()  # Chrome 브라우저 설정 옵션 객체 생성

        # 다양한 설정 옵션 추가
        # options.add_argument('--disable-extensions')  # 확장 프로그램 사용 안함
        options.add_argument('--start-maximized')  # 창 최대화
        # options.add_argument('--incognito')  # 시크릿 모드로 실행
        # options.add_argument('--disable-gpu')  # GPU 가속 사용 안함 (★★★★★ 많이 사용)
        options.add_argument('--disable-dev-shm-usage')  # /dev/shm 사용 안함
        options.add_argument(f'--user-agent={user_agent}')  # User-Agent 설정
        options.add_argument('--disable-notifications')  # 알림 사용 안함
        
        # Google chrome closes immediately after being launched with selenium
        # https://stackoverflow.com/questions/47508518/google-chrome-closes-immediately-after-being-launched-with-selenium
        options.add_experimental_option("detach", True)

        if option == 'old':
            pass
        else:
            # 버전 135.0.7049.96(공식 빌드) (x86_64)
            # 크롬드라이버 실행
            self.driver = webdriver.Chrome(options=options)

    def __del__(self):
        self.quit()
        
    def move_start_page(self):
        # 크롬 드라이버에 url 주소 넣고 실행
        self.driver.get(self.url)
        # 페이지가 완전히 로딩되도록 3초동안 기다림
        # time.sleep(3)
        
    def sel_elements_by_class(self, by_class=None):
        if by_class is not None:
            selected_element = self.driver.find_elements(By.CLASS_NAME, by_class)
        else:
            selected_element = None
        
        return selected_element

    def sel_elements_by_xpath(self, by_xpath=None):
        if by_xpath is not None:
            selected_element = self.driver.find_elements(By.CLASS_NAME, by_xpath)
        else:
            selected_element = None

        return selected_element

    def find_element_by_xpath(self, by_xpath=None):
        if by_xpath is not None:
            print("=====")
            selected_element = self.driver.find_element(By.XPATH, by_xpath)
        else:
            selected_element = None

        return selected_element

    def move_next_page(self):
         pass

    def move_page(self):
        pass

    def click_sel_element(self, sel_element=None):
        if sel_element is not None:
            sel_element.click()
            time.sleep(3)

    def new_tap(self):
        pass

    def delay(self, seconds):
        time.sleep(seconds)

    def quit(self):
        self.driver.close()

    def move_tap(self):
        pass

    def close_tap(self):
        pass

if __name__ == "__main__":
    # Terminal을 clear
    os.system("clear")

    url = 'https://onoffmix.com/event/main?s=국비'
    mySelenCrawling = CrawlingSelen(target_url=url)
    # mySelenCrawling.delay(3)
    mySelenCrawling.move_start_page()
    found_element = mySelenCrawling.find_element_by_xpath(by_xpath='//*[@id="content"]/div/section[2]/ul/li[1]/article[1]/a/div[2]')
    # mySelenCrawling.click_sel_element(sel_element)
    print(f"type:\n {type(found_element)}")
    print(f"found_element:\n {found_element}")
    mySelenCrawling.click_sel_element(found_element)