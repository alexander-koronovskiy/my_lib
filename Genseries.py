import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


class Genseries_1d:

    ############################################
    # methods print of the class object params:
    # filename, data, data_frame
    ############################################

    def print_number_of_points(self):
        print(self.points)
        return self

    def print_data(self):
        print(self.data)
        return self

    def print_data_frame(self):
        print(self.data_frame)
        return self

    ###############################################
    # 1d series generation methods
    # series is written in variable
    ###############################################

    def linear(self, first_point=0, last_point=1000):
        self.data = np.linspace(first_point, last_point, self.points)
        return self

    def nonlinear(self, first_point=-3, last_point=3, n=5):
        x = self.linear(first_point, last_point).data
        apex = (last_point + first_point) / 2
        y = list()
        for i in x:
            y.append([(i - apex)**n - 10])
        self.data = y
        return self

    def quadratic(self, first_point=-10, last_point=10):
        self.data = self.nonlinear(first_point, last_point, 2).data
        return self

    def cubic(self, first_point=-10, last_point=10):
        self.data = self.nonlinear(first_point, last_point, 3).data
        return self

    def __init__(self, points=1000):
        self.points = points
        self.data = []
        self.data_frame = pd.DataFrame([])

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
        data = self.data
        f = open(filename, 'w')
        for index in data:
            f.write(str(index[0]) + '\n')
        f.close()
        return self


if __name__ == "__main__":
    a = Genseries_1d(100).cubic().to_txt()
    plt.plot(a.data); plt.show()
