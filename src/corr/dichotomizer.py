import pandas

dataset = pandas.read_csv('C:/Users/vecryd/Projects/WineCorrelationAnalysis/data/winequality-red.csv',';')

length = len(dataset.index)

for i in range(length):
    if dataset.loc[i, 'quality'] <= 5:
        dataset.loc[i, 'quality'] = 0
    else:
        dataset.loc[i, 'quality'] = 1

dataset.to_csv('C:/Users/vecryd/Projects/WineCorrelationAnalysis/data/winequality-red-dichotomous.csv',';', header=True, index=False)