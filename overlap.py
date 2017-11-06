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
    return [correct/float(num_samples),iterations,score]
    #ax = fig.add_subplot(212)
    #for i in range(len(X)):
    #    ax.scatter(X[i][0],X[i][1],color=colors[labels[i]])

distances = [(x/2.0) for x in reversed(range(21))]
print(distances)
accuracy = []
std_acc = []
mi_score = []
std_mi_score = []
iterations = []
std_iterations = []

trials_acc = []
trials_iter = []
trials_mi = []



for dist in distances:
    for i in range(0,100):
        kMeans_trial = kMeans_accuracy(dist)
        trials_acc.append(kMeans_trial[0])
        trials_iter.append(kMeans_trial[1])
        trials_mi.append(kMeans_trial[2])
    accuracy.append(np.average(trials_acc))
    std_acc.append(np.std(trials_acc))
    iterations.append(np.average(trials_iter))
    std_iterations.append(np.std(trials_iter))
    mi_score.append(np.average(trials_mi))
    std_mi_score.append(np.std(trials_mi))
    trials_acc = []
    trials_iter = []
    trials_mi = []

plt.errorbar(distances,mi_score,std_mi_score,fmt='o', capsize=5)


