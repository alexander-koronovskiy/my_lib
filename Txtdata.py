import pandas as pd


class Txtdata:

    # метод класса долж
    def __init__(self, data):
        self.data = data

    def read(self, enc='utf-8'):
        f = self.data
        data_map = list()
        with open(f, "r", encoding=enc) as file:
            for line in file:
                data_map.append(list(map(str, line.split())))
        self.data_map = data_map
        return self

    def to_df(self):
        data_arr = self.data_map
        print('biba')
        for i in range(len(data_arr)):
            print(data_arr[i])
        return self


if __name__ == "__main__":
    a = Txtdata('test.txt').read().to_df()
