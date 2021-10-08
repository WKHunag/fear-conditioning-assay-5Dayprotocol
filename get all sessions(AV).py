# -*- coding: utf-8 -*-
"""
Created on Mon Aug 16 16:35:05 2021

@author: DELL_04
"""
def GetAllSession(genotype,Day,Daynu,period,VCcolor):
#    genotypes = ['Hetero','Homo','Wtsibling']
    locations = ['RT','RD','LT','LD']
    Sets = ['1','2']
    if Day == 'Day 1':
        if period == 'Baseline':
            for location in locations:
                for Set in Sets:    
                    try:
                        vars()[genotype+location+Set+period+Daynu] = np.array([
                             globals()[genotype+location+Set+'AV'][Day][min(globals()[genotype+Set+Daynu+'timingdf'][VCcolor].dropna()[i])-240:min(globals()[genotype+Set+Daynu+'timingdf'][VCcolor].dropna()[i])+480]
                                                    for i in range(0,2)#if red range(0,8) if grn range(0,2)
                                                    
                              ])
                    except: 
                            pass
            try:
                a = {genotype+'LD1'+period:locals()[genotype+'LD1'+period+Daynu],
                                                 genotype+'LD2'+period:locals()[genotype+'LD2'+period+Daynu],
                                                 genotype+'LT1'+period:locals()[genotype+'LT1'+period+Daynu],
                                                 genotype+'LT2'+period:locals()[genotype+'LT2'+period+Daynu],
                                                 genotype+'RD1'+period:locals()[genotype+'RD1'+period+Daynu],
                                                 genotype+'RD2'+period:locals()[genotype+'RD2'+period+Daynu],
                                                 genotype+'RT1'+period:locals()[genotype+'RT1'+period+Daynu],
                                                 genotype+'RT2'+period:locals()[genotype+'RT2'+period+Daynu]}
            except:
                a = {genotype+'LD1'+period:locals()[genotype+'LD1'+period+Daynu],
                                                 genotype+'LT1'+period:locals()[genotype+'LT1'+period+Daynu],
                                                 genotype+'LT2'+period:locals()[genotype+'LT2'+period+Daynu],
                                                 genotype+'RD1'+period:locals()[genotype+'RD1'+period+Daynu],
                                                 genotype+'RD2'+period:locals()[genotype+'RD2'+period+Daynu],
                                                 genotype+'RT1'+period:locals()[genotype+'RT1'+period+Daynu],
                                                 genotype+'RT2'+period:locals()[genotype+'RT2'+period+Daynu]}
            return  a
        elif period == 'Training':
            for location in locations:
                for Set in Sets:
                    try:
                        vars()[genotype+location+Set+period+Daynu] = np.array([
                             globals()[genotype+location+Set+'AV'][Day][min(globals()[genotype+Set+Daynu+'timingdf'][VCcolor].dropna()[i])-240:min(globals()[genotype+Set+Daynu+'timingdf'][VCcolor].dropna()[i])+480] 
                                                    for i in range(2,len(globals()[genotype+Set+Daynu+'timingdf'][VCcolor].dropna().values))
                                                    
                         ])
                    except:
                        pass
            try:
                a = {genotype+'LD1'+period:locals()[genotype+'LD1'+period+Daynu],
                                                 genotype+'LD2'+period:locals()[genotype+'LD2'+period+Daynu],
                                                 genotype+'LT1'+period:locals()[genotype+'LT1'+period+Daynu],
                                                 genotype+'LT2'+period:locals()[genotype+'LT2'+period+Daynu],
                                                 genotype+'RD1'+period:locals()[genotype+'RD1'+period+Daynu],
                                                 genotype+'RD2'+period:locals()[genotype+'RD2'+period+Daynu],
                                                 genotype+'RT1'+period:locals()[genotype+'RT1'+period+Daynu],
                                                 genotype+'RT2'+period:locals()[genotype+'RT2'+period+Daynu]}
            except:
                a = {genotype+'LD1'+period:locals()[genotype+'LD1'+period+Daynu],
                                                 genotype+'LT1'+period:locals()[genotype+'LT1'+period+Daynu],
                                                 genotype+'LT2'+period:locals()[genotype+'LT2'+period+Daynu],
                                                 genotype+'RD1'+period:locals()[genotype+'RD1'+period+Daynu],
                                                 genotype+'RD2'+period:locals()[genotype+'RD2'+period+Daynu],
                                                 genotype+'RT1'+period:locals()[genotype+'RT1'+period+Daynu],
                                                 genotype+'RT2'+period:locals()[genotype+'RT2'+period+Daynu]}
            return  a
        
                
    elif Day !='Day 1' and Day !='Testing':
        period = 'Training'
        for location in locations:
            for Set in Sets:
                try:
                    vars()[genotype+location+Set+period+Daynu] = np.array([
                         globals()[genotype+location+Set+'AV'][Day][min(globals()[genotype+Set+Daynu+'timingdf'][VCcolor].dropna()[i])-240:min(globals()[genotype+Set+Daynu+'timingdf'][VCcolor].dropna()[i])+480] 
                                                for i in range(0,len(globals()[genotype+Set+Daynu+'timingdf'][VCcolor].dropna().values))
                                                
                         ])
                except:
                    pass
        try:
            a = {genotype+'LD1'+period:locals()[genotype+'LD1'+period+Daynu],
                                                 genotype+'LD2'+period:locals()[genotype+'LD2'+period+Daynu],
                                                 genotype+'LT1'+period:locals()[genotype+'LT1'+period+Daynu],
                                                 genotype+'LT2'+period:locals()[genotype+'LT2'+period+Daynu],
                                                 genotype+'RD1'+period:locals()[genotype+'RD1'+period+Daynu],
                                                 genotype+'RD2'+period:locals()[genotype+'RD2'+period+Daynu],
                                                 genotype+'RT1'+period:locals()[genotype+'RT1'+period+Daynu],
                                                 genotype+'RT2'+period:locals()[genotype+'RT2'+period+Daynu]}
        except:
            a = {genotype+'LD1'+period:locals()[genotype+'LD1'+period+Daynu],
                                             genotype+'LT1'+period:locals()[genotype+'LT1'+period+Daynu],
                                             genotype+'LT2'+period:locals()[genotype+'LT2'+period+Daynu],
                                             genotype+'RD1'+period:locals()[genotype+'RD1'+period+Daynu],
                                             genotype+'RD2'+period:locals()[genotype+'RD2'+period+Daynu],
                                             genotype+'RT1'+period:locals()[genotype+'RT1'+period+Daynu],
                                             genotype+'RT2'+period:locals()[genotype+'RT2'+period+Daynu]}
        return  a
                       
    elif Day == 'Testing':
        period = 'Testing'
        for location in locations:
            for Set in Sets:
                try:
                    vars()[genotype+location+Set+period] = np.array([
                         globals()[genotype+location+Set+'AV'][Day][min(globals()[genotype+Set+period+'timingdf'][VCcolor].dropna()[i])-240:min(globals()[genotype+Set+period+'timingdf'][VCcolor].dropna()[i])+480] 
                                                for i in range(0,len(globals()[genotype+Set+period+'timingdf'][VCcolor].dropna().values))
                                                
                         ])
                except:pass
        try:
            a = {genotype+'LD1'+Daynu:locals()[genotype+'LD1'+period],
                                                 genotype+'LD2'+Daynu:locals()[genotype+'LD2'+period],
                                                 genotype+'LT1'+Daynu:locals()[genotype+'LT1'+period],
                                                 genotype+'LT2'+Daynu:locals()[genotype+'LT2'+period],
                                                 genotype+'RD1'+Daynu:locals()[genotype+'RD1'+period],
                                                 genotype+'RD2'+Daynu:locals()[genotype+'RD2'+period],
                                                 genotype+'RT1'+Daynu:locals()[genotype+'RT1'+period],
                                                 genotype+'RT2'+Daynu:locals()[genotype+'RT2'+period]}
        except:
            a = {genotype+'LD1'+Daynu:locals()[genotype+'LD1'+period],
                                             genotype+'LT1'+Daynu:locals()[genotype+'LT1'+period],
                                             genotype+'LT2'+Daynu:locals()[genotype+'LT2'+period],
                                             genotype+'RD1'+Daynu:locals()[genotype+'RD1'+period],
                                             genotype+'RD2'+Daynu:locals()[genotype+'RD2'+period],
                                             genotype+'RT1'+Daynu:locals()[genotype+'RT1'+period],
                                             genotype+'RT2'+Daynu:locals()[genotype+'RT2'+period]}
        return  a
    else:
        print('check parameter')




        