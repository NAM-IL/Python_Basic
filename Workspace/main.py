import os
from customPlot import CustomPlot
from dbtest.sqlite_example import DbHandler
from dbtest.db_ex02 import SqlalchemyKlass
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

    # ------------------------------------------- 
    dir_path = os.path.dirname(os.path.realpath(__file__))
    # file_name = "example.json"
    # file_name_csv = "ex5.csv"
    # file_name_xml = "Performance_MNR.xml"
    # file_fullpath_csv = f"{dir_path}/data/{file_name_csv}"
    # file_fullpath_xml = f"{dir_path}/data/{file_name_xml}"
    # print(f"cwd: {os.getcwd()}")
    # print(f"dir_path: {dir_path}")
    # print(f"file_fullpath_csv: {file_fullpath_csv}")
    # print(f"file_fullpath_xml: {file_fullpath_xml}")
    # myPlot.파일열기(file_fullpath_csv)
    # myPlot.serialize_obj(obj_sample)
    # myPlot.deserialize_obj(obj_sample)
    # myPlot.load_html(test_url)

    # xml_data = myPlot.load_xml(file_fullpath_xml)
    # print(f"xml_data: \n{xml_data}")

    # perf = pd.DataFrame(xml_data)
    # print(f"perf: \n {perf}")

    # [6.3 Interacting with Web APIs](https://wesmckinney.com/book/accessing-data#io_web_apis)
    # request_url = "https://api.github.com/repos/pandas-dev/pandas/issues"
    # request_url = "https://jsonplaceholder.typicode.com/posts"
    # df_data = myPlot.request_web(request_url)
    # print(f"resp_data: {df_data.head()}")

    # [6.4 Interacting with Databases](https://wesmckinney.com/book/accessing-data#io_databases)
    db_name = "mydata.sqlite"
    db_full_path = f"{dir_path}/data/{db_name}"
    print(f"db_name: {db_name}")
    print(f"dir_path: {dir_path}")
    print(f"db_full_path: {db_full_path}")
    db_handler = DbHandler()
    db_handler.connect_db(db_full_path)

    data = [("Atlanta", "Georgia", 1.25, 6),
            ("Tallahassee", "Florida", 2.6, 3),
            ("Sacramento", "California", 1.7, 5)]

    stmt = "INSERT INTO test VALUES(?, ?, ?, ?)"
    # db - Insert
    # db_handler.insert_db_data(stmt, data)

    # db - Read
    # df = db_handler.read_db_data()
    # print(f"df data - 1:\n{df.head()}")

    # SQLAlchemy 사용 예제
    db_name2 = "mydata.sqlite"
    db_full_path2 = f"{dir_path}/data/{db_name2}"
    print(f"db_full_path2:\n{db_full_path2}")
    db2 = SqlalchemyKlass(dbfullpath=db_full_path2)
    df = db2.read_db()
    print(f"df data - 2:\n{df.head()}")