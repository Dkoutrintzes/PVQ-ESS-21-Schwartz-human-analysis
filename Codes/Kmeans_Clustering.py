import csv
import os
from pdb import run
import sys
import numpy as np
from sklearn.cluster import KMeans
from sklearn import neighbors
from sklearn import cluster, datasets
from sklearn.preprocessing import StandardScaler
from sklearn import metrics
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, RegularPolygon
from matplotlib.path import Path
from matplotlib.projections.polar import PolarAxes
from matplotlib.projections import register_projection
from matplotlib.spines import Spine
from matplotlib.transforms import Affine2D
from Utils import loadcsv,savecsv
from Utils import visulize_cluster_values,visulize_cluster

def kmean_cluster(df,features = [],centers=2,savepath=''):
    print(features)
    if features == []:
        features = df.index.values.tolist()
    data = df[features].values.tolist()
    print(data)
    scalar_input = scalar(data)
    kmeans = KMeans(n_clusters=centers, random_state=0).fit(scalar_input)
    y = kmeans.labels_
    centers = kmeans.cluster_centers_
    pca_data,pca_centers = run_pca(data,centers)
    visulize_cluster(pca_data,y,pca_centers,savepath)
    return y, centers

def run_pca(data,centers):
    pca = PCA(n_components=2)
    pca.fit(data)
    return pca.transform(data),pca.transform(centers)


def scalar(data):
    """Standardize features by removing the mean and scaling to unit variance"""
    return StandardScaler().fit_transform(data)
