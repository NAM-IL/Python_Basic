import requests


# from urllib import request, parse, error
# import json
# def main():
#     query = parse.urlencode({'q': 'python'})
#     # httpbin은 요청 내용을 반환해 줌
#     url = f'https://httpbin.org/get?{query}'
#     try:
#         with request.urlopen(url) as f:
#             res = f.read().decode('utf-8')
#     except error.HTTPError as e:
#         print(e)

#     return json.loads(res)

def main2():
    res = requests.get('https://httpbin.org/get',
                   params={'q': 'python'})
    return res.json()


if __name__ == "__main__":
    출력 = main2()
    print(출력)