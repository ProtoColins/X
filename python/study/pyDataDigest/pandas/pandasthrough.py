import pandas as pd
import numpy as np
#   NUMPY-STYLE 

#usual data structures:    Series DataFrame
# Series: 1d array with index { hash table with an order}
obj = pd.Series([1,2,3,4])
print(obj.values)
print(obj.index)

obj = pd.Series([1,2,3,4],index=['a','b','c','d'])
obj['a']
obj[obj > 2]
obj * 2
obj = pd.Series({'a':1,'b':2,'c':3},index = ['b','c','a','d'])
print(obj)   #lost data use NaN to fill in

# test null methods
pd.isnull(obj)
pd.notnull(obj)
obj.isnull()

#Auto aligning:  (datatypes,items,etc)

obj + obj*2


#Series and its index have 'Name'
obj.name = 'O-B-J'
obj.index.name = 'iavb'


#Dataframe parlance
#multiple index - Dict

wasabi = pd.DataFrame({
    'A' : [1,2,3],
    'B' : [0,9,8],
    'C' : [5,6,-1]},
    columns=['D','B','C','A'],
    index= ['one','two','three']
)
#Strict Sizes
wasabi.head()
wasabi.Name = 'boo'
wasabi.index.name = '?'
#get items [lines and rows]
wasabi.D
wasabi['C']
wasabi.loc['one']

#re-filling data accrodig to indexes:
B = pd.Series([12,13,14],index=['three','one','two'])
wasabi['D'] = B
wasabi['bools'] = wasabi.D == 'one'
print (wasabi)

del wasabi['bools']


# dict in a dict
ddict = {'KEY1':{102:1,120:2},'KEY2':{120:3,14:0}}
obj = pd.DataFrame(ddict)
obj.Name = 'BA'
obj.index.name = 'AB'
#CONNECTIONS WITH NUMPY
obj.T

#indexin object
std = pd.Series( range(5) , index = [1,2,3,4,5])
index = std.index[2:3]
print(index)

#indexobject is unchangeable
#like a set but can include multiple items



# RE -INDEXING
std = std.reindex([4,3,1,0], method = 'ffill')
#ffilling / bfill need unique index
#ffill - plug items in whencountered missing numbers 
#re arrangeing using new index
wasabi.reindex(columns = [ 'three' ,'two' ,'one'])

#dropping columns
wasabi.drop(['D'],axis ='columns',inplace=True)
#use axis for dropping other lines


#indexmethods:
std = pd.Series(np.arange(5) , index = ['a','b','c','d','e'])
std['b']
std[1]
std[2:4]
std[['a','c']]
std[[1,3]]
std[std<3]
#slicing includes end!

std = pd.DataFrame(np.arange(25).reshape(5,5) ,index=[1,2,3,4,5],columns=[5,6,7,8,9])
print(std[:3])  # colums selection (default,only slicing)
std.loc[:1]  #?
std.iloc[:2]


#calculations combining:

obj1 = pd.DataFrame(np.arange(16).reshape(4,4),index = [1,2,3,4] ,columns=[ 5,6,7,8])
obj2 = pd.DataFrame(np.arange(16).reshape(4,4),index = [3,4,5,6] ,columns=[ 7,8,9,10])#index up-down , col,left-right
print(obj1+obj2)
#flexible calcs:
print(obj1.add(obj2,fill_value= 0 ))  #first expand two plots ,fill with 0 ,then add

arr = np.arange(16).reshape(4,4)
print (arr - arr[0])
#for s & d , s will fill in to d's lines and do the same calc
arr = pd.Series([1,2,3,4], index = [6,8,7,5])# left-right

print(arr+obj1)


#funcs usage:
np.abs(arr)
np.abs(obj1)

g = lambda x : x+1  #series
obj1.apply(g)
obj1.applymap(g)


#internal sorting:
arr.sort_index()
obj1.sort_index()
obj1.sort_index(axis=1,ascending= False)
arr.sort_values()
#defalut ,all nans will go to the bottom

obj1.sort_values(by= ['2'])

#???? RANKING
#______________________#

#multiple indexes:
balh = pd.Series(range(6) , index = [ 1,2,3,3,4,5])
balh.is_unique
balh.iloc[3]


#   STATICS
stat = pd.DataFrame(np.arange(25).reshape(5,5) , 
index=[1,2,3,4,5],
columns=['a','b','c','d','e']
)
stat.sum
stat.sum(axis='columns')
stat.sum(skipna= False)

stat.idxmax
stat.describe
stat.cumsum
#.-.

obj1.unique().sort_values()
arr.value_counts()


