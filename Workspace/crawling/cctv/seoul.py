import os
import pandas as pd


def get_data():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    cctv_data_path = f"{dir_path}/data/01. CCTV_in_Seoul.csv"
    pop_Seoul_path = f"{dir_path}/data/01. population_in_Seoul.xls"
    # print(f"cctv_data_path: {cctv_data_path}")
    
    cctv_seoul = pd.read_csv(cctv_data_path, encoding='utf-8')
    # cctv_seoul = pd.read_csv(cctv_data_path)
    cctv_seoul['최근증가율'] = (cctv_seoul['2016년'] + cctv_seoul['2015년'] + \
                        cctv_seoul['2014년']) / cctv_seoul['2013년도 이전']  * 100
    cctv_seoul.sort_values(by='최근증가율', ascending=False).head(5)
    # cctv_data = cctv_seoul.head()
    # print(f"cctv_data:\n {cctv_data}")
    cctv_seoul.rename(columns={cctv_seoul.columns[0] : '구별'}, inplace=True)
    cctv_data = cctv_seoul.head()
    # print(f"cctv_data:\n {cctv_data}")

    # pop_Seoul = pd.read_excel(pop_Seoul_path, encoding='utf-8')
    pop_seoul = pd.read_excel(pop_Seoul_path, header = 2, usecols = 'B, D, G, J, N')
    
    # pop_seoul.drop([0], inplace=True)
    # pop_seoul_data = pop_seoul.head()
    # print(f"pop_seoul_data:\n {pop_seoul_data}")
    pop_seoul.rename(columns={pop_seoul.columns[0] : '구별',
                          pop_seoul.columns[1] : '인구수',
                          pop_seoul.columns[2] : '한국인',
                          pop_seoul.columns[3] : '외국인',
                          pop_seoul.columns[4] : '고령자'}, inplace=True)

    pop_seoul_data = pop_seoul.head()
    # print(f"pop_seoul_data:\n {pop_seoul_data}")
    
    data_result = pd.merge(cctv_seoul, pop_seoul, on='구별')
    # print(f"data_result:\n {data_result}")
    return data_result


if __name__ == "__main__":
    get_data()