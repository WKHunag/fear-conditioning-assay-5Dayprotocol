# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 12:29:56 2021

@author: 8C08-2
"""

import pandas as pd
import numpy as np

path = r'G:\fear conditioning assay data'
genotypes = ['Wtsibling','Hetero','Homo']
locations = ['LD','LT','RD','RT']
Set = ['1','2']

for Set in Set:
    for genotype in genotypes:
        for location in locations:
            try:
                for y in ['1','2','3','4','5']:
                   if y == '5':
                       vars()['data5'] = pd.read_hdf(path+"\Day 5\Training Day5 Shank3b NeuroD "+genotype+"_"+location+" "+Set+"DLC_resnet50_trackJun18shuffle1_77000.h5")
                       vars()['data6'] = pd.read_hdf(path+"\Day 5\Testing Day5 Shank3b NeuroD "+genotype+"_"+location+" "+Set+"DLC_resnet50_trackJun18shuffle1_77000.h5")
                   else:
                       vars()['data'+str(y)]= pd.read_hdf(path+'\Day '+y+'\Day'+y+'Shank3b NeuroD '+genotype+'_'+location+' '+Set+'DLC_resnet50_trackJun18shuffle1_77000.h5')
             
      
                for j in range(1,7):
                    vars()['nose'+str(j)] = vars()['data'+str(j)]['DLC_resnet50_trackJun18shuffle1_77000']['nose'][['x','y']]
                    vars()['righteye'+str(j)] = vars()['data'+str(j)]['DLC_resnet50_trackJun18shuffle1_77000']['righteye'][['x','y']]
                    vars()['lefteye'+str(j)] = vars()['data'+str(j)]['DLC_resnet50_trackJun18shuffle1_77000']['lefteye'][['x','y']]
                    vars()['body'+str(j)] = vars()['data'+str(j)]['DLC_resnet50_trackJun18shuffle1_77000']['body'][['x','y']]
    
    
        
                col = pd.MultiIndex.from_arrays([np.hstack((np.array(['Day 1']*8),np.array(['Day 2']*8),np.array(['Day 3']*8),np.array(['Day 4']*8),np.array(['Day 5']*8),np.array(['Testing']*8))),
                                         np.array(['nose','nose','righteye','righteye','lefteye','lefteye','body','body']*6),np.array(['x','y']*24)])
        
                vars()[genotype+location+Set] = pd.DataFrame(pd.concat([nose1,righteye1,lefteye1,body1,nose2,righteye2,lefteye2,body2,nose3,righteye3,lefteye3,body3,nose4,righteye4,lefteye4,body4,nose5,righteye5,lefteye5,body5,nose6,righteye6,lefteye6,body6],axis=1).values,columns=col)
            except : 
                pass


