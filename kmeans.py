# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 18:35:44 2017

@author: Smau2
"""
from __future__ import division
import numpy as np
import math as math
import matplotlib.pyplot as plt
import sys


def euclidDist(ptA, ptB):
    """
    Function to find euclidean distance between ptA and ptB
    IN: ptA, ptB - points to compare
    Out: dist - euclidean distance ^ 2
    """
    dist = 0
    #Check if point sizes are equal.
    if len(ptA) != len(ptB):
        sys.exit('Error: ptA has size ' + str(len(ptA)) + ' but ptA has size ' + str(len(ptB)))
    #Calculate euclidean distance
    else:
        for num in range(0,len(ptA)):
            dist = dist + math.pow(ptA[num]-ptB[num],2)
    return dist

def average(points):
    """
    Function to find average of points in array
    IN: points - Array of points
    Out: avg - average of all points in the array.  Will output "None" if points is empty
    """
    #If no points are in the cluster, return None.
    if len(points) == 0:
        return None
    avg = [None]*len(points[0])
    #Calculate the average of each coordinate
    for i in range(0,len(points[0])):
        sum = 0
        for j in range(0,len(points)):
            sum = sum + points[j][i]
        avg[i] = sum/len(points)
    return avg

def randomPoint(minP, maxP):
    """
    Function to generate a random points between minValues and maxValues
    IN: minP, maxP - minimum values and maximum values of points, respectively
    Out: point - random point generated from minP and maxP
    """
    point = []
    for i in range (0,len(minP)):
        point.append((maxP[i]-minP[i])*np.random.rand() + minP[i])
    return point 
       
def kmeans(k, points, distanceFunc, newCenterFunc):
    """
    IN: k - number of clusters, points - array of points to be sorted
    distanceFunc - function to determine distance, newCenterFunc - function to find new center
    OUT: groupings - output array, centers - centers used, iterations - number of iterations
    """
    
    #Find range of points, store in minP and maxP
    minP = [sys.maxint]*len(points[0])
    maxP = [-sys.maxint]*len(points[0])
    for j in range(0,len(points)):
        for l in range(0,len(points[0])):
            if points[j][l] < minP[l]:
                minP[l] = points[j][l]
            if points[j][l] > maxP[l]:
                maxP[l] = points[j][l]
                
     #Initialize array centers, which stores the initially random centers          
    centers = np.zeros((k,len(maxP)))
    for j in range(0,k):
         centers[j] = randomPoint(maxP,minP)
    
    #Group each point to the closest center.  groupings[i] will store the cluster of point[i]
    groupings = np.zeros(len(points))
    
    for j in range(0,len(points)):  
        minDist = sys.maxint
        group = 0
        for l in range(0,k):
            if distanceFunc(centers[l],points[j]) < minDist:
                minDist = distanceFunc(centers[l],points[j])
                group = l
        groupings[j]=group
    
    #Create k lists of points associated with each cluster
    clusters = [[] for x in xrange(0,k)]
    for j in range(0,len(points)):
        clusters[int(groupings[j])].append(points[j])
        
    #Generate new cluster centers
    for j in range(0,k):
        newCenter = newCenterFunc(clusters[j])
        if newCenter == None:
            centers[j] = randomPoint(minP,maxP)
        else:
            centers[j] = newCenter

    #Repeat the process until the groupings converge    
    iterations = 1
    new_groupings = -np.ones(len(points))
    while not np.array_equal(groupings,new_groupings):
        iterations = iterations + 1
        groupings = new_groupings
        for j in range(0,len(points)):  
            minDist = sys.maxint
            group = 0
            for l in range(0,k):
                if distanceFunc(centers[l],points[j]) < minDist:
                    minDist = distanceFunc(centers[l],points[j])
                    group = l
            new_groupings[j]=group
        clusters = [[] for x in xrange(0,k)]
        for j in range(0,len(points)):
            clusters[int(new_groupings[j])].append(points[j])
        for j in range(0,k):
            newCenter = newCenterFunc(clusters[j])
            if newCenter == None:
                centers[j] = randomPoint(minP,maxP)
            else:
                centers[j] = newCenter
        print groupings
        print new_groupings
    
    return groupings, centers, iterations
    
    

groupings, centers, iterations = kmeans(2,[[1,1],[1.1,1.1],[1.1,1],[1,1.1],[1.2,1],[0.9,1]],euclidDist,average)
print groupings
print centers
print iterations

    

    
    