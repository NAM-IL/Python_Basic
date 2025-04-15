import os
from webscraping import Webscrapingex01


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
        referer: https://onoffmix.com/?srsltid=AfmBOoozzSsdfepBrCgGbxsTWeHLHcs2v1mjRnBi9rTRkQ8nDIvLsp4r
        user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36 Origin and script links for profile and function calls in Performance
    """
    # target_url = 'https://onoffmix.com/event/main?s=%EA%B5%AD%EB%B9%84'
    headers = get_headers_as_dict(headers_text)
    target_url = 'https://onoffmix.com/event/main'
    params = {
        's' : '국비'
        # 's' : '%EA%B5%AD%EB%B9%84'
    }
    my_crawling = Webscrapingex01(url=target_url, params=params, headers=headers)
    scraping_data = my_crawling.get_page_data()
    # print(f"scraping_data:\n {scraping_data}")

    with open(r'file_webpage.html', 'w', encoding='utf8') as f:
        f.write(scraping_data)

    df_event = my_crawling.get_dataframe()
    print(f"df_event: \n{df_event.head()}")