# PVQ-ESS-21-Schwartz-human-analysis
 This GitHub contains an analysis of the PVQ(ESS) 21 data. The analysis of the questionnaire is based on the Scoring and Analysis Instructions for the ESS21 Value Scale [1]
The questionnaire includes 21 items and can generate Schwartz's [2] 10 human values and the 4 high-order values.

---
To run the scripts first install the required Python packages
```
pip install requirements.txt
```
---
 The Analysis.py runs the main analysis of the data. To run it you must have the data from the questionnaire in a CSV file. 
The analysis also has the option to run a k-means clustering using the 4 high-order values and to visualize the clusters' statistics.
This code is meant to run even if the CSV file contains other data. In the case of the CSV file containing labels in the first line, the labels of each item must be v+[number of item]. The format of the file must look something like the following:

 ```
     ... v1 v2 v3  ... v19 v20 v21 ...
0    ... 6   4   2  ... 6   6   3  ... 
1    ... 1   3   3  ... 6   5   3  ... 
..   ... ..  ..  ..  .. ..  ..  .. ... 
n-1  ... 6   6   5  ... 5   6   4  ...
n    ... 4   6   6  ... 4   6   1  ... 
```
If there are no labels, the code will request the start and end columns where the PVQ data are. In this case, the question must be in order and together. For the order of the questionnaire items see [3]

---
Analysis.py contains 5 arguments:
1. Data path: The path to the CSV file
2. Save path: The path where the export data will be saved
3. Labeled (True/False): True if the CSV file contains labels, False if not
4. Clustering (True/False): True for running the k-means clustering
5. Visualization (True/False): True for visualizing the stats of the clusters

To run the code execute:
```
python Codes\Analysis.py <path to csv> <path to save folder> <labeled> <clustering> <visualization>

```
 The code will create a CSV file in the save folder containing the 10 human values and the 4 high-order values.
For the clustering, in the export CSV file, there will be a cluster label for each individual and an image will be created with a 2D representation of the clusters
For the Visualization, the code created a localhost site containing a scanner graph with the 4 high-order values of each cluster.

---
[1] https://scholarworks.gvsu.edu/cgi/viewcontent.cgi?filename=0&article=1173&context=orpc&type=additional&preview_mode=1

[2] Schwartz, Shalom H. "An overview of the Schwartz theory of basic values." Online readings in Psychology and Culture 2.1 (2012): 11.

[3] *** To be added




