# -*- coding: utf-8 -*-
"""
Created on Mon Aug 16 13:21:19 2021

@author: DELL_04
"""
import numpy as np
import pandas as pd

def periodgenerator(CSVdata):
  df1 = CSVdata.iloc[:,0]
  df2 = CSVdata.iloc[:,1]
  list1 = list(np.where(df1 == 1)[0])
  list2 = list(np.where(df2 == 1)[0])
  redLED = []
  boo1 = True
  i = 0
  j = 0
  while boo1:
    i += 1
    if list1[i]-list1[i-1] != 1:
        redLED.insert(j,list1[:i])
        j += 1
        del list1[:i]
        i = 0
    elif len(list1) <= 300: 
        j += 1
        redLED.insert(j,list1)
        del list1
        boo1 = False
  grnLED = []
  boo2 = True
  x = 0
  y = 0
  while boo2:
    x += 1
    if list2[x]-list2[x-1] != 1:
        grnLED.insert(y,list2[:x])
        y += 1
        del list2[:x]
        x = 0
    elif len(list2) <= 1000: 
        y += 1
        grnLED.insert(y,list2)
        del list2
        boo2 = False        
        
  timingdf = pd.concat([pd.DataFrame({'redLED':redLED}),pd.DataFrame({'greenLED':grnLED})],axis=1)
  return timingdf

Daynus = ['Day1','Day2','Day3','Day4','Day5','Testing']
Days = ['Day 1','Day 2','Day 3','Day 4','Day 5','Testing']
for genotype in genotypes:
    for Set in Sets:
        for Day,Daynu in zip(Days,Daynus):
            vars()[genotype+Set+Daynu+'timingdf'] = periodgenerator(locals()[genotype+Set+'eData'][Day])
            
