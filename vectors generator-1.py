# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 15:58:22 2021

@author: 8C08-2
"""

genotypes = ['Wtsibling','Hetero','Homo']
locations = ['LT','RD','RT','LD']
Set = ['1','2']
Days = ['1','2','3','4','5','Testing']
for Set in Set:
    for genotype in genotypes:
        if Set == '2' and genotype == 'Homo':
            try : locations.remove('LD')
            except ValueError: pass
        for location in locations:
            for Day in Days:
                try :
                   vars()[genotype+location+Set+'vectorsDay'+Day]=globals()[genotype+location+Set]['Day '+Day]['nose']-(globals()[genotype+location+Set]['Day '+Day]['righteye']+globals()[genotype+location+Set]['Day '+Day]['lefteye'])/2
                except KeyError: 
                   vars()[genotype+location+Set+'vectorsTesting']=globals()[genotype+location+Set]['Testing']['nose']-(globals()[genotype+location+Set]['Testing']['righteye']+globals()[genotype+location+Set]['Testing']['lefteye'])/2
            vars()[genotype+location+Set+'vectors'] = pd.DataFrame(pd.concat([vars()[genotype+location+Set+'vectorsDay1'],vars()[genotype+location+Set+'vectorsDay2'],vars()[genotype+location+Set+'vectorsDay3'],vars()[genotype+location+Set+'vectorsDay4'],vars()[genotype+location+Set+'vectorsDay5'],vars()[genotype+location+Set+'vectorsTesting']],axis=1).values,columns =pd.MultiIndex.from_arrays([np.hstack((np.array(['Day 1']*2),np.array(['Day 2']*2),np.array(['Day 3']*2),np.array(['Day 4']*2),np.array(['Day 5']*2),np.array(['Testing']*2))),np.array(['x','y']*6)]))
            
            
