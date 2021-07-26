from numpy.core.defchararray import index
from numpy.lib.function_base import append, quantile
import pandas as pd
import numpy as np
from pandas.core import groupby

#Groupby-method: (split-apply-combine)
Dummy = pd.DataFrame({
    'key1':['a','a','b','b','c','d'],
    'key2':[1,2,3,4,5,4],
    'data1':np.random.randn(6),
    'data2':np.random.randn(6)
},index=['a','aa','aaa','aaaa','aaa','a'])
#get [data] with [key(alsolist,also reindex)]
grouper = Dummy['data1'].groupby(Dummy['key1']) #almost raw-data
grouper2 = Dummy.groupby( [ Dummy['key1'] , Dummy['key2'] ])
f1=np.array(['?','?','.','?','.','?'])
f2=np.array([1,2,1,2,1,1])
grouper3 = Dummy['data1'].groupby([f1,f2])
#raw - grouped data:
print(
    grouper.mean(),"\n",
    grouper2.mean(),"\n",
    grouper3.mean()
    )
#uni-groupby-method:
grouper3.size()


#Scanning the group:(like hanglieshi)
for name , group in Dummy.groupby('key1'):
    print(name)
    print(group)
#multi-keyed:
for (k1,k2) , group in Dummy.groupby(['key1','key2']):
    print(k1,'  ',k2)
    print(group)

#u can create a dict of data:
pointer = dict(list(Dummy.groupby('key1')))

#groupby also any other group/axis:
grouper4 = Dummy[['data1','data2']].groupby(Dummy.dtypes,axis = 1)



#using groupby to select a line/ subset of lines:
Dummy.groupby(['key1'])[['data1']].mean()


#using dict and Series 
map = {'a':'apple','b':'benlala','c':'cytus','d':'dejavu'}
print("\nhere\n",Dummy[['key1']].groupby(map).count())
#????

#using functions:
# key - func - partname
keylist = ['a','a','b','b','b','a']
#? print(  Dummy.groupby([len(Dummy['key1']),keylist]).sum())     #default firstline

#using indexlevels:
Dummy_bigger = pd.DataFrame({
    'key1':['a','a','b','b','c','d'],
    'key2':[1,2,3,4,5,4],
    'data1':np.random.randn(6),
    'data2':np.random.randn(6)
},index=[['a','b','a','b','a','b'],[1,2,3,2,1,3]])
Dummy_bigger.index.name =  ('first','second')

print(Dummy_bigger.groupby( level = 1).sum())




#data accu:
#count sum mean median std var min max prod(?) first/last

#if you want to use self-func:(much-slower)
def peak_to_peak(arr):
    return arr.max() - arr.min()
print(grouper.agg(peak_to_peak))
#also some not-so-formal-ways:
grouper.describe()

#line-org and multi-funced:
tips = pd.read_csv(r'D:\#CXNOVA\UNI-STOCK\Codes\Dummies\pydata-book-2nd-edition\examples\tips.csv')
tips['tip_prt'] = tips['tip'] / tips['total_bill']

grouped = tips.groupby(['day','smoker'])
grouped['tip_prt'].agg(['mean','std',peak_to_peak])
#name new lines for (name,func)
print(grouped['tip_prt'].agg([('Iceflem','mean'),('*FW','std'),('shabby',peak_to_peak)]))

#samething for dataframe:

regrouper = tips[['total_bill','tip']].agg(['count','mean','max'])
#also for (name , func)
#different func for diff lines:
print(regrouper.agg({'tip':np.max,'total_bill':['sum','std']}))



#return lines without index
tips.groupby(['day','smoker'],as_index=False).mean() #savier for reset_index




#apply---paring the data and apply methods:
def lowest( dataframe , n = 5 , columns = 'tip_prt'):
    return dataframe.sort_values(by = columns)[:n]
print('balbalbal\n',tips.groupby('smoker').apply(lowest))


#-? compressing keys:(origin key will be saved)
tips.groupby('smoker',group_keys=False).apply(lowest)

#-? Cuts and qcuts
newframe = pd.DataFrame({'data1':np.random.randn(1000),'data2':np.random.randn(1000)})
quartiles = pd.cut(newframe.data1,10)
#catagorial object to pd.groupby:
Grouped = newframe.groupby(quartiles)

#-qcut:
grouping = pd.qcut(newframe['data1'] , 10 ,labels=False)#label = false 获得分位数数值




#fillna filling all naerrors:
line = pd.Series(np.random.randn(10))
line[::2] = np.nan
line.fillna(line.mean())

#fillina with different groups:
fillmean = lambda x : x.fillna(x.mean())
print(line.groupby([1,1,1,1,1,2,2,2,2,2]).apply(fillmean))



#random picking and arranging:
suits = ['A','B','C','D']
card_val = list(range(1,13))
card = []
for suit in suits:
    card.extend(suit + str(val)  for val in card_val )
deck = pd.Series(card )
#sample:
def draw(deck):
    return deck.sample(2)
#groupsample:
getsuit = lambda x : str(x)[-1]
print(deck.groupby(getsuit).apply(draw)) ###?? can't draw lager than the cuts ,bug?


#grouped weighted average/ relativity:
newframe = pd.DataFrame({'catag':['a']*5+['b']*5,'data':np.random.randn(10),'weight':np.random.randn(10)})
get_weiavg = lambda x :np.average(x['data'],weights=x.weight)
groupeeeer = newframe.groupby(newframe.catag)
groupeeeer.apply(get_weiavg)

#grouped-line-regression
####sample


#pivot table / crosstab
#index - day+smoker
tips.pivot_table(index=['day','smoker']) #alldata , index
tips.pivot_table(['tip_prt','size'],index= ['time','day'],columns=['smoker'],margins= True) #prt data , index  , col 
#margin: add -all-column

#using different func:
tips.pivot_table(['tip_prt'] , index=['time','smoker'],columns=['day'],aggfunc=len , fill_value= 0 )

#crosstab:(pivottable for frequency)
pd.crosstab([tips.time,tips.day],tips.smoker,margins=True)



pd.merge()