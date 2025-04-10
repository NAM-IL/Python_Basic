import os
from customPlot import CustomPlot
import matplotlib.pyplot as plt
import pandas as pd

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
    # style_list = ['default', 'classic', 'ggplot', 'fivethirtyeight', 'seaborn-whitegrid']

    # myPlot.plot_figure(style_label="seaborn-whitegrid")

    # Plot a demonstration figure for every available style sheet.
    # for style_label in style_list:
    #     with plt.style.context(style_label):
    #         fig = myPlot.plot_figure(style_label=style_label)

    # myPlot.show_chart()

    test_url = "https://mizykk.tistory.com/39"
    obj_sample = """
    {"name": "Wes",
    "cities_lived": ["Akron", "Nashville", "New York", "San Francisco"],
    "pet": null,
    "siblings": [{"name": "Scott", "age": 34, "hobbies": ["guitars", "soccer"]},
                {"name": "Katie", "age": 42, "hobbies": ["diving", "art"]}]
    }
    """

    dir_path = os.path.dirname(os.path.realpath(__file__))
    # file_name = "example.json"
    file_name_csv = "ex5.csv"
    file_name_xml = "Performance_MNR.xml"
    file_fullpath_csv = f"{dir_path}/data/{file_name_csv}"
    file_fullpath_xml = f"{dir_path}/data/{file_name_xml}"
    print(f"cwd: {os.getcwd()}")
    print(f"dir_path: {dir_path}")
    # print(f"file_fullpath_csv: {file_fullpath_csv}")
    print(f"file_fullpath_xml: {file_fullpath_xml}")
    # myPlot.파일열기(file_fullpath_csv)
    # myPlot.serialize_obj(obj_sample)
    # myPlot.deserialize_obj(obj_sample)
    # myPlot.load_html(test_url)

    xml_data = myPlot.load_xml(file_fullpath_xml)
    # print(f"xml_data: \n{xml_data}")

    perf = pd.DataFrame(xml_data)
    print(f"perf: \n {perf}")