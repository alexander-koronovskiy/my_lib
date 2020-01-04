import pandas as pd


class Series:

    # method print of the class object params:
    # filename, data, data_frame
    def __str__(self):
        return '{}\n{}'.format(self.data_frame, self.parameter)

    def __init__(self, parameter):
        self.parameter = parameter
        self.data = []
        self.data_frame = pd.DataFrame([])
        self.filename = ''

    # read .txt file - this need to file path exceptions (unique method)
    # record rows in list: "data"
    def read(self, enc='utf-8'):
        with open(self.filename, "r", encoding=enc) as file:
            self.data = [line.split() for line in file]
        return self

    # method reads list: "data" - this need to null variable exception
    # records "data" to pandas data frame format: "data_frame"
    def to_df(self):
        data = self.data
        pd_map = list()
        for i in range(len(data)):
            tmp = list()
            for j in range(len(data[i])):
                tmp.append(data[i][j])
            pd_map.append(tmp)
        r = pd.DataFrame(pd_map[1:], columns=data[0])
        self.data_frame = r
        return self

    # method reads pandas data frame format: "data_frame"
    # reads file path: "file"
    # records "data_frame" to .csv file by "file" path
    def to_csv(self, file=''):
        pd_data = self.data_frame
        if file == '':
            file = 'result.csv'
            pd_data.to_csv(file[:len(file)-4] + '.csv', index=0)
        else:
            pd_data.to_csv(file, index=0)
        return self

    # method reads list: "data"
    # records "data" to .txt file
    def to_txt(self, filename='out.txt'):
        with open(filename, 'w') as f:
            for index in self.data:
                f.write(str(index[0]) + '\n')
        return self


if __name__ == "__main__":
    a = Series(1000)
    print(a)
