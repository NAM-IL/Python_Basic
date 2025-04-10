import pandas as pd
import csv

def 파일열기(경로):
    with open(경로, encoding="utf-8", mode="r") as f:
        print(f"경로: {경로}")
        # f.readline()
        reader = csv.reader(f)
        for line in reader:
            print(line)
            
class Klass():
    
    def __init__(self):
        pass
    
    def load_csv(self, path=""):
        """
        load csv file
        Args:
            path (str, optional): _description_. Defaults to "".

        Returns:
            _type_: _description_
        """
        with open(path, encoding="utf-8", mode="r") as csvFile:
            # csvFile.readline()
            # reader = csv.reader(csvFile)
            lines = list(csv.reader(csvFile))
            header, values = lines[0], lines[1:]
            return (header, values)


if __name__ == "__main__":
    파일열기(r"./ex5.csv")