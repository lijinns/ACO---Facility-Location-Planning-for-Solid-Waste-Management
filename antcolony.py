# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 20:52:02 2022

@author: Lijin N S
"""

import pandas as pd
import numpy as np
import requests
import json 
import random
from itertools import permutations

from functions import part, probdenom, setrandom, chooserandom, totaldist, phupdate

# Defining the Ant Colony function. deafult values, alpha = 1, beta = 5, gamma = 0.5

def AntColony(size,alpha = 1, beta = 5, gamma = 0.5, test = False, best = None):  
    '''The Ant Colony Optimization Function'''
    
    #Requires 'distancedata.csv' file in the directory
    distancematrix = pd.read_csv('distancedata.csv',index_col = 0).values
    triald = distancematrix
    trialh = np.full((26,26),0.1)
    shortestd = 20000000 #or any large number
    
    #iteration for journeys
    for epoch in range(size*2):
        print('Epoch {}:'.format(epoch+1))
        shortestdistance = 20000000
        
        #ant iteration
        for x in range(size*20):
            unvisited = np.arange(0,size)
            path = [] 
            
            #choosing next location to visit
            for ant in range(size):

                if ant == 0:
                    node = np.random.choice(unvisited)

                else:
                    denom = probdenom(node,visit,trialh,triald)
                    numprob = setrandom(node,visit,denom,trialh,triald)
                    randindex = chooserandom(numprob)
                    node = visit[randindex]
            
                visit = unvisited[unvisited!=node]
                path.append(node)
                unvisited = visit
        
            distance = totaldist(triald,path)
            path.append(path[0])
            
            if test == True:
                if distance <= best:
                    print('optimal Solution found at Epoch {}'.format(epoch+1))
                    return
            
            trialh *= 0.5
            phupdate(trialh,path,distance)
            if distance <= shortestdistance:
                shortestdistance = distance
                shortestpath = path
            
        
    
        print('Shortest Path of Ant in this epoch: {}\nShortest Path Distance in this epoch: {}\n'.format(shortestpath,shortestdistance))
        trialh = np.full((26,26),0.1)
        if shortestdistance < shortestd:
                shortestd = shortestdistance
                shortestp = shortestpath
                ep = epoch
    print('Ant Colony Optimization:\nShortest Path: {}\nShortest Path Distance: {} kilometres\n'.format(shortestp,shortestd))
    return shortestp,shortestd, ep
    #returns shortest path and distance of that path