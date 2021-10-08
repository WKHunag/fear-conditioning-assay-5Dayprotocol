# -*- coding: utf-8 -*-
"""
Created on Mon Aug 16 11:55:24 2021

@author: DELL_04
"""
import pandas as pd
path = r'G:\fear conditioning assay data\electric data'
genotypes = ['Wtsibling','Hetero','Homo']
Set = ['1','2']

for Set in Set:
    for genotype in genotypes:
        for y in ['1','2','3','4','5']:
            if y == '5':
                vars()['eData5'] = pd.read_csv(path+"\Day 5\Training Day 5shank3b neuroD "+genotype+"_electricityData "+Set+".csv",index_col=(0))
                vars()['eData6'] = pd.read_csv(path+"\Day 5\Testing Day 5shank3b neuroD "+genotype+"_electricityData "+Set+".csv",index_col=(0))
            else:
                vars()['eData'+str(y)]= pd.read_csv(path+'\Day '+y+'\Day '+y+'shank3b neuroD '+genotype+'_electricityData '+Set+'.csv',index_col=(0))
            
        vars()[genotype+Set+'eData'] = pd.DataFrame(pd.concat([eData1,
                                                                            eData2,
                                                                            eData3,
                                                                            eData4,
                                                                            eData5,
                                                                            eData6],axis=1).values,
                                                                 columns = pd.MultiIndex.from_arrays([np.hstack((np.array(['Day 1']*3),np.array(['Day 2']*3),np.array(['Day 3']*3),np.array(['Day 4']*3),np.array(['Day 5']*3),np.array(['Testing']*3))),
                                     np.array(['redLED','greenLED','shock timing']*6)]))
            
