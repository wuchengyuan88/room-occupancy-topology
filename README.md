# room-occupancy-topology
Code and data sets for Topological Machine Learning for Multivariate Time Series

Folder structure:
Occupancy_Test1: Contains data set and codes for Test 1 (predicting future room occupancy)
Occupancy_Test2: Contains data set and codes for Test 2 (predicting past room occupancy)

Order of running code:
1) dataCleaning.py
Python code for data preparation and cleaning.

2) pointCloud.py
Python code for converting multivariate time series to point cloud data.

3) predictionColumn.py
Python code to output a column containing room occupancy status (0 or 1) of each time window.

4) TDA_distmatrix.R
R code to calculate Wasserstein distances between persistence diagrams.

5) knn.py
Python code to run the k-nearest neighbors algorithm for binary classification.
