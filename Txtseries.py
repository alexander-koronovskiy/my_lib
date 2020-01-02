import pandas as pd


class Txtseries:

    ############################################
    # methods print of the class object params:
    # filename, data, data_frame
    ############################################

    def print_filename(self):
        print(self.filename)
        return self

    def print_data(self):
        print(self.data)
        return self

    def print_data_frame(self):
        print(self.data_frame)
        return self

    ################################################
    # methods initialise of the class object params:
    # filename, data, data_frame
    ################################################

    def __init__(self, filename):
        self.filename = filename
        self.data = str([]) + '\nFile with series isn\'t read, ' \
                              'use the method "read" in this way: obj.read()'
        self.data_frame = str(pd.DataFrame([])) + '\nClass object has not data frame,' \
                                                  ' use the methods this way obj.read().to_df()'

    # read .txt file - this need to file path exceptions (unique method)
    # record rows in list: "data"
    def read(self, enc='utf-8'):
        f = self.filename
        data_map = list()
        with open(f, "r", encoding=enc) as file:
            for line in file:
                data_map.append(list(map(str, line.split())))
        self.data = data_map
        return self

    #######################################
    # we may heritage this from superclass
    # __init__ and print methods too
    #######################################

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
            file = self.filename
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
    a = Txtseries('out.txt')
    a.read().to_df().to_txt('out1.txt')
