import pandas as pd


class Txtdata:

    def print_filename(self):
        print(self.name)
        return self

    def print_data(self):
        print(self.data)
        return self

    def print_data_frame(self):
        print(self.data_frame)
        return self

    def __init__(self, name):
        self.name = name

    # read .txt file
    def read_file(self, enc='utf-8'):
        f = self.name
        data_map = list()
        with open(f, "r", encoding=enc) as file:
            for line in file:
                data_map.append(list(map(str, line.split())))
        self.data = data_map
        return self

    # writes data into pandas data frame format
    def to_df(self):
        data = self.data
        pd_map = list()
        for i in range(len(data)):
            tmp = list()
            for j in range(len(data[i])):
                tmp.append(data[i][j])
            pd_map.append(tmp)
        r = pd.DataFrame(pd_map)
        self.data_frame = r
        return self

    # writes pandas data frame into .csv file
    def to_csv(self, file=''):
        pd_data = self.data_frame
        if file == '':
            file = self.name
            pd_data.to_csv(file[:len(file)-4] + '.csv')
        else:
            pd_data.to_csv(file)
        return self


if __name__ == "__main__":
    a = Txtdata('test.txt')
    a.read_file()\
        .to_df()\
        .to_csv()\
        .print_data_frame()
