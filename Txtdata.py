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

    def __init__(self, filename):
        self.name = filename

    # read .txt file
    # record result in a class object variable: "data"
    def read_file(self, enc='utf-8'):
        f = self.name
        data_map = list()
        with open(f, "r", encoding=enc) as file:
            for line in file:
                data_map.append(list(map(str, line.split())))
        self.data = data_map
        return self

    # method reads class object variable: "data"
    # transforms to pandas data frame format
    # into class object variable: "data_frame"
    def to_df(self):
        data = self.data
        pd_map = list()
        for i in range(len(data)):
            tmp = list()
            for j in range(len(data[i])):
                tmp.append(data[i][j])
            pd_map.append(tmp)
        print(pd_map)
        r = pd.DataFrame(pd_map)

        self.data_frame = r
        return self

    # method reads class object variable: "data_frame"
    # reads .csv file path
    # records class object variable to .csv file by the path
    def to_csv(self, file=''):
        pd_data = self.data_frame
        if file == '':
            file = self.name
            pd_data.to_csv(file[:len(file)-4] + '.csv', index=0)
        else:
            pd_data.to_csv(file, index=0)
        return self


if __name__ == "__main__":
    a = Txtdata('test.txt')
    a.read_file().to_df().print_data_frame()
