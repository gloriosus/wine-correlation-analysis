import pandas
import matplotlib.pyplot as plt

dataset = pandas.read_csv('winequality-red.csv',';')

i = 1

for n in range(12):
    x = dataset.iloc[:, n].values
    for m in range(n + 1, 12):
        y = dataset.iloc[:, m].values
        plt.plot(x, y, 'ro')
        plt.savefig('fig' + str(i) + '.png')
        i = i + 1