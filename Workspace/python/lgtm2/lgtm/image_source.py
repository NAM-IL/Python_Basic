from io import BytesIO
from pathlib import Path

import requests


class LocalImage:
    """파일로부터 이미지를 얻음"""

    def __init__(self, path):
        self._path = path

    def get_image(self):
        return open(self._path, 'rb')


class RemoteImage:
    """URL로부터 이미지를 얻음"""

    def __init__(self, path):
        self._url = path

    def get_image(self):
        data = requests.get(self._url)
        # 바이트 데이터를 파일 객체로 변환
        return BytesIO(data.content)


class _LoremFlickr(RemoteImage):
    """키워드 검색으로부터 이미지를 얻음"""

    LOREM_FLICKR_URL = 'https://loremflickr.com'
    WIDTH = 800
    HEIGHT = 600

    def __init__(self, keyword):
        super().__init__(self._build_url(keyword))

    def _build_url(self, keyword):
        return (f'{self.LOREM_FLICKR_URL}/{self.WIDTH}/{self.HEIGHT}/{keyword}')


KeywordImage = _LoremFlickr


# 컨스트럭터로 이용하기 위해
# 단어를 대문자로 시작해 클래스처럼 보이도록 함
def ImageSource(keyword):
    """최적의 이미지 소스 클래스를 반환함"""
    if keyword.startswith(('http://', 'https://')):
        return RemoteImage(keyword)
    elif Path(keyword).exists():
        return LocalImage(keyword)
    else:
        return KeywordImage(keyword)


def get_image(keyword):
    """이미지 파일 객체를 반환함"""
    return ImageSource(keyword).get_image()
