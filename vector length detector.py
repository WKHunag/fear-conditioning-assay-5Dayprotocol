# @jit(nopython=True)
def VectorslenGenerator(data):
    df1 = data['Day 1'].dropna()
    df2 = data['Day 2'].dropna()
    df3 = data['Day 3'].dropna()
    df4 = data['Day 4'].dropna()
    df5 = data['Day 5'].dropna()
    df6 = data['Testing'].dropna()
    dfs = [df1,df2,df3,df4,df5,df6]
    
    z = [
            [np.dot(i.values[j],i.values[j])
                            for j in range(0,len(i))]
                            for i in dfs]
    df = pd.concat([pd.DataFrame({'Day 1':z[0]}),pd.DataFrame({'Day 2':z[1]}),pd.DataFrame({'Day 3':z[2]}),pd.DataFrame({'Day 4':z[3]}),pd.DataFrame({'Day 5':z[4]}),pd.DataFrame({'Testing':z[5]})],axis=1)
    df = np.sqrt(df)
    return df

Sets = ['1','2']
locations = ['LT','RT','RD','LD']

for Set in Sets:
    for genotype in genotypes:
        if Set == '2' and genotype == 'Homo':
            try : locations.remove('LD')
            except ValueError: pass
        for location in locations:
            vars()[genotype+location+Set+'vectorslen'] = VectorslenGenerator(globals()[genotype+location+Set+'vectors'])