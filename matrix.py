# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 22:34:21 2022

@author: Lijin N S
"""

import numpy as np
import pandas as pd
import requests
import json 

#Function to find the distance between routes connecting each and every bin using OSRM(Open Source Routing Machine) API
def calcdist(lon1,lat1,lon2,lat2):
    r = requests.get(f"http://router.project-osrm.org/route/v1/car/{lon1},{lat1};{lon2},{lat2}?overview=false""")
    routes = json.loads(r.content)
    route_1 = routes.get("routes")[0]
    return route_1['distance']

data = pd.read_csv('dataset.csv')
data = data.drop("Elevation", axis = 1)
array = data.values[:,1:3]
distancematrix = np.zeros(26*26).reshape(26,26)
for x in range(26):
  x1,x2 = array[x] 
  for y in range(26):
    y1,y2 = array[y]
    if x==y: continue
    distancematrix[x,y] = calcdist(x1,x2,y1,y2)
    print(distancematrix[x,y])
    
#Converting distance unit to kilometers
distancematrix = distancematrix/1000