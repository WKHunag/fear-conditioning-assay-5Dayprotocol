# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 11:35:05 2021

@author: DELL_04
"""
import matplotlib.pyplot as plt



def papulation(genotype,period,Day,datacolor=''):
    if period == 'Baseline' or period == 'Testing':
        try:
            vars()[genotype+period+'papulation'] = np.array([
                np.mean(globals()[genotype+period+'session'+datacolor][genotype+location+Set+period],axis=0) 
                for location in locations
                for Set in Sets
                ])
            return vars()[genotype+period+'papulation']
        except:
            vars()[genotype+period+'papulation'] = np.array([
                np.mean(globals()[genotype+period+'session'+datacolor][genotype+locationSet+period],axis=0) 
                for locationSet in ['RD1','RD2','RT1','RT2','LT1','LT2','LD1']
                ])
            return vars()[genotype+period+'papulation']
    elif period == 'Training':
        try:
            vars()[genotype+period+Day.replace(' ','')+'papulation'] = np.array([
                np.mean(globals()[genotype+Day.replace(' ','')+period+'session'+datacolor][genotype+location+Set+period],axis=0) 
                for location in locations
                for Set in Sets
                ])
            return vars()[genotype+period+Day.replace(' ','')+'papulation']
        except:
            vars()[genotype+period+Day.replace(' ','')+'papulation'] = np.array([
                np.mean(globals()[genotype+Day.replace(' ','')+period+'session'+datacolor][genotype+locationSet+period],axis=0) 
                for locationSet in ['RD1','RD2','RT1','RT2','LT1','LT2','LD1']
                ])
            return vars()[genotype+period+Day.replace(' ','')+'papulation']


def SingleGenoPopFigure(figsize,genotype,period,Day,ymax,VCcolor,datacolor=''):
    fig, ax = plt.subplots(figsize = figsize)
    data = papulation(genotype,period,Day,datacolor)
    for i in range(0,len(data)):
        ax.plot(data[i,:],color = 'black',alpha = 0.2)
    ax.plot(np.mean(data,axis=0),color = 'black')
    ax.bar(420,ymax,color = VCcolor,width=360,alpha = 0.2)
    plt.tick_params(labelsize=65,length=12,width=5)
    ax.set_ylabel('Angular Velocity',fontsize=75)
    ax.set_xlabel('Frames',fontsize=75)
    ax.spines['top'].set_linewidth(5)
    ax.spines['right'].set_linewidth(5)
    ax.spines['bottom'].set_linewidth(5)
    ax.spines['left'].set_linewidth(5)
    if period == 'Baseline'or period =='Testing':
        ax.set_title(genotype+' '+period,fontsize = 80)
    else:
        ax.set_title(genotype+' '+Day.replace(' ','')+' '+period,fontsize = 80)
        if VCcolor == 'red':
            ax.bar(460,ymax,color = 'navy',width=80,alpha = 0.2)
        else:
            pass
    ax.set_xlim(0, 750)
    ax.set_ylim(0,ymax)
    plt.yticks(np.arange(0,ymax))
    plt.xticks(np.arange(0, 720, 120))

def MultiGenoPopFigure(figsize,period,Day,VCcolor,datacolor=''):
    fig, ax = plt.subplots(figsize = figsize)
    data1 = papulation('Wtsibling',period,Day,datacolor)
    data2 = papulation('Hetero',period,Day,datacolor)
    data3 = papulation('Homo', period, Day,datacolor)
    ax.plot(np.mean(data1,axis=0),color = 'black')
    ax.plot(np.mean(data2,axis=0),color = 'blue')
    ax.plot(np.mean(data3,axis=0),color = 'red')
    plt.tick_params(labelsize=65,length=12,width=5)
    ax.set_ylabel('Angular Velocity',fontsize=75)
    ax.set_xlabel('Frames',fontsize=75)
    ax.bar(420,np.amax(np.concatenate((np.mean(data1,axis=0),np.mean(data2,axis=0),np.mean(data3,axis=0))))+0.5,color = VCcolor,width=360,alpha = 0.2)
    ax.spines['top'].set_linewidth(5)
    ax.spines['right'].set_linewidth(5)
    ax.spines['bottom'].set_linewidth(5)
    ax.spines['left'].set_linewidth(5)
    if period == 'Baseline'or period =='Testing':
        ax.set_title('Multigenotype'+' '+period,fontsize = 80)
    else:
       ax.set_title('Multigenotype'+' '+Day.replace(' ','')+' '+period,fontsize = 80)
       if VCcolor == 'red':
           ax.bar(460,np.amax(np.concatenate((np.mean(data1,axis=0),np.mean(data2,axis=0),np.mean(data3,axis=0))))+0.5,color = 'navy',width=80,alpha = 0.2)
       else: pass
    ax.set_xlim(0, 7500)
    ax.set_ylim(0,np.amax(np.concatenate((np.mean(data1,axis=0),np.mean(data2,axis=0),np.mean(data3,axis=0))))+0.5)
    plt.xticks(np.arange(0, 720),np.arange(0,6000))
    plt.yticks(np.arange(0,np.amax(np.concatenate((np.mean(data1,axis=0),np.mean(data2,axis=0),np.mean(data3,axis=0))))+0.5,0.5))
    
def Singlefishbehaviorresponse(figsize,genotype,datacolor=''):
    fig, ax = plt.subplots(figsize = figsize)
    plt.tick_params(labelsize=65,length=12,width=5)
    ax.set_ylabel('Behavioral response',fontsize=75)
    # ax.set_xlabel('Conditions',fontsize=75)
    plt.xticks(np.arange(0,7),['pre','Day1\ntrain','Day2\ntrain','Day3\ntrain','Day4\ntrain','Day5\ntrain','post'])
    ax.set_title(genotype,fontsize = 80)
    ax.spines['top'].set_linewidth(5)
    ax.spines['right'].set_linewidth(5)
    ax.spines['bottom'].set_linewidth(5)
    ax.spines['left'].set_linewidth(5)
    if genotype != 'Homo':
        baseline = np.array([np.mean([np.mean(globals()[genotype+'Baselinesession'+datacolor][genotype+i+'Baseline'][j][240:250])-np.mean(globals()[genotype+'Baselinesession'+datacolor][genotype+i+'Baseline'][j][230:240]) for j in range(0,8)]) for i in ['LD1','LD2','LT1','LT2','RD1','RD2','RT1','RT2']])
        training1 = np.array([np.mean([np.mean(globals()[genotype+'Day1'+'Trainingsession'+datacolor][genotype+i+'Training'][j][240:250])-np.mean(globals()[genotype+'Day1'+'Trainingsession'+datacolor][genotype+i+'Training'][j][230:240]) for j in range(0,16)]) for i in ['LD1','LD2','LT1','LT2','RD1','RD2','RT1','RT2']])
        training2 = np.array([np.mean([np.mean(globals()[genotype+'Day2'+'Trainingsession'+datacolor][genotype+i+'Training'][j][240:250])-np.mean(globals()[genotype+'Day2'+'Trainingsession'+datacolor][genotype+i+'Training'][j][230:240]) for j in range(0,16)]) for i in ['LD1','LD2','LT1','LT2','RD1','RD2','RT1','RT2']])
        training3 = np.array([np.mean([np.mean(globals()[genotype+'Day3'+'Trainingsession'+datacolor][genotype+i+'Training'][j][240:250])-np.mean(globals()[genotype+'Day3'+'Trainingsession'+datacolor][genotype+i+'Training'][j][230:240]) for j in range(0,16)]) for i in ['LD1','LD2','LT1','LT2','RD1','RD2','RT1','RT2']])
        training4 = np.array([np.mean([np.mean(globals()[genotype+'Day4'+'Trainingsession'+datacolor][genotype+i+'Training'][j][240:250])-np.mean(globals()[genotype+'Day4'+'Trainingsession'+datacolor][genotype+i+'Training'][j][230:240]) for j in range(0,16)]) for i in ['LD1','LD2','LT1','LT2','RD1','RD2','RT1','RT2']])
        training5 = np.array([np.mean([np.mean(globals()[genotype+'Day5'+'Trainingsession'+datacolor][genotype+i+'Training'][j][240:250])-np.mean(globals()[genotype+'Day5'+'Trainingsession'+datacolor][genotype+i+'Training'][j][230:240]) for j in range(0,16)]) for i in ['LD1','LD2','LT1','LT2','RD1','RD2','RT1','RT2']])
        testing = np.array([np.mean([np.mean(globals()[genotype+'Testingsession'+datacolor][genotype+i+'Testing'][j][240:250])-np.mean(globals()[genotype+'Testingsession'+datacolor][genotype+i+'Testing'][j][230:240]) for j in range(0,15)]) for i in ['LD1','LD2','LT1','LT2','RD1','RD2','RT1','RT2']])
        for i,j in zip(['LD1','LD2','LT1','LT2','RD1','RD2','RT1','RT2'],range(0,8)):
            vars()[i] = np.array([baseline[j],training1[j],training2[j],training3[j],training4[j],training5[j],testing[j]])
            ax.plot(locals()[i])
        a = np.mean([locals()['LD1'],locals()['LD2'],locals()['LT1'],locals()['LT2'],locals()['RD1'],
                                  locals()['RD2'],locals()['RT1'],locals()['RT2']],axis=0)
        ax.plot(a,color='black',linewidth=5)
        return a
    else:
        baseline = np.array([np.mean([np.mean(globals()[genotype+'Baselinesession'+datacolor][genotype+i+'Baseline'][j][240:250])-np.mean(globals()[genotype+'Baselinesession'+datacolor][genotype+i+'Baseline'][j][230:240]) for j in range(0,8)]) for i in ['LD1','LT1','LT2','RD1','RD2','RT1','RT2']])
        training1 = np.array([np.mean([np.mean(globals()[genotype+'Day1'+'Trainingsession'+datacolor][genotype+i+'Training'][j][240:250])-np.mean(globals()[genotype+'Day1'+'Trainingsession'+datacolor][genotype+i+'Training'][j][230:240]) for j in range(0,16)]) for i in ['LD1','LT1','LT2','RD1','RD2','RT1','RT2']])
        training2 = np.array([np.mean([np.mean(globals()[genotype+'Day2'+'Trainingsession'+datacolor][genotype+i+'Training'][j][240:250])-np.mean(globals()[genotype+'Day2'+'Trainingsession'+datacolor][genotype+i+'Training'][j][230:240]) for j in range(0,16)]) for i in ['LD1','LT1','LT2','RD1','RD2','RT1','RT2']])
        training3 = np.array([np.mean([np.mean(globals()[genotype+'Day3'+'Trainingsession'+datacolor][genotype+i+'Training'][j][240:250])-np.mean(globals()[genotype+'Day3'+'Trainingsession'+datacolor][genotype+i+'Training'][j][230:240]) for j in range(0,16)]) for i in ['LD1','LT1','LT2','RD1','RD2','RT1','RT2']])
        training4 = np.array([np.mean([np.mean(globals()[genotype+'Day4'+'Trainingsession'+datacolor][genotype+i+'Training'][j][240:250])-np.mean(globals()[genotype+'Day4'+'Trainingsession'+datacolor][genotype+i+'Training'][j][230:240]) for j in range(0,16)]) for i in ['LD1','LT1','LT2','RD1','RD2','RT1','RT2']])
        training5 = np.array([np.mean([np.mean(globals()[genotype+'Day5'+'Trainingsession'+datacolor][genotype+i+'Training'][j][240:250])-np.mean(globals()[genotype+'Day5'+'Trainingsession'+datacolor][genotype+i+'Training'][j][230:240]) for j in range(0,16)]) for i in ['LD1','LT1','LT2','RD1','RD2','RT1','RT2']])
        testing = np.array([np.mean([np.mean(globals()[genotype+'Testingsession'+datacolor][genotype+i+'Testing'][j][240:250])-np.mean(globals()[genotype+'Testingsession'+datacolor][genotype+i+'Testing'][j][230:240]) for j in range(0,16)]) for i in ['LD1','LT1','LT2','RD1','RD2','RT1','RT2']])
        for i,j in zip(['LD1','LT1','LT2','RD1','RD2','RT1','RT2'],range(0,7)):
            vars()[i] = np.array([baseline[j],training1[j],training2[j],training3[j],training4[j],training5[j],testing[j]])
            ax.plot(locals()[i])
        a = np.mean([locals()['LD1'],locals()['LT1'],locals()['LT2'],locals()['RD1'],
                                  locals()['RD2'],locals()['RT1'],locals()['RT2']],axis=0)
        ax.plot(a,color='black',linewidth=5)
        return a
def BehavioralResponsetrend(figsize,datacolor=''):
    a = Singlefishbehaviorresponse(figsize, 'Wtsibling',datacolor)
    b = Singlefishbehaviorresponse(figsize, 'Hetero',datacolor)
    c = Singlefishbehaviorresponse(figsize, 'Homo',datacolor)
    fig, ax2 = plt.subplots(figsize=figsize)
    ax2.plot(a,color = 'black',linewidth=5,label='Wtsibling')
    ax2.plot(b,color = 'blue',linewidth=5,label='Hetero')
    ax2.plot(c,color = 'red',linewidth=5,label='Homo')
    plt.tick_params(labelsize=35,length=12,width=5)
    ax2.set_ylabel('Behavioral response',fontsize=45)
    # ax2.set_xlabel('Conditions',fontsize=45)
    plt.xticks(np.arange(0,7),['pre','Day1\ntrain','Day2\ntrain','Day3\ntrain','Day4\ntrain','Day5\ntrain','post'])
    # ax2.set_title('Multigenotype Behavioral response Trend',fontsize = 50)
    ax2.spines['top'].set_linewidth(5)
    ax2.spines['right'].set_linewidth(5)
    ax2.spines['bottom'].set_linewidth(5)
    ax2.spines['left'].set_linewidth(5)
    ax2.legend(loc='upper left',fontsize=20)
    


def BRchanged(figsize,genotype):
    if genotype == 'Homo':
        baseline = np.array([np.mean([np.mean(globals()[genotype+'Baselinesession'][genotype+i+'Baseline'][j][240:250])-np.mean(globals()[genotype+'Baselinesession'][genotype+i+'Baseline'][j][230:240]) for j in range(0,8)]) for i in ['LD1','LT1','LT2','RD1','RD2','RT1','RT2']])
        training = np.array([np.mean([np.mean(globals()[genotype+'Testingsession'][genotype+i+'Testing'][j][240:250])-np.mean(globals()[genotype+'Day1'+'Trainingsession'][genotype+i+'Training'][j][230:240]) for j in range(0,16)]) for i in ['LD1','LT1','LT2','RD1','RD2','RT1','RT2']])
        x = np.transpose(np.array([baseline,training]))
        baseline_mean = np.mean(baseline)
        training_mean = np.mean(training)
        baseline_err = stats.sem(baseline)
        training_err = stats.sem(training)
        fig,ax = plt.subplots(figsize=figsize)
        ax.bar(['pre','Day1\nsession 9-16'],[baseline_mean,training_mean],color=(0,0,0,0),edgecolor=['black','red'],linewidth=5,yerr=[baseline_err,training_err],capsize=20)
        for i,m in zip(range(0,7),['o','*','^','v','s','d','8']):
            ax.scatter(['pre','Day1\nsession 9-16'],x[i],marker=m,color='black',s=100)
        ax.set_title(genotype+' Behavioral Response Variety',fontsize=50)
        ax.spines['top'].set_linewidth(5)
        ax.spines['right'].set_linewidth(5)
        ax.spines['bottom'].set_linewidth(5)
        ax.spines['left'].set_linewidth(5)
        ax.set_xlabel('Condition',fontsize=45)
        ax.set_ylabel('Behavioral Response',fontsize=45)
        plt.tick_params(labelsize=35,length=10,width=5)
        return baseline,training,baseline_mean,training_mean,baseline_err,training_err
    else:
        baseline = np.array([np.mean([np.mean(globals()[genotype+'Baselinesession'][genotype+i+'Baseline'][j][240:250])-np.mean(globals()[genotype+'Baselinesession'][genotype+i+'Baseline'][j][230:240]) for j in range(0,8)]) for i in ['LD1','LD2','LT1','LT2','RD1','RD2','RT1','RT2']])
        training = np.array([np.mean([np.mean(globals()[genotype+'Testingsession'][genotype+i+'Testing'][j][240:250])-np.mean(globals()[genotype+'Day1'+'Trainingsession'][genotype+i+'Training'][j][230:240]) for j in range(0,15)]) for i in ['LD1','LD2','LT1','LT2','RD1','RD2','RT1','RT2']])
        x = np.transpose(np.array([baseline,training]))
        baseline_mean = np.mean(baseline)
        training_mean = np.mean(training)
        baseline_err = stats.sem(baseline)
        training_err = stats.sem(training)
        fig,ax = plt.subplots(figsize=figsize)
        ax.bar(['pre','Day1\nsession 9-16'],[baseline_mean,training_mean],color=(0,0,0,0),edgecolor=['black','red'],linewidth=5,yerr=[baseline_err,training_err],capsize=20)
        for i,m in zip(range(0,8),['o','*','^','v','s','d','8','+']):
            ax.scatter(['pre','Day1\nsession 9-16'],x[i],marker=m,color='black',s=100)
        ax.set_title(genotype+' Behavioral Response Variety',fontsize=50)
        ax.spines['top'].set_linewidth(5)
        ax.spines['right'].set_linewidth(5)
        ax.spines['bottom'].set_linewidth(5)
        ax.spines['left'].set_linewidth(5)
        ax.set_xlabel('Condition',fontsize=45)
        ax.set_ylabel('Behavioral Response',fontsize=45)
        plt.tick_params(labelsize=35,length=10,width=5)
        return baseline,training,baseline_mean,training_mean,baseline_err,training_err

def MultiBRchanged(figsize):
    homobase,homotesting,homobmean,homotmean,homoberr,homoterr = BRchanged(figsize, 'Homo')
    heterobase,heterotesting,heterobmean,heterotmean,heteroberr,heteroterr = BRchanged(figsize, 'Hetero')
    Wtbase,Wttesting,Wtbmean,Wttmean,Wtberr,Wtterr = BRchanged(figsize, 'Wtsibling')
    a = stats.ttest_ind(homobase,homotesting)
    b = stats.ttest_ind(heterobase,heterotesting)
    c = stats.ttest_ind(Wtbase,Wttesting)
    x = np.array([12,18])
    y = np.array([1.5]*2)
    fig,ax = plt.subplots(figsize=figsize)
    plt.bar(x+y,[homobmean,homotmean],color=(0,0,0,0),edgecolor='red',yerr=[homoberr,homoterr],capsize=20,linewidth=5,width=1.5,label='Homo')
    plt.bar(x-y,[Wtbmean,Wtbmean],color=(0,0,0,0),edgecolor='black',yerr=[Wtberr,Wtterr],capsize=20,linewidth=5,width=1.5,label='Wtsibling')
    plt.bar(x,[heterobmean,heterotmean],color=(0,0,0,0),edgecolor='blue',yerr=[heteroberr,heteroterr],capsize=20,linewidth=5,width=1.5,label='Hetero')
    for i in range(0,7):
        plt.scatter(x+y, np.transpose(np.array([homobase,homotesting]))[i],marker='o',color='red',s=50)
    for i in range(0,8):
        plt.scatter(x-y,np.transpose(np.array([Wtbase,Wttesting]))[i],marker='*',color='black',s=50)
        plt.scatter(x,np.transpose(np.array([heterobase,heterotesting]))[i],color='blue',marker='d',s=50)
    if c[1]<0.5:
        ax.plot([(x-y)[0],(x-y)[0]],[np.amax(np.array([Wtbase,Wttesting]))+0.1,np.amax(np.array([Wtbase,Wttesting]))+0.2],color='black')
        ax.plot([(x-y)[1],(x-y)[1]],[np.amax(np.array([Wtbase,Wttesting]))+0.1,np.amax(np.array([Wtbase,Wttesting]))+0.2],color='black')
        ax.plot(x-y,[np.amax(np.array([Wtbase,Wttesting]))+0.2,np.amax(np.array([Wtbase,Wttesting]))+0.2],color='black')
        ax.scatter((x-y)[1],np.amax(np.array([Wtbase,Wttesting]))+0.3,marker='*',s=100,color='black')
    elif b[1]<0.5:
        ax.plot([x[0],x[0]],[np.amax(np.array([heterobase,heterotesting]))+0.1,np.amax(np.array([heterobase,heterotesting]))+0.2],color='black')
        ax.plot([x[1],x[1]],[np.amax(np.array([heterobase,heterotesting]))+0.1,np.amax(np.array([heterobase,heterotesting]))+0.2],color='black')
        ax.plot(x,[np.amax(np.array([heterobase,heterotesting]))+0.2,np.amax(np.array([heterobase,heterotesting]))+0.2],color='black')
        ax.scatter(x[1],np.amax(np.array([heterobase,heterotesting]))+0.3,marker='*',s=100,color='black')
    elif a[1]<0.5:
        ax.plot([(x+y)[0],(x+y)[0]],[np.amax(np.array([homobase,homotesting]))+0.1,np.amax(np.array([homobase,homotesting]))+0.2],color='black')
        ax.plot([(x+y)[1],(x+y)[1]],[np.amax(np.array([homobase,homotesting]))+0.1,np.amax(np.array([homobase,homotesting]))+0.2],color='black')
        ax.plot(x+y,[np.amax(np.array([homobase,homotesting]))+0.2,np.amax(np.array([homobase,homotesting]))+0.2],color='black')
        ax.scatter((x+y)[1],np.amax(np.array([homobase,homotesting]))+0.3,marker='*',s=100,color='black')
    else:
        pass
    print(a[1],b[1],c[1])    
    ax.spines['top'].set_linewidth(5)
    ax.spines['right'].set_linewidth(5)
    ax.spines['bottom'].set_linewidth(5)
    ax.spines['left'].set_linewidth(5)
    # ax.set_xlabel('Condition',fontsize=45)
    ax.set_ylabel('Behavioral Response',fontsize=45)
    plt.tick_params(labelsize=35,length=10,width=5)
    plt.xticks(x,['pre-training','post-training'])
    ax.set_title('Behabioral response variety',fontsize=50)
    ax.legend(loc='upper left',fontsize=28)
    ax.set_ylim(-1,4)


def binmotilitytrace(figsize,period,Day,VCcolor,datacolor=''):
    fig, ax = plt.subplots(figsize = figsize)
    data1 = papulation('Wtsibling',period,Day,datacolor)
    data2 = papulation('Hetero',period,Day,datacolor)
    data3 = papulation('Homo', period, Day,datacolor)
    newdata1 = np.array([np.array([np.mean(data1[i,j:j+10]) for j in range(0,710)]) for i in range(0,len(data1))])
    newdata2 = np.array([np.array([np.mean(data2[i,j:j+10]) for j in range(0,710)]) for i in range(0,len(data2))])
    newdata3 = np.array([np.array([np.mean(data3[i,j:j+10]) for j in range(0,710)]) for i in range(0,len(data3))])
    ax.plot(np.mean(newdata1,axis=0),color = 'black',label='Wtsibling')
    ax.plot(np.mean(newdata2,axis=0),color = 'blue',label='Hetero')
    ax.plot(np.mean(newdata3,axis=0),color = 'red',label='Homo')
    plt.tick_params(labelsize=18,length=12,width=2)
    ax.set_ylabel('Angular Velocity',fontsize=20)
    ax.set_xlabel('Time(s)',fontsize=20)
    ax.bar(420,2.5,color = VCcolor,width=360,alpha = 0.2)
    ax.spines['top'].set_linewidth(2)
    ax.spines['right'].set_linewidth(2)
    ax.spines['bottom'].set_linewidth(2)
    ax.spines['left'].set_linewidth(2)
    ax.legend(loc='upper right',fontsize=15)
    if period == 'Baseline'or period =='Testing':
        ax.set_title(period,fontsize = 30)
    else:
       ax.set_title(Day.replace(' ','')+' '+period.lower(),fontsize = 30)
       if VCcolor == 'red':
           ax.bar(460,np.amax(np.concatenate((np.mean(newdata1,axis=0),np.mean(newdata2,axis=0),np.mean(newdata3,axis=0))))+1,color = 'navy',width=80,alpha = 0.2)
       else: pass
    ax.set_xlim(0, 730)
    ax.set_ylim(0,2)
    plt.xticks(np.arange(0, 710, 120),np.arange(0,6,1))
    plt.yticks(np.arange(0,2,0.5))
    plt.savefig(r'\\192.168.83.71\home\a.png',dpi=300,bbox_inches='tight')