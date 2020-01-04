import Series
import pandas as pd


class Txtseries(Series):

    def __init__(self, parameter):
        super().__init__(parameter)
        self.data = []


    # read .txt file - this need to file path exceptions (unique method)
    # record rows in list: "data"

    def read(self, enc='utf-8'):
        with open(self.filename, "r", encoding=enc) as file:
            self.data = [line.split() for line in file]
        return self


if __name__ == "__main__":
    a = Txtseries('out.txt')
    a.to_df().print_data()
    print(a.data)
