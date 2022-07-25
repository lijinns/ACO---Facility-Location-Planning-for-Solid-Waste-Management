# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 20:51:58 2022

@author: Lijin N S
"""

import pandas as pd
import numpy as np
import requests
import json 
import random
from itertools import permutations

#Defining functions used in the code

def part(a,b, phmap,dmap, alpha = 1, beta = 5):
    '''Function to calculate a term of numerator of the probability function.'''
    return (phmap[a,b]**alpha)*((1/dmap[a,b])**beta)

def probdenom(row,columnlist,phmap,dmap,alpha = 1, beta = 5):
    '''Function to calculate the denominator of the probability function.'''
    sum = 0
    for x in columnlist:
        sum += part(row,x,phmap,dmap,alpha,beta)
    return sum

def setrandom(node,visit,denom,phmap,dmap,alpha = 1, beta = 5):
  '''Function to create a list of probabilities of node to visit and then 
       create a roulette wheel of probabilities(summation per iteration).'''
  numprob = []
  sum = 0
  for x in visit:
    sum += part(node,x,phmap,dmap,alpha,beta)/denom
    numprob.append(sum)
  return numprob

def chooserandom(probset):
  '''Function to choose a location to visit next probabilistically'''
  rwvar = random.random()
  for x in range(len(probset)):
    if rwvar <= probset[x]:
      return x
  return x

def totaldist(distmatrix,path):
    '''Function to calculate the total distance covered by a path'''
    sum = 0
    for x in range(len(path)-1):
        sum += distmatrix[path[x],path[x+1]]
    return sum

def phupdate(phmatrix,path,td):
    '''Function to update pheromone trail in path covered'''
    for x in range(len(path)-1):
        phmatrix[path[x],path[x+1]] += td**-1