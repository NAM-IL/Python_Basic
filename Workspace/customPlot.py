import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

# 예제데이터 넣어주기위해
from sklearn.datasets import load_iris

# Fixing random state for reproducibility
np.random.seed(20200720)

class CustomPlot():
    """
        CustomPlot class
    """
    
    def __init__(self):
        # hidden attribute for testing
        self.__verMatploLib = mpl.__version__
        self.__verNumpyLib = np.__version__
        
        # public attribute for testing
        self.verNumpyLib = np.__version__

    def print_lib_version(self):
        """ 
            print used lib. version
        """
        print(f'matplotlib version : {self.__verMatploLib}')
        print(f'numpy version : {self.__verNumpyLib}')
    
    def draw_line_chart(self):
        """ 
            Draw Line chart 
        """
        print("drawLineChart 함수\n")
        grade = np.array([3.71, 3.83, 3.36, 3.47, 3.67, 3.89]) # 성적 데이터
        plt.plot(grade) # 선 그래프
        self.show_chart()
        
    def draw_bar_chart(self):
        """ 
            Draw Bar chart 
        """
        print("drawBarChart 함수\n")
        # 성적 알파벳과 개수
        alphabet = np.array(['A+', 'A', 'B+', 'B', 'C+', 'C', 'D+', 'D', 'F']) 
        count = np.array([14,13,13,11,1,2,0,1,1])
        plt.bar(alphabet, count)
        self.show_chart()
    
    def draw_scatter_chart(self):
        """ 
            Draw Scatter chart : 산점도 (scatter plot)
        """
        print("drawScatterChart 함수\n")
        N, mu, sigma = 10000, 1, 0.05 #개수, 평균, 표준편차
        x = np.random.normal(mu, sigma, N) # 정규분포
        y = np.random.normal(mu, sigma, N)
        plt.scatter(x, y, alpha=0.1) # alpha는 투명도
        self.show_chart()
        
    def draw_donut_chart(self):
        """ 
            Draw Donut chart 
        """
        print("drawDonutChart 함수\n")
        
    def test_subplot(self):
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
        self.show_chart()
        

    def 아이리스_시각화(self):
        """
            키워드인자방식으로
        """
        iris = load_iris(as_frame=True).frame
        print(iris)
        print(type(iris))
        # sepal:꽃받침, petal:꽃잎
        print(f'데이터의 개수는 {len(iris)}개입니다.')
        print(f'데이터에는 다음과 같은 특징이 있습니다.\n', list(iris.columns))
        print(iris.head())
        iris_type = iris['target'].value_counts().sort_index()
        print(iris_type)
        # 이제 이 내용을 시각화하면 다음과 같습니다.

        # 그냥 맵플롯이 알아서
        fig, axes = plt.subplots(1, 2, figsize=(12, 6)) # figsize는 figure의 사이즈
        axes[0].bar(iris_type.index, iris_type)
        axes[1].pie(iris_type, labels=iris_type.index, autopct='%1.1f%%')
        plt.tight_layout()
        # plt.show()

        fig, axes = plt.subplots(1, 2, figsize=(12, 6))
        axes[0].bar(iris_type.index, iris_type, color='tomato')
        axes[1].bar(iris_type.index, iris_type,
                    # ggplot2 theme : blue, red, yellow
                    color=['#00798c', '#d1495b', '#edae49']
                )
        self.show_chart()

    def 아이리스_산점도(self):
        iris = load_iris(as_frame=True).frame
        fig, axes = plt.subplots(2, 2, figsize=(12, 12))

        # Plot 1 : 아무런 정보 없이 단순한 scatter
        axes[0][0].set_title('Plot 1 : without color') # 제목 추가
        axes[0][0].scatter(x=iris['petal length (cm)'], y=iris['petal width (cm)'])


        # Plot 2 : 객체 지향 방식으로 각 target별로 plot을 한 ax에 그리기
        axes[0][1].set_title('Plot 2 : with color')
        for iris_type, color in enumerate(['#00798c', '#d1495b', '#edae49']):
            axes[0][1].scatter(x=iris[iris['target']==iris_type]['petal length (cm)'],
                            y=iris[iris['target']==iris_type]['petal width (cm)'],
                            color=color, label=f'type {iris_type}')

        # Plot 3 : 투명도를 추가하여 밀도 파악가능
        axes[1][0].set_title('Plot 3 : with color + transparency')
        for iris_type, color in enumerate(['#00798c', '#d1495b', '#edae49']):
            axes[1][0].scatter(x=iris[iris['target']==iris_type]['petal length (cm)'],
                            y=iris[iris['target']==iris_type]['petal width (cm)'],
                            color=color, label=f'type {iris_type}',
                            alpha=0.5)

        # Plot 4 : Text 정보를 추가하여 가독성 높임
        axes[1][1].set_title('Plot 4 : with color + text')
        for iris_type, color in enumerate(['#00798c', '#d1495b', '#edae49']):
            axes[1][1].scatter(x=iris[iris['target']==iris_type]['petal length (cm)'],
                            y=iris[iris['target']==iris_type]['petal width (cm)'],
                            color=color, label=f'type {iris_type}',
                            alpha=0.5)

        axes[1][1].legend(loc='upper left') # 범주 (좌측상단)
        axes[1][1].set_xlabel('length (cm)') # X축 Label
        axes[1][1].set_ylabel('width (cm)') # Y축 Label

        plt.tight_layout()
        self.show_chart()

    def show_chart(self):
        """
            Show chart
        """
        print("showChart 함수\n")

        try:
            # 한글깨짐 해결(Mac)
            plt.rc('font', family='AppleGothic')
            # 한글깨짐 해결(Windows)
            # curPlt.rc('font', family='NanumGothic')
            
            # 그래프에서 마이너스 기호 깨짐 해결
            plt.rcParams['axes.unicode_minus'] = False

            plt.show()
        except Exception as ex:
            print(f"Exception: {ex}")

    # -----------[]------------
    def plot_scatter(self, ax, prng, nb_samples=100):
        """Scatter plot.
        """
        for mu, sigma, marker in [(-.5, 0.75, 'o'), (0.75, 1., 's')]:
            x, y = prng.normal(loc=mu, scale=sigma, size=(2, nb_samples))
            ax.plot(x, y, ls='none', marker=marker)
        ax.set_xlabel('X-label')
        return ax


    def plot_colored_sinusoidal_lines(self, ax):
        """Plot sinusoidal lines with colors following the style color cycle.
        """
        L = 2 * np.pi
        x = np.linspace(0, L)
        nb_colors = len(plt.rcParams['axes.prop_cycle'])
        shift = np.linspace(0, L, nb_colors, endpoint=False)
        for s in shift:
            ax.plot(x, np.sin(x + s), '-')
        ax.set_xlim([x[0], x[-1]])
        return ax


    def plot_bar_graphs(self, ax, prng, min_value=5, max_value=25, nb_samples=5):
        """Plot two bar graphs side by side, with letters as x-tick labels.
        """
        x = np.arange(nb_samples)
        ya, yb = prng.randint(min_value, max_value, size=(2, nb_samples))
        width = 0.25
        ax.bar(x, ya, width)
        ax.bar(x + width, yb, width, color='C2')
        ax.set_xticks(x + width)
        ax.set_xticklabels(['a', 'b', 'c', 'd', 'e'])
        return ax

    def plot_colored_circles(self, ax, prng, nb_samples=15):
        """Plot circle patches.

        NB: draws a fixed amount of samples, rather than using the length of
        the color cycle, because different styles may have different numbers
        of colors.
        """
        for sty_dict, j in zip(plt.rcParams['axes.prop_cycle'], range(nb_samples)):
            ax.add_patch(plt.Circle(prng.normal(scale=3, size=2),
                                    radius=1.0, color=sty_dict['color']))
        # Force the limits to be the same across the styles (because different
        # styles may have different numbers of available colors).
        ax.set_xlim([-4, 8])
        ax.set_ylim([-5, 6])
        ax.set_aspect('equal', adjustable='box')  # to plot circles as circles
        return ax


    def plot_image_and_patch(self, ax, prng, size=(20, 20)):
        """Plot an image with random values and superimpose a circular patch.
        """
        values = prng.random_sample(size=size)
        ax.imshow(values, interpolation='none')
        c = plt.Circle((5, 5), radius=5, label='patch')
        ax.add_patch(c)
        # Remove ticks
        ax.set_xticks([])
        ax.set_yticks([])


    def plot_histograms(self, ax, prng, nb_samples=10000):
        """Plot 4 histograms and a text annotation.
        """
        params = ((10, 10), (4, 12), (50, 12), (6, 55))
        for a, b in params:
            values = prng.beta(a, b, size=nb_samples)
            ax.hist(values, histtype="stepfilled", bins=30,
                    alpha=0.8, density=True)
        # Add a small annotation.
        ax.annotate('Annotation', xy=(0.25, 4.25),
                    xytext=(0.9, 0.9), textcoords=ax.transAxes,
                    va="top", ha="right",
                    bbox=dict(boxstyle="round", alpha=0.2),
                    arrowprops=dict(
                            arrowstyle="->",
                            connectionstyle="angle,angleA=-95,angleB=35,rad=10"),
                    )
        return ax


    def plot_figure(self, style_label=""):
        """Setup and plot the demonstration figure with a given style.
        """
        # Use a dedicated RandomState instance to draw the same "random" values
        # across the different figures.
        prng = np.random.RandomState(96917002)

        # Tweak the figure size to be better suited for a row of numerous plots:
        # double the width and halve the height. NB: use relative changes because
        # some styles may have a figure size different from the default one.
        (fig_width, fig_height) = plt.rcParams['figure.figsize']
        fig_size = [fig_width * 2, fig_height / 2]

        fig, axes = plt.subplots(ncols=6, nrows=1, num=style_label,
                                figsize=fig_size, squeeze=True)
        axes[0].set_ylabel(style_label)

        self.plot_scatter(axes[0], prng)
        self.plot_image_and_patch(axes[1], prng)
        self.plot_bar_graphs(axes[2], prng)
        self.plot_colored_circles(axes[3], prng)
        self.plot_colored_sinusoidal_lines(axes[4])
        self.plot_histograms(axes[5], prng)

        fig.tight_layout()

        return fig