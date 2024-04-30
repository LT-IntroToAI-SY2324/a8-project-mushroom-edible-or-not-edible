# Cat Markowska, P.3
# Kelly Ocampo, P.3

from typing import Tuple
from neural import *
from sklearn.model_selection import train_test_split

def parse_line(line: str) -> Tuple[List[float], List[float]]:
    tokens = line.split(",")
    out = int(tokens[0])
    output = [0 if out == 1 else 0.5 if out == 2 else 1]

    inpt = [float(x) for x in tokens[1:]]
    return (inpt, output)

def normalize(data: List[Tuple[List[float], List[float]]]):
    leasts = len(data[0][0]) * [100.0]
    mosts = len(data[0][0]) * [0.0]

    for i in range(len(data)):
        for j in range(len(data[i][0])):
            if data[i][0][j] < leasts[j]:
                leasts[j] = data[i][0][j]
            if data[i][0][j] > mosts[j]:
                mosts[j] = data[i][0][j]

    for i in range(len(data)):
        for j in range(len(data[i][0])):
            data[i][0][j] = (data[i][0][j] - leasts[j]) / (mosts[j] - leasts[j])
    return data

with open("mushroom_data.txt", "r") as f:
    training_data = [parse_line(line) for line in f.readlines() if len(line) > 4]

# print(training_data)
td = normalize(training_data)
# print(td)

train, test = train_test_split(td)

nn = NeuralNet(13, 3, 1)
nn.train(train, iters=10000, print_interval=1000, learning_rate=0.2)

for i in nn.test_with_expected(test):
    difference = round(abs(i[1][0] - i[2][0]), 3)
    print(f"desired: {i[1]}, actual: {i[2]} diff: {difference}")