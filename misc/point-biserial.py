import math
from scipy import stats

X = [1, 5, 3, 6, 7, 9, 2, 1]
#Y = [0, 1, 0, 1, 1, 1, 0, 0]
Y = [3, 6, 3, 7, 6, 7, 2, 4]

pbr, pvalue = stats.pointbiserialr(Y, X)
rxy, rp = stats.pearsonr(X, Y)

print(pbr)
print(rxy)

'''
# Pearson's correlation
mean_x = sum(X) / len(X)
mean_y = sum(Y) / len(Y)

r1 = 0
r2 = 0
r3 = 0

for i in range(len(X)):
    r1 = r1 + (X[i] - mean_x) * (Y[i] - mean_y)

for i in range(len(X)):
    r2 = r2 + (X[i] - mean_x)**2

r2 = math.sqrt(r2)

for i in range(len(Y)):
    r3 = r3 + (Y[i] - mean_y)**2

r3 = math.sqrt(r3)

rxy = r1 / (r2 * r3)

print(rxy)

# Point-biserial correlation
M1 = 6.75
M0 = 1.75

n1 = 4
n0 = 4
n = 8

xp = 0
for i in range(len(X)):
    xp = xp + (X[i] - mean_x)**2

std = math.sqrt((1 / (n-1)) * xp)

pb = ((M1 - M0) / std) * math.sqrt((n1 * n0) / (n * (n - 1)))

print(pb)
'''