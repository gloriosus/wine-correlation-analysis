# Multiple correlation analysis of wine quality

The application consists of three preliminary modules that help to prepare the data by dichotomizing and normalizing the original dataset, and make histograms. The modules should be run before executing the main module in the following order:
1. [[src/corr/dichotomizer.py|dichotomizer.py]]
2. [[src/corr/normalization.py|normalization.py]]
3. [[src/corr/histograms.py|histograms.py]]

Then the "[[src/corr/main.py|main.py]]" module may be executed.

The original data file named "winequality-red.csv" is located in the data folder. There are also other data files that are already prepared for an analysis. So, the execution of the three preliminary modules may be skipped and the main module may be run with the "winequality-red-dichotomous-normalized.csv" file from the data folder.

The "dichotomizer.py" module creates a new data file which includes changes to the original data file replacing expert evaluates to their dichotomized versions (0 or 1).

The "normalization.py" module creates a new data file with a log-transform function applied to selected features in order to get a distribution close to normal.

The "histograms.py" module creates histograms and pdf from the normalized data.

The "main.py" module carries out the analysis and print results to console.