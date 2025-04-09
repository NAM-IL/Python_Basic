import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

class CustomPlot():
    """
        CustomPlot class
    """
    
    def __init__(self):
        # hidden attribute
        self.__verMatploLib = mpl.__version__
        self.__verNumpyLib = np.__version__
        
        # public attribute
        self.verNumpyLib = np.__version__
        self.showChart(plt)
    
    def printLibVersion(self):
        """ 
            print used lib. version
        """
        print(f'matplotlib version : {self.__verMatploLib}')
        print(f'numpy version : {self.__verNumpyLib}')
    
    # draw Line chart
    def drawLineChart(self):
        """ 
            Draw Line chart 
        """
        print("drawLineChart 함수\n")
        grade = np.array([3.71, 3.83, 3.36, 3.47, 3.67, 3.89]) # 성적 데이터
        plt.plot(grade) # 선 그래프
        self.showChart(plt)
        
    def drawBarChart(self):
        """ 
            Draw Bar chart 
        """
        print("drawBarChart 함수\n")
        # 성적 알파벳과 개수
        alphabet = np.array(['A+', 'A', 'B+', 'B', 'C+', 'C', 'D+', 'D', 'F']) 
        count = np.array([14,13,13,11,1,2,0,1,1])
        plt.bar(alphabet, count)
        self.showChart(plt)
    
    def drawScatterChart(self):
        """ 
            Draw Scatter chart : 산점도 (scatter plot)
        """
        print("drawScatterChart 함수\n")
        N, mu, sigma = 10000, 1, 0.05 #개수, 평균, 표준편차
        x = np.random.normal(mu, sigma, N) # 정규분포
        y = np.random.normal(mu, sigma, N)
        plt.scatter(x, y, alpha=0.1) # alpha는 투명도
        self.showChart(plt)
        
    def drawDonutChart(self):
        """ 
            Draw Donut chart 
        """
        print("drawDonutChart 함수\n")
        
    def subPlot(self):
        """
            Test subPlot
        """
        print("subPlot 함수\n")
    
        x = np.arange(0,5,0.1)
        y1 = np.cos(x)
        y2 = np.exp(x)
        y3 = y1 * y2
        y4 = np.sin(x)
        
        plt.title("한글 테스트")
        plt.subplot(2, 2, 1)
        plt.plot(x,y1)
        plt.title('y = cos(x)')
        
        plt.subplot(2, 2, 2)
        plt.plot(x,y2)
        plt.title('y = exp(x)')
        
        plt.subplot(2,2,3)
        plt.plot(x,y3)
        plt.title('y = cos(x)*exp(y)')
        
        plt.subplot(2,2,4)
        plt.plot(x,y4)
        plt.title('y = sin(x)')
        
        #
        self.showChart(plt)
        
    def showChart(self, curPlt):
        """ 
            Show chart 
        """
        print("showChart 함수\n")
        
        try:
            # 한글깨짐 해결(Mac)
            curPlt.rc('font', family='AppleGothic')
            # 한글깨짐 해결(Windows)
            # curPlt.rc('font', family='NanumGothic')
            
            # 그래프에서 마이너스 기호 깨짐 해결
            curPlt.rcParams['axes.unicode_minus'] = False

            curPlt.show()
        except Exception as ex:
            print(f"Exception: {ex}")
            