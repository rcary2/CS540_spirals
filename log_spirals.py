#!/usr/bin/env python3.6

########################################################## 
# Author:   Paul Cary
# Class:    CS 540 - Spring 2020
#
# This program will attempt to perform heirarchical 
#  agglomerative clustering (HAC) on a detaset of 
#  interlocking spirals (approximated from lecture)
#
# Packages Used:
# scipy==1.4.1
# matplotlib==3.2.0
# numpy==1.18.1
#
########################################################## 

## IMPORTS ##
import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial.distance import pdist
from scipy.cluster.hierarchy import dendrogram,linkage

## EXECUTION OPTIONS ##
DEBUG=False
#Set PLOT to True to see output
PLOT_SPIRALS=False
HAC=True #Heirarchical Agglomerative Clustering
PLOT_HAC=True
HCA=False #Heirarchical Clustering Analysis

## FUNCTIONS ##

#Make a function to verify euclidian distance
def point_dist_np(xy1,xy2):
    x = math.pow( (float(xy1[0]) - float(xy2[0]) ), 2)
    #print(x)
    y = math.pow( (float(xy1[1]) - float(xy2[1]) ), 2)
    #print(y)
    d = math.pow( (x + y), 0.5)
    #print(d)
    return d


if __name__ == '__main__':
    ## Example Set 1 -- Interlocking Spirals ##

    #Formula for log-spirals borrowed from:
    #https://stackoverflow.com/questions/48563526/drawing-a-logarithmic-spiral-in-three-axes-in-python
    #consider adding small rand epsilon to each theta/time point for a more interesting example

    #curve1
    n=100
    a1=0.6
    b1=0.20
    th1=np.linspace(7, 14, 30)
    #requires pylab * operator overload
    x1=a1*np.exp(b1*th1)*np.cos(th1)-1 #Rough adjust
    y1=a1*np.exp(b1*th1)*np.sin(th1)

    #curve2
    a2=0.85
    b2=0.23
    th2=np.linspace(4, 11, 30)
    x2=a2*np.exp(b2*th2)*np.cos(th2)
    y2=a2*np.exp(b2*th2)*np.sin(th2)+1 #Rough adjust

    if PLOT_SPIRALS:
        fig1 = plt.figure()
        ax1 = fig1.gca()
        ax1.scatter(x1, y1)
        ax1.scatter(x2, y2)

        plt.show()
        
    if HAC:
        #prep arrays for pdist, needs mxn array
        pts1 = np.column_stack((x1,y1))
        pts2 = np.column_stack((x2,y2))
        if DEBUG:
            print(pts1[0])
            print(pts1[1])
            #print(pts2[0])
            #print(pts2[1])
            X0 = point_dist_np(pts1[0],pts1[1])
            print(X0)

        X = np.row_stack((pts1,pts2))
        #print(all_points.shape)
        euY = pdist(X) # default metric='euclidian'
        #print(euY) 
        #print(euY.shape) #This is pts[0] vs. all, then pts[1] vs. all-pts[0]
        slinkH = linkage(euY, method='single', metric='euclidean')
        clinkH = linkage(euY, method='complete', metric='euclidean')

        if PLOT_HAC:
            fig, axs = plt.subplots(1, 3)

            axs[0].scatter(x1, y1)
            axs[0].scatter(x2, y2)
            axs[0].set_title('Spirals - Blue[0:29], Orange[30:59]')

            d1 =dendrogram(slinkH, ax=axs[1])
            axs[1].set_title('Single Linkage')

            d2 = dendrogram(clinkH, ax=axs[2])
            axs[2].set_title('Complete Linkage')

            plt.show()

    
        if HCA:
            #Start looking at clusters
            pass
