import pandas as pd


def write_to_map(f):
    data_map = list()
    with open(f, "r") as file:
        for line in file:
            data_map.append(list(map(str, line.split())))
    return(data_map)


def solution(path=r'D:\Санкт Петербург жизнь и работа\Техническая литература\словарик.txt'):
    sample_map = write_to_map(path)
    en_words = list()
    ru_words = list()
    for i in range(len(sample_map) - 2):
        en_words.append({"english": sample_map[i][0]})
        ru_words.append({"russian": sample_map[i][len(sample_map[i]) - 1]})
    en_words = pd.DataFrame(en_words)
    ru_words = pd.DataFrame(ru_words)
    words = en_words.join(ru_words)
    words.to_csv(path[:len(path)-4] + '.csv')


if __name__ == "__main__":
    solution()
