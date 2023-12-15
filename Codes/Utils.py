from tkinter import font
from matplotlib import legend
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, RegularPolygon
from matplotlib.path import Path
from matplotlib.projections.polar import PolarAxes
from matplotlib.projections import register_projection
from matplotlib.spines import Spine
from matplotlib.transforms import Affine2D
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
import os
import csv
import json



def loadjson(filename):
    """Load json file from filename."""
    with open(filename, 'r') as f:
        data = json.load(f)
    return data

def loadcsv(path):
    with open(path, 'r',encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile)
        data = [row for row in reader]
    return data

def savecsv(path,csvdata):
    """Save csv file to path."""
    with open(path, 'w', newline='',encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(csvdata)

def find_unique_values(data):
    """Return a list of unique values in data."""
    unique = []
    for item in data:
        if item not in unique:
            unique.append(item)
    return unique

def visulize_cluster(data,y,centers,savepath):
    plt.scatter(data[:,0],data[:,1],c=y)
    plt.scatter(centers[:,0],centers[:,1],c='r')
    name = 'cluster.png'
    counter = 1
    while True:
        if os.path.isfile(os.path.join(savepath,name)):
            name = 'cluster_'+str(counter)+'.png'
            counter += 1
        else:
            break
    plt.savefig(os.path.join(savepath,name))

def visulize_cluster_values(df,stats=[],labels = [],savepath=''):
    if labels == []:
        stats = df.index.values.tolist()
    else:
        stats = stats + ['Cluster']

    data = df[stats]
    colors = ['#FFA33C','#427D9D','#566246','#F6AE2D','#433E0E','#EDEEC0','#A7A284','#CACFD6','#B3B3B3','#F2F2F2','#561F37','#453823','#55DBCB','#75E4B3','#FBC2B5','#A14A76']
    
    if labels == []:
        labels = data.index.values.tolist().removing('Cluster')
    print(data['Cluster'].values.tolist())
    unique_cluster = find_unique_values(data['Cluster'].values.tolist())
    unique_cluster = sorted(unique_cluster)
    fig = go.Figure()
    for cluster in unique_cluster:
        cluster_stuts = []
        for stat in stats:
            if stat != 'Cluster':
                #print(len(data[stat][data['Cluster']==cluster]))
                cluster_stuts.append(data[stat][data['Cluster']==cluster].mean())
        fig.add_trace(go.Scatterpolar(
        r=cluster_stuts,
        theta=labels,
        fill='toself',
        name='Cluster '+str(cluster + 1) + ' ('+str(len(data['Cluster'][data['Cluster']==cluster]))+' data points)',
        line_color = colors[cluster],
        ))
    name = 'cluster_values.png'
    counter = 1
    while True:
        if os.path.isfile(os.path.join(savepath,name)):
            name = 'cluster_values_'+str(counter)+'.png'
            counter += 1
        else:
            break
    
    #fig.save(os.path.join(savepath,'name'))
    fig.show()



