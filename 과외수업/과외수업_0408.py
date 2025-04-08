# import time
import pdb

# 
# time.sleep(300)

# 그 윗줄까지만 실행하고 정상 종료
# import sys
# sys.exit()


#  디버깅모드 진입
breakpoint()


# def sum(x, y):
#     z = x + y
#     return z

# a = 100
# b = 250
# c = sum(a, b)

aa = []
for i in range(0, 10):
    for j in range(0, 10):
        print(i, j)
        
        aa.append((i, j))

# 디버깅모드 진입
pdb.set_trace()

a = []

print(a)