# -*- coding: utf-8 -*-
"""
This program will exhibit an example of data minning
We will import and visualise data from a spreadsheet
Classify and cluster 
discover relationships
compress and
analyse the data set by using k-means


stats taken from https://corona-stats.co.za/ as of 22 April 05:30am

@author: KeamogetsweMashao
"""


from copy import deepcopy
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans
import random as rd

#Importing data from external csv file
data = pd.read_csv('covid.csv')
data.head()

X = data[["TotalCases","Deaths"]]
#Visualising data points of the total number of cases and the deaths
plt.scatter(X["Deaths"],X["TotalCases"],c='black')
plt.xlabel('Deaths)')
plt.ylabel('TotalCases')
plt.show()


#number of clusters
K=1  #making it one cluster to show a more accurate description as opposed to
#a greater variance

#Selecting random observation as centroids
Centroids = (X.sample(n=K))
plt.scatter(X["Deaths"],X["TotalCases"],c='black')
plt.scatter(Centroids["Deaths"],Centroids["TotalCases"],c='red')
plt.xlabel('Deaths')
plt.ylabel('TotalCases')
plt.show()

diff = 1
j=0


#Required loop to implement k-means
while(diff!=0):
    XD=X
    i=1
    for index1,row_c in Centroids.iterrows():
        ED=[]
        for index2,row_d in XD.iterrows():
            d1=(row_c["Deaths"]-row_d["Deaths"])**2
            d2=(row_c["TotalCases"]-row_d["TotalCases"])**2
            d=np.sqrt(d1+d2)
            ED.append(d)
        X[i]=ED
        i=i+1

    C=[]
    for index,row in X.iterrows():
        min_dist=row[1]
        pos=1
        for i in range(K):
            if row[i+1] < min_dist:
                min_dist = row[i+1]
                pos=i+1
        C.append(pos)
    X["Cluster"]=C
    Centroids_new = X.groupby(["Cluster"]).mean()[["TotalCases","Deaths"]]
    if j == 0:
        diff=1
        j=j+1
    else:
        diff = (Centroids_new['TotalCases'] - Centroids['TotalCases']).sum() + (Centroids_new['Deaths'] - Centroids['Deaths']).sum()
        print(diff.sum())
    Centroids = X.groupby(["Cluster"]).mean()[["TotalCases","Deaths"]]
    
    #colours for scatter plot
    color=['blue','green','cyan']
for k in range(K):
    data=X[X["Cluster"]==k+1]
    #used a line graph as oppsed to a scattter to better show the relationship
    plt.plot(data["Deaths"],data["TotalCases"],c=color[k])
plt.plot(Centroids["Deaths"],Centroids["TotalCases"],c='red')
plt.xlabel('Deaths')
plt.ylabel('TotalCases')
plt.title ('covid cases in relation to number of deaths in South Africa')
#display data in scatter plot, analysing the data set
plt.show()