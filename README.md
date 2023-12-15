# PVQ-ESS-21-Schwartz-human-values-extraction
This GitHub contains an analysis of the PVQ(ESS) 21 data. The analysis of the questionnaire is based on the Scoring and Analysis Instructions for the ESS21 Value Scale [1]
The questionnaire includes 21 items and can generate Schwartz's [2] 10 human values and the 4 high motivations.

---
To run the scripts first install the required Python packages
```
pip install requirements.txt
```
---
The Analysis.py runs the main analysis of the data. To run it you must have the data from the questionnaire in a CSV file. 
The analysis also has the option to run a k-means clustering using the 4 high motivations and to visualize the clusters' statistics.
This code is meant to run even if the CSV file contains other data. In the case of the CSV file containing labels in the first line, the labels of each item must be v+[number of item]. The format of the file must look something like the following:

 ```
     ... v1 v2 v3  ... v19 v20 v21 ...
0    ... 6   4   2  ... 6   6   3  ... 
1    ... 1   3   3  ... 6   5   3  ... 
..   ... ..  ..  ..  .. ..  ..  .. ... 
n-1  ... 6   6   5  ... 5   6   4  ...
n    ... 4   6   6  ... 4   6   1  ... 
```
If there are no labels, the code will request the start and end columns where the PVQ data are. In this case, the question must be in order and together. 



