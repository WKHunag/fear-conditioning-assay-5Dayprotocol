# -*- coding: utf-8 -*-
"""
Created on Mon Aug 16 09:30:42 2021

@author: DELL_04
"""
def anguarvelocityDetecter(vec,veclen):
    vecs = [vec['Day '+str(i)].dropna() for i in range(1,6)].append(vec['Testing'].dropna())
    veclens= [veclen['Day '+str(i)].dropna() for i in range(1, 6)].append(veclen['Testing'].dropna())
   
    cosangles = [
               [np.dot(vec.iloc[i],vec.iloc[i+1])/(veclen[i]*veclen[i+1])
               for i in vec.index.drop(max(vec.index))]
               for vec,veclen in zip(vecs,veclens)
               ]
    cosangledf = pd.concat([pd.DataFrame({'Day 1':cosangles[0]}),
                            pd.DataFrame({'Day 2':cosangles[1]}),
                            pd.DataFrame({'Day 3':cosangles[2]}),
                            pd.DataFrame({'Day 4':cosangles[3]}),
                            pd.DataFrame({'Day 5':cosangles[4]}),
                            pd.DataFrame({'Testing':cosangles[5]})],axis=1)
    cosangledf[cosangledf<-1] = -1
    cosangledf[cosangledf>1] = 1
    angledf = np.arccos(cosangledf)
    angularVdf = angledf*360/(2*np.pi)/8.333
    return angularVdf

Sets = ['1','2']
locations = ['LT','LD','RT','RD']
for location in locations:
    for genotype in genotypes:
        try:
            for Set in Sets:
                vars()[genotype+location+Set+'AV'] = anguarvelocityDetecter(globals()[genotype+location+Set+'vectors'],globals()[genotype+location+Set+'vectorslen'])
        except:
            pass
