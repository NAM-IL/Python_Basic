from customPlot import CustomPlot
import matplotlib.pyplot as plt

def main():
    """
        Main Function
    """
    pass

if __name__ == "__main__":
    main()
    myPlot = CustomPlot()
    # print(myPlot.__verMatploLib)
    print(myPlot.verNumpyLib)
    # myPlot.print_lib_version()
    # myPlot.draw_line_chart()
    # myPlot.draw_bar_chart()
    # myPlot.draw_scatter_chart()
    # myPlot.test_subplot()
    # myPlot.아이리스_산점도()

    # Setup a list of all available styles, in alphabetical order but
    # the `default` and `classic` ones, which will be forced resp. in
    # first and second position.
    style_list = ['default', 'classic', 'ggplot', 'fivethirtyeight', 'seaborn-whitegrid']

    myPlot.plot_figure(style_label="seaborn-whitegrid")

    # Plot a demonstration figure for every available style sheet.
    # for style_label in style_list:
    #     with plt.style.context(style_label):
    #         fig = myPlot.plot_figure(style_label=style_label)

    myPlot.show_chart()
