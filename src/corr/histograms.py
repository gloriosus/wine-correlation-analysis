import pandas
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

dataset = pandas.read_csv('C:/Users/vecryd/Projects/WineCorrelationAnalysis/data/winequality-red-dichotomous.csv',';')
#dataset = pandas.read_csv('C:/Users/vecryd/Projects/WineCorrelationAnalysis/data/winequality-red-dichotomous-normalized.csv',';')

number_of_columns = len(dataset.columns)

for i in range(number_of_columns - 1):

    feature = dataset.iloc[:, i]

    min_value = feature.min()
    max_value = feature.max()
    length = feature.count()

    mean = np.mean(feature)
    median = np.median(feature)
    mode = stats.mode(feature)[0][0]  # Result like 'ModeResult(mode=array([86]), count=array([3]))'
    kurt = stats.kurtosis(feature)
    skewness = stats.skew(feature)

    number_of_bins = 40  # math.ceil(math.sqrt(length))
    bins = np.linspace(min_value, max_value, number_of_bins)

    figure, axes = plt.subplots()

    plt.hist(x=feature, bins=bins, density=True, color='green', alpha=0.7, rwidth=0.85)
    plt.grid(axis='y', alpha=0.75)
    plt.xlabel('Value')
    plt.ylabel('Density')
    plt.title(feature.name)
    plt.text(0.7, 1.02, 'x\u0304=' + str(round(mean, 2)) + ', x\u0303=' + str(round(median, 2)) + ', x\u030a=' + str(round(mode, 2)) + ',\n' + 'k=' + str(round(kurt, 2)) + ', s=' + str(round(skewness, 2)), transform=axes.transAxes)

    # Distribution function
    std = np.std(feature)
    X = np.linspace(min_value, max_value, 400)
    pdf = stats.norm.pdf(X, mean, std)

    scale = 1  # 0.8 * math.sqrt(2*math.pi) * std

    plt.plot(X, scale * pdf, c='red')

    plt.savefig(str(i+1) + ' ' + feature.name)
    #plt.show()