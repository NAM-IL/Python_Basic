from datetime import datetime

# Optional은 None의 가능성이 있을 때 이용함
from typing import Optional

# 04-data-structures
def ex01():
    # 순서가 없으므로 인덱스를 이용해 참조할 수 없음
    items = {'note', 'notebook', 'sketchbook'}
    items.pop()
    print(items)

    number = [ str(v) for v in range(10)]
    print(number)

    number = [ 
              str(v) for v in range(10) if v % 2 == 0
             ]
    print(number)

    리스트 = [(lambda item:item*2) for item in range(0, 10)]
    print(리스트)

    def 복잡한함수(item):
        return item*2

    리스트 = [(lambda item:item*2)(item) for item in range(0, 10) if item % 2 == 0]
    print(리스트)

    리스트2 = [(x, y) for x in [1, 2, 3] for y in [4, 5, 6]]
    print(리스트2)


# 05-functions
def ex02():
    pass
    # 실인수
    
    





# 기본값의 잘못된 사용 예시
# def print_page(content, timestamp=datetime.now()):
def print_page(content, timestamp=None):
    if timestamp is None:
        timestamp = datetime.now()
    print(content)
    print(timestamp)


# 첫 번째 인수의 함수가 참이 되는 것만 남음
def asdf(x):
    if len(x) == 3:
        return x

# 맵은 컨테이너 객체가 들어가서 같은 크기의 객체가 나옴

# 필터는 통과하고 나면 크기가 줄어든다.
# True 인것만 모아서 새로운 객체를 만들어 준다.

nums = range(0, 10)
filtered = filter(lambda x : x ==3, nums)
print(type(filtered))
print(list(filtered))



def increment(
    page_num: int,
    last: int,
    *,
    ignore_error: bool = False) -> Optional[int]:
    next_page = page_num + 1
    if next_page <= last:
        return next_page
    if ignore_error:
        return None
    raise ValueError('Invalid arguments')


if __name__ == "__main__":
    # pass
    # ex01()
    # ex02()
    # print_page("hello")
    anno = increment.__annotations__  # 타입 정보가 저장되어 있음
    print(anno)