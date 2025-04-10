import os
import csv
import json
import pandas as pd

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