import pandas as pd


class Txtdata:

    # метод класса долж
    def __init__(self, data):
        self.data = data

    def read(self, f, enc='utf-8'):
        data_map = list()
        with open(f, "r", encoding=enc) as file:
            for line in file:
                data_map.append(list(map(str, line.split())))
        return (data_map)

    def to_df(self, data_arr):
        words = list()
        for i in range(len(data_arr)):
            print()
            # for j in range(len(data_arr[i])): words.append({"english": data_arr[i][j]})
        # return words


if __name__ == "__main__":
    a = Txtdata('privet')
    a_map = a.to_df(a.read('test.txt'))
    print(a)
