import pandas
from sklearn.preprocessing import PowerTransformer

dataset = pandas.read_csv('winequality-red.csv',';')

pt = PowerTransformer()
dataset = pt.fit_transform(dataset)
dataset = pandas.DataFrame(data=dataset)
feature = dataset.iloc[:, 6]