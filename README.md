The application includes three modules which should be run before executing the main module in the following order:
1. dichotomizer.py
2. normalization.py
3. histograms.py

dichotomizer.py makes changes into the original dataset by replacing expert evaluates to dichotomize version (0 or 1).
normalization.py applies log-transform function to selected features in order to get a distribution close to normal.
histograms.py builds histograms and pdf from the normalized data.

Then main.py is executed and results are shown up.