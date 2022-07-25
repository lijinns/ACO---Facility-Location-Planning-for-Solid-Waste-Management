# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 20:44:31 2022

@author: Lijin N S
"""

#Importing required libraries

import pandas as pd
import numpy as np
import requests
import json 
import random
from itertools import permutations

from antcolony import AntColony


#Loading the dataset procured by plotting bin locations on Google Mymaps
#Requires 'dataset.csv' file in the directory
data = pd.read_csv('dataset.csv')
data = data.drop("Elevation", axis = 1)



#Renaming the index and columns
#Converting matrix to DataFrame
#Visualizing DataFrame
#x = data.id.values.tolist()
#distancedata=pd.DataFrame(distancematrix)
#distancedata.columns = x
#distancedata.index = x
#all units are in kilometers


#Running ACO with alpha = 1, beta = 5, gamma = 0.5
#The results show the path taken and the distance travelled in each journey per iteration
path,dist,epoch = AntColony(26)

#Displaying Result
path = path[path.index(25):] + path[: path.index(25)]
for x in range(len(path)):
    path[x] = 'Bin {}'.format(path[x]+1)
path[0] = 'Start'

print('Shortest Path found by the algorithm: \n{}\n\nDistance of path: {}. \nPath found in epoch {}.'.format(path,dist,epoch+1))








