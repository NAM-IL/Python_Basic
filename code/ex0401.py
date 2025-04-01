import json
import os
from functools import reduce


경로1 = "/Volumes/DATA/Workspace_Python/Python_Basic/fulfillPython-main/08-built-in-functions-and-dunder-methods/interactive.ipynb"

경로들 = 경로1.split("/")

print(f"경로들:{경로들}")
print(f"확장자: {경로들[-1].split('.')[1]}")


class Mutable:
    def __init__(self, attr_map):
        # 딕셔너리의 키를 속성 이름으로 한 인스턴스 변수를 준비
        for k, v in attr_map.items():
            setattr(self, str(k), v)
            
            
def 숫자화(a):
    return int(a)


def 열배함수(x):
    return x * 10

튜플 = (1, 4, 3, 5, 2)

# map(함수자리, 이터러블객체)
# map( lambda x: x * 10, 튜플)
map( lambda x: x * 10, 튜플)


키들 = ["a", "b", "c", "d"]
벨류들 = ["a", "b", "c", "d"]
딕셔너리 = {}

for _, (k,v) in enumerate(zip(키들, 벨류들)):
    딕셔너리[k] = v
    
# join()과 조합해 쿼리 문자열을 작성
def 쿼리스트링만들기(**딕셔너러):
    keys = 딕셔너러.keys()
    values = 딕셔너러.values()
    결과 = "?" + '&'.join(
        map(lambda k, v : f'{k}={v}', keys, values)
    )

    return list(결과)
    
만들어진결과 = 쿼리스트링만들기(**딕셔너리)
print(만들어진결과)

결과문자열 = ''

for 문자열 in 만들어진결과:
    결과문자열 += 문자열
    
# print(결과문자열)

# filter
x = (1,4,3,5,2)

def 크기확인(a):
    if a > 3:
        return True
    else:
        return False
    
ret = list(filter(크기확인, x))
# print(ret)


def 누적합(a, b):
    return a+b

nums = [1, 2, 3, 4, 5]

# reduce(function, sequence[, initial])
result = reduce(lambda a, b : a + b, nums)
print(result)


class Klass:
    xx = 0

    def asdf(self):
        pass
    @classmethod
    def 필드조회_카운트(cls):
        cls.xx += 1
        
# 함수 데커레이터 이용
# @decorator
# def f():
    # pass

# decorator(f)의 반환값이 f라는 이름에 묶임
# f = decorator(f)


# 데커레이트할 함수를 받음
def deco1(f):
    print('데코레이터 호출')
    def wrapper():
        print('꾸밈 받기 전')
        v = f()  # 원래 함수를 실행
        print('꾸밈 받기 후')
        return v
    return wrapper

@deco1
def 그냥함수():
    print("exec")
    return

if __name__ == "__main__":
    # m = Mutable({'a': 1, 'b': 2})
    # print(m.b)
    
    # k =  Klass()
    # c = Klass.필드조회_카운트()
    # print(Klass.xx)
    # c = Klass.필드조회_카운트()
    # print(Klass.xx)
    그냥함수()
    pass