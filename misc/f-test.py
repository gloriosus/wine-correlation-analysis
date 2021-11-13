from scipy import stats
from scipy import special

sample_size = 30
number_of_independent_var = 3

determination_coefficient = 0.45

d1 = number_of_independent_var
d2 = sample_size - (number_of_independent_var + 1)

f_value = (determination_coefficient * (sample_size - number_of_independent_var - 1)) / (number_of_independent_var * (1 - determination_coefficient))

a = 0.05
f_crit = stats.f.ppf(q=1-a, dfn=d1, dfd=d2)

x = (d1 * f_value) / (d1 * f_value + d2)

p_value = 1 - special.betainc(d1/2, d2/2, x)
#p_value = 1 - stats.f.cdf(f_value, dfn=d1, dfd=d2) Exact the same thing
#p_value = stats.f.sf(f_value, dfn=d1, dfd=d2) Exact the same thing

print(f_value)
print(f_crit)
print(p_value)

# Correct results
'''
7.090909090909091
2.9751539639733933
0.0012326805381360773
'''