import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from cctv.seoul import get_data

if __name__ == "__main__":
    dir_path = os.path.dirname(os.path.realpath(__file__))
    print(f"dir_path: {dir_path}")
    
    # 데이터 읽어오기
    data_result = get_data()
    # print(f"data: {data_result}")
    
    # 데이터 시각화
    # plt.plot(data)
    # plt.show()
    
    # plt.figure()
    # data_result['소계'].plot(kind='barh', grid=True, figsize=(10,10))
    # plt.show()
    
    fp1 = np.polyfit(data_result['인구수'], data_result['소계'], 1)
    f1 = np.poly1d(fp1)
    fx = np.linspace(100000, 700000, 100)

    data_result['오차'] = np.abs(data_result['소계'] - f1(data_result['인구수']))

    df_sort = data_result.sort_values(by='오차', ascending=False)
    df_sort.head()

    plt.figure(figsize=(14,10))
    plt.scatter(data_result['인구수'], data_result['소계'], 
                c=data_result['오차'], s=50)
    plt.plot(fx, f1(fx), ls='dashed', lw=3, color='g')

    for n in range(10):
        plt.text(df_sort['인구수'][n]*1.02, df_sort['소계'][n]*0.98, 
                df_sort.index[n], fontsize=15)
        
    plt.xlabel('인구수')
    plt.ylabel('인구당비율')
    plt.colorbar()
    plt.grid()
    
    # 한글깨짐 해결(Mac)
    plt.rc('font', family='AppleGothic')
    # 한글깨짐 해결(Windows)
    # curPlt.rc('font', family='NanumGothic')
    
    # 그래프에서 마이너스 기호 깨짐 해결
    plt.rcParams['axes.unicode_minus'] = False
            
    plt.show()