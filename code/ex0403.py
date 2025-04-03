 #모듈 패키지(pandas) 가져오기
import pandas as pd  # as pd : 별칭(as: )

# dataFilePath = r"생성형AI_교육/02_판다스/data/friend_list_no_head.csv"
dataFilePath = r"data/friend_list_no_head.csv"
# 대입 연산자 오른쪽에 있는것을 왼쪽 변수에 저장
# df - dataFrame
df = pd.read_csv(dataFilePath, encoding="utf-8")

df.head()