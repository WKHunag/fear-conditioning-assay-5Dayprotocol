# -*- coding: utf-8 -*-
"""
Created on Mon Aug 16 09:30:42 2021

@author: DELL_04
"""
def anguarvelocityDetecter(vec,veclen):
    vec1 = vec['Day 1'].dropna()
    vec2 = vec['Day 2'].dropna()
    vec3 = vec['Day 3'].dropna()
    vec4 = vec['Day 4'].dropna()
    vec5 = vec['Day 5'].dropna()
    vec6 = vec['Testing'].dropna()
    vecs = [vec1,vec2,vec3,vec4,vec5,vec6]
    veclen1 = veclen['Day 1'].dropna()
    veclen2 = veclen['Day 2'].dropna()
    veclen3 = veclen['Day 3'].dropna()
    veclen4 = veclen['Day 4'].dropna()
    veclen5 = veclen['Day 5'].dropna()
    veclen6 = veclen['Testing'].dropna()
    veclens = [veclen1,veclen2,veclen3,veclen4,veclen5,veclen6]
   
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