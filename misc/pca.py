import pandas
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

dataset = pandas.read_csv('winequality-red.csv',';')

X = dataset.iloc[:, 0:11].values
y = dataset.iloc[:, 11].values

sc = StandardScaler()

X_sc = sc.fit_transform(X)

pca = PCA()
pca.fit(X_sc)

print(pca.components_.round(2))
print('\n')
print(pca.explained_variance_ratio_.round(2))