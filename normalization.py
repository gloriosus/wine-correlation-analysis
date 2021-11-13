import pandas
from sklearn.preprocessing import PowerTransformer

dataset = pandas.read_csv('C:/Users/vecryd/Projects/WineCorrelationAnalysis/data/winequality-red-dichotomous.csv',';')

pt = PowerTransformer()

columns_for_transformation = ['fixed acidity', 'volatile acidity', 'residual sugar', 'chlorides', 'free sulfur dioxide', 'total sulfur dioxide', 'sulphates']

dataset.loc[:, columns_for_transformation] = pt.fit_transform(dataset.loc[:, columns_for_transformation])
dataset = pandas.DataFrame(data=dataset, columns=['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar', 'chlorides', 'free sulfur dioxide', 'total sulfur dioxide', 'density', 'pH', 'sulphates', 'alcohol', 'quality'])

dataset.to_csv('C:/Users/vecryd/Projects/WineCorrelationAnalysis/data/winequality-red-dichotomous-normalized.csv',';', header=True, index=False)