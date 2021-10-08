# -*- coding: utf-8 -*-
"""
Created on Mon Aug 16 13:21:19 2021

@author: DELL_04
"""

def lightDetector(CSVdata):
  redLED = CSVdata.iloc[:,0]
  greenLED = CSVdata.iloc[:,1]
  react2red = [
                  i
                  for i in redLED.index
                  if redLED[i] == 20
                  ]
  react2grn = [
                  i
                  for i in greenLED.index
                  if greenLED[i] == 20
                  ]
  return react2red, react2grn

def perioddector(CSVdata):
  redreact, grnreact = lightDetector(CSVdata)
  for i in range(len(redreact)-1,-1,-1):
    while redreact[i]-redreact[i-1] > 100:
      start = redreact[i-1]
      diff = redreact[i]-redreact[0]
      if diff > 10000:
        diff = diff/2
      break
  redperiod = [
            [
                     i
                     for i in redreact
                     if i <= start + diff * j
                     if CSVdata.iloc[:,0][i] == 20
                     ]
            for j in range(0,31)
            ]
  grnperiod = [
               [
                i
                for i in grnreact
                if i <= grnreact[0] + diff * j
                if CSVdata.iloc[:,1][i] == 20
                ]
               for j in range(0,31)
               ]
  return redperiod, grnperiod

def modifyperiod(redperiod, grnperiod):
  for i in np.arange(30,-1,-1):
    if i <= 0:
      break
    else:
      del redperiod[i][0:len(redperiod[i-1])]
      del grnperiod[i][0:len(grnperiod[i-1])]
  while [] in redperiod:
    redperiod.remove([])
  while [] in grnperiod:
    grnperiod.remove([])
  return redperiod, grnperiod

def removeErr(redperiod,grnperiod):
  for i in range(0,len(redperiod)):
    for j in range(0,len(redperiod[i])-2):
      if redperiod[i][j+1] - redperiod[i][j] != 1:
        redperiod[i-1] = redperiod[i-1] + redperiod[i][:j+1]
        del redperiod[i][0:j+1]
        break
  for i in range(0,len(grnperiod)):
    for j in range(0,len(grnperiod[i])-2):
      if grnperiod[i][j+1] - grnperiod[i][j] != 1:
        grnperiod[i-1] = grnperiod[i-1] + grnperiod[i][:j+1]
        del grnperiod[i][0:j+1]
        break        
  for i in range(len(grnperiod)-1,-1,-1):
    if grnperiod[i][0] - grnperiod[i-1][len(grnperiod[i-1])-1] == 1:
      grnperiod[i-1] = grnperiod[i-1] + grnperiod[i]
      del grnperiod[i]
  redlightLength = [
                  len(redperiod[i])
                  for i in range(0,len(redperiod))
                  ]
  for i in range(len(redlightLength)-1,-1,-1):
    if redlightLength[i] < 300 and redlightLength[i-1] < 300:
      redperiod[i-1] = redperiod[i-1] + redperiod[i]
      del redperiod[i]
    elif redperiod[i][0] - redperiod[i-1][-1] == 1:
      redperiod[i-1] = redperiod[i-1] + redperiod[i]
      del redperiod[i]
  return redperiod, grnperiod

def periodgenerator(CSVdata):
  redperiod, grnperiod = perioddector(CSVdata)
  redperiod, grnperiod = modifyperiod(redperiod, grnperiod)
  for i in range(0,len(redperiod)):
      if len(redperiod[i]) < 300:
          redperiod, a = removeErr(redperiod, grnperiod)
          break
  for j in range(0,len(grnperiod)):
      if len(grnperiod[j]) < 300:
          b, grnperiod = removeErr(redperiod, grnperiod)
          break
  timingdf = pd.concat([pd.DataFrame({'redLED':redperiod}),pd.DataFrame({'greenLED':grnperiod})],axis=1)
  return timingdf

Daynus = ['Day1','Day2','Day3','Day4','Day5','Testing']
Days = ['Day 1','Day 2','Day 3','Day 4','Day 5','Testing']
for genotype in genotypes:
    for Set in Sets:
        for Day,Daynu in zip(Days,Daynus):
            vars()[genotype+Set+Daynu+'timingdf'] = periodgenerator(locals()[genotype+Set+'eData'][Day])
            