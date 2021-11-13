import os
import math
import pandas
import numpy
from scipy import stats
from scipy import special

def calculate_pvalues(source_data):
    significance_level = 0.001
    number_of_columns = len(source_data.columns)
    pvalue_matrix = numpy.zeros((number_of_columns, number_of_columns))

    for i in range(number_of_columns):
        for j in range(number_of_columns):
            pvalue_matrix[i, j] = 1 if stats.pearsonr(source_data.iloc[:, i], source_data.iloc[:, j])[1] < significance_level else 0

    return pvalue_matrix

numpy.set_printoptions(suppress=True)
pandas.set_option("display.max_columns", None)

filename = os.path.join(os.path.dirname(__file__), 'data/winequality-red-dichotomous-normalized.csv')

dataset = pandas.read_csv(filename,';')

correlation_matrix = dataset.corr()
print(correlation_matrix.round(2))
print('\n')

pvalue_matrix = calculate_pvalues(dataset)
print(pvalue_matrix)
print('\n')

determinant = numpy.linalg.det(correlation_matrix)

minor = correlation_matrix.drop(correlation_matrix.tail(1).index, axis=0)
minor = minor.drop(minor.columns[-1], axis=1)

complement = numpy.linalg.det(minor)

multiple_correlation = math.sqrt(1 - determinant / complement)

determination_coefficient = multiple_correlation**2

dataset_size = len(dataset)
independent_var_number = len(minor)
adjusted_determination_coefficient = 1 - (1 - determination_coefficient) * (dataset_size - 1) / (dataset_size - independent_var_number - 1)

'''
length = len(dataset.index)
degree_of_freedom = length - 2
tvalue = (multiple_correlation * math.sqrt(length - 2)) / math.sqrt(1 - multiple_correlation**2)
x = (tvalue + math.sqrt(tvalue**2 + degree_of_freedom)) / (2 * math.sqrt(tvalue**2 + degree_of_freedom))
a = degree_of_freedom / 2
b = degree_of_freedom / 2

multiple_pvalue = 1 - special.betainc(a, b, x) if x > (a + 1) / (a + b + 2) else special.betainc(a, b, x)
'''

d1 = independent_var_number
d2 = dataset_size - (independent_var_number + 1)

f_value = (adjusted_determination_coefficient * (dataset_size - independent_var_number - 1)) / (independent_var_number * (1 - adjusted_determination_coefficient))

a = 0.001
f_crit = stats.f.ppf(q=1-a, dfn=d1, dfd=d2)

x = (d1 * f_value) / (d1 * f_value + d2)

p_value = 1 - special.betainc(d1/2, d2/2, x)

print('Множественный коэффициент корреляции:', multiple_correlation)
print('Коэффициент детерминации:', determination_coefficient)
print('Скорректированный коэффициент детерминации:', adjusted_determination_coefficient)
print('F-значение:', f_value)
print('Критическое значение F:', f_crit)
print('p-значение множественного коэффициента корреляции:', p_value)