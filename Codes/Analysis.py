import csv
from itertools import count
from cycler import V
import pandas as pd
from math import e, exp
import os
from re import T
import datetime
import sys
import numpy as np
from numpy import mean, save
from Utils import loadcsv,savecsv,visulize_cluster_values
import tkinter as tk 
from tkinter.filedialog import askopenfilename
from PVQ_Values import Schwartz_10_values, Schwartz_4_high_values
from Kmeans_Clustering import kmean_cluster


if __name__ == '__main__':
    savepath = sys.argv[2]
    if not os.path.isdir(savepath):
        os.mkdir(savepath)

    datapath = sys.argv[1]
    data = loadcsv(datapath)

    labeled = sys.argv[3]
    if labeled == 'True':
        data = pd.DataFrame(data[1:],columns=data[0])
        items = ['v'+str(i+1) for i in range(21)]
        pvq_answers = data[items]
        #print(pvq_answers)
    else:
        items = ['v'+str(i+1) for i in range(21)]
        pvq_data = []
        id = 1
        start = 0
        end = 0
        while end - start != 21:
            #Ask for start and end points 
            start = int(input('Start: '))
            end = int(input('End: '))
            if end - start != 21:
                print('Invalid start and end points. Please try again.')
        for pt in data:
            answers = pt[start:end]
            pvq_data.append(answers)
        pvq_answers = pd.DataFrame(pvq_data,columns=items)
    
    print(pvq_answers)

    pvq_10_values = Schwartz_10_values(pvq_answers)
    pvq_4_high_values = Schwartz_4_high_values(pvq_10_values)
    exp_data = pd.concat([pvq_10_values,pvq_4_high_values],axis=1)
    #print(exp_data)
    
    clustering = sys.argv[4]
    if clustering == 'True':
        y,centers = kmean_cluster(exp_data,features=['Openness to Change','Self-Enhancement','Conservation','Self-Trancendence'],centers=3,savepath=savepath)
        exp_data = pd.concat([exp_data,pd.DataFrame(y,columns=['Cluster'])],axis=1)
    visulization = sys.argv[5]
    if visulization == 'True':
        visulize_cluster_values(exp_data,stats=['Self-Enhancement','Openness to Change','Self-Trancendence','Conservation'],labels=['SE','OC','ST','CO'],savepath=savepath)

    name = 'PVQ_Values.csv'
    counter = 1
    while True:
        if os.path.isfile(os.path.join(savepath,name)):
            name = 'PVQ_Values_'+str(counter)+'.csv'
            counter += 1
        else:
            break

    exp_data.to_csv(os.path.join(savepath,name),index=False)