# -*- coding: utf-8 -*-
"""
Created on Thu Nov 02 08:11:32 2017

@author: Smau2
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets.samples_generator import make_blobs
from sklearn.cluster import k_means
from sklearn.metrics import adjusted_mutual_info_score, mutual_info_score, normalized_mutual_info_score

def kMeans_accuracy(dist):
    num_samples = 100
    #fig = plt.figure()
    #ax = fig.add_subplot(211)
    X,y = make_blobs(n_samples=num_samples, centers=[[0,0],[dist,0]], n_features=2)
    #colors = ['red','blue','green']
    #for i in range(len(X)):
    #    ax.scatter(X[i][0],X[i][1],color=colors[y[i]])
    centroid, labels, intertia, iterations = k_means(n_clusters=2,X=X,return_n_iter=True)
    correct = 0;
    score = (normalized_mutual_info_score(y,labels))
    for i in range(len(X)):
        if labels[i] == y[i]:
            correct = correct + 1
    correct = max(correct, num_samples-correct)
    return [score,iterations]
    #ax = fig.add_subplot(212)
    #for i in range(len(X)):
    #    ax.scatter(X[i][0],X[i][1],color=colors[labels[i]])

distances = [(x/2.0) for x in reversed(range(21))]
print(distances)
accuracy = []
std = []
trials_acc = []
trials_iter = []



for dist in distances:
    for i in range(0,500):
        trials_acc.append(kMeans_accuracy(dist)[0])
        trials_iter.append(kMeans_accuracy(dist)[1])
    accuracy.append(np.average(trials_acc))
    std.append(np.std(trials_acc))
    trials_acc = []

plt.errorbar(distances,accuracy,std,fmt='o', capsize=5)

