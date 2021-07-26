from numpy.core.defchararray import index
from numpy.core.numeric import True_
import pandas as pd
import numpy as np
from pandas.core.indexes import period
from pandas.core.indexes.multi import MultiIndex

#layered index: more layers of index on one same axis
X  = pd.Series(np.random.randn(9) , index=[['a','a','a','b','b','b','c','c','c'],[1,2,3,1,2,3,1,2,3]])
print(X.index)
# - so is part-index
X['a']
X['a':'2']
X.loc[:,2]

#unstacking mulitiindex
print(X.unstack().stack())
#also in Dataframes
Y = pd.DataFrame(np.arange(16).reshape((4,4)),index = [['a','a','b','b'],[1,2,3,4]],columns=[['A','B','A','B'],[4,3,2,1]])
Y.index.names = ['words','numbers']
Y.columns.names = ['WoRdS','Nub']

#Or a simply way if
MultiIndex.from_arrays([['name1list'],['name2list']],names= ['nameslist','namelist2'])
#SWAPing and re-sorting with mtlayerindex
Y.swaplevel('words','numbers')
Y.sort_index(level = 0) #???? need more info



#methods on level:
Y.sum(level = 'words' , axis = 0)
print(Y)
#? use lines for indexing
#?print(Y.set_index(['1','2'],drop = False))




#merging data(pandas form)
#--DATABASE-STYLE-CONNECTING(merge with key(lines))
d1 = pd.DataFrame({'key':['a','b','b','a','a','b'],'data1': range(6)})
d2 = pd.DataFrame({'key':['a','b'],'data2':[1,-1]})
pd.merge(d1,d2 , on = 'key')# point out name of -key-
pd.merge(d1,d2, left_on='key',right_on= 'key')# if no same keyname
pd.merge(d1,d2,how ='outer') # on how method **

#you can also use multi-keys#skipqwqwqwq  if same key name, use suffix =


#-merge with index                  how = outer can save dumpli-indexes
pd.merge(d1,d2,left_index=True,right_index=True,how = 'outer')
#old-version
# d1.join(d2,how='outer')#join on left with same index

#merge with axis (numpy+pandas)
s1 = pd.Series([0,1],index=['a','b'])
s2 = pd.Series([2,3,4],index=['b','c','d'])
s3 = pd.Series([5,6],index=['d','e'])

pd.concat([s1,s2,s3] ,axis= 0) #shuffle in
pd.concat([s1,s2,s3],axis  = 1)
print(np.concatenate([s1,s2,s3]))

#-same for databases (only one axis per time)
d1 = pd.DataFrame(np.random.randn(3,4),columns=['a','b','c','d'])
d2 = pd.DataFrame(np.random.randn(2,3),columns=['a','b','d'])
print(pd.concat([d1,d2],ignore_index=True))  #simply smash them together


#conneccting data
s1 = pd.Series([np.nan,2,np.nan,4,5],index= ['a','b','c','d','e'])
s2 = pd.Series([2,3,4,5,6],index = ['a','b','c','d','e'])

np.where(s1.isnull(),s1,s2)
s1.combine_first(s2)  #like fix data


#remodeling and projection
# - using multiindex (stack ,unstack)
data = pd.DataFrame(np.random.randn(25).reshape(5,5),index=[1,2,3,4,5],columns=[11,22,33,44,55])
print(data.stack())  #col to index
print(data.stack().unstack()) #unsatcking can follow layers  (layername or 0)

#unstacking may brings in NAN:(However it is reversable)
print(pd.concat([s1,s2],keys = ['one','two']).unstack())
#if you unstack names,it will be the least level of indexes
data.index.name = 'A'
data.columns.name = 'B'

#all of them can pass a special name:
print(data.stack().unstack('A'))  #index and cols are swapped

#proj- length to wide: (shift between data, index and columns)
data = pd.read_csv(r'D:\#CXNOVA\UNI-STOCK\Codes\Dummies\pydata-book-2nd-edition\examples\macrodata.csv')
periods = pd.PeriodIndex(year = data.year,quarter = data.quarter,name='date')
columns = pd.Index(['realgdp','infl','unemp'],name= 'item')
data = data.reindex(columns = columns)
data.index = periods.to_timestamp('D','end')  #notice to_timestamp did not appear here
pdata = data.stack().reset_index().rename(columns={0:'value'})
print(pdata)  #data with two or more keys ,we prefer them to be unstacked:
print(pdata.pivot('date','item','value'))  #for col ,index,value
#pivot  =  set_index + unstack
pdata['value2'] = np.random.randn(len(pdata))
print(pdata.pivot('date','item','value')) #single column

#proj - wide to length
#-melt method: reverse of pivot
data = pd.DataFrame({'key':['A','B','C'],'11':[1,2,3],'22':[4,5,6],'33':[7,8,9]})
data.melt('key')
data.melt('key').pivot().reset_index()  #give another line for indexing
#melting selections:
pd.melt(data,id_vars=['key'],value_vars=['11','22'])#id_vars is not neccessary
