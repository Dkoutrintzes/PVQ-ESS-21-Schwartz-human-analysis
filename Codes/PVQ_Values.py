import csv
from itertools import count
from math import e, exp
import os
from re import T
import datetime
import re
import sys
import pandas as pd
from numpy import mean, save
from Utils import loadcsv,savecsv
import tkinter as tk 
from tkinter.filedialog import askopenfilename
from statistics import mean


def Schwartz_10_values(data):
    """Return the 10 values of Schwartz."""
    values = ['Mrat','Self-direction','Stimulation','Hedonism','Achievement','Power','Security','Conformity','Tradition','Benevolence','Universalism']
    output = []
    for i in data.index.values.tolist():
        allavg = 0
        for j in range(21):
            item = 'v'+str(j+1)
            allavg += int(data[item][int(i)])
        mrat = round(allavg/21,3)

        #Power v2, v17
        power = round(mean((int(data['v2'][int(i)]),int(data['v17'][int(i)]))) - mrat,3)
        #achievement v4, v13
        achievement = round(mean((int(data['v4'][int(i)]),int(data['v13'][int(i)]))) - mrat,3)
        #hedonism v10, v21
        hedonism = round(mean((int(data['v10'][int(i)]),int(data['v21'][int(i)]))) - mrat,3)
        #stimulation v6, v15
        stimulation = round(mean((int(data['v6'][int(i)]),int(data['v15'][int(i)]))) - mrat,3)
        #self-direction v1, v11
        self_direction = round(mean((int(data['v1'][int(i)]),int(data['v11'][int(i)]))) - mrat,3)
        #universalism v3, v8, v19
        universalism = round(mean((int(data['v3'][int(i)]),int(data['v8'][int(i)]),int(data['v19'][int(i)]))) - mrat,3)
        #benevolence v12, v18
        benevolence = round(mean((int(data['v12'][int(i)]),int(data['v18'][int(i)]))) - mrat,3)
        #tradition v9, v20
        tradition = round(mean((int(data['v9'][int(i)]),int(data['v20'][int(i)]))) - mrat,3)
        #conformity v7, v16
        conformity = round(mean((int(data['v7'][int(i)]),int(data['v16'][int(i)]))) - mrat,3)
        #security v5, v14 
        security = round(mean((int(data['v5'][int(i)]),int(data['v14'][int(i)]))) - mrat,3)    
        #print(power)
        output.append([mrat,self_direction,stimulation,hedonism,achievement,power,security,conformity,tradition,benevolence,universalism])

    output = pd.DataFrame(output,columns=values)
    return output

def Schwartz_4_high_values(data):
    """Return the 4 high values of Schwartz."""
    values = ['Openness to Change','Self-Enhancement','Conservation','Self-Trancendence']
    output = []
    #print(data)
    for i in data.index.values.tolist():
        #print(float(data['Self-direction'][int(i)]),float(data['Stimulation'][int(i)]),float(data['Hedonism'][int(i)]))
        # Openness to Change = (Self-direction + Stimulation + Hedonism)/3
        opchng = round(mean((float(data['Self-direction'][int(i)]),float(data['Stimulation'][int(i)]),float(data['Hedonism'][int(i)]))),3)
        # Self-Enhancement = (Achievement + Power)/2
        self_enhancement = round(mean((float(data['Achievement'][int(i)]),float(data['Power'][int(i)]))),3)
        # Conservation = (Security + Conformity + Tradition)/3
        conservation = round(mean((float(data['Security'][int(i)]),float(data['Conformity'][int(i)]),float(data['Tradition'][int(i)]))),3)
        # Self-Trancendence = (Benevolence + Universalism)/2
        self_trancendence = round(mean((float(data['Benevolence'][int(i)]),float(data['Universalism'][int(i)]))),3)
        
        output.append([opchng,self_enhancement,conservation,self_trancendence])
    output = pd.DataFrame(output,columns=values)
    return output    


    