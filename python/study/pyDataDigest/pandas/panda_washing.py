from numpy.core.fromnumeric import reshape
import pandas as pd
import numpy as np
from pandas._libs.missing import NA
#legal missing data:
strings = pd.Series(['avocado', np.nan , 'bananas!',None,pd.NA])
print(strings.isnull())

#filtering NA : dropna
dataframes = pd.DataFrame([[1,2,3,4],[5,pd.NA,6,7],[8,9,10,pd.NA],[pd.NA,11,pd.NA,12]])

print(strings.dropna(),"\n",dataframes.dropna(),"\n",dataframes.dropna(how='all'))
#normal dtframe.dropna will drop all lines ,killing data
#if how = all ,datais saved ,only drop all-na lines/columns
#  default axis = 0:
print(dataframes.dropna(axis=1))

#threshing data with limited NAs
df = pd.DataFrame(np.random.randn(6,6))
df.iloc[:4,5] =np.nan
df.iloc[:3,:2]=np.nan
print(df.dropna(thresh= 6) )#???



    #filling the missing numbers
print("""here!\n""",
df.fillna(0),"\n",   #fill-all
df.fillna({1:0,2:10}),"\n",  #fill accroding to lines
df.fillna(method='ffill'),"\n"#importing methods
)# fillna is view


#deleting multiple numbers
df = pd.DataFrame({'k1': [1,2,3]*3 ,'k2' :[1,2,3,1,2,3,1,2,3]})
print(df.duplicated())
#default first ,also keep = last
df.drop_duplicates(keep='last')

#using ufunc(MAPPING) to make data transforming
Unclassed = pd.Series([1,3,5,7,9,2,4,7,8,9])
is_prime_proj = {1 : False ,2 : True ,3 : True ,4 : False ,5 : True ,6 : False ,7 : True ,8 : False ,9 : False ,0 : False ,}
Unclassed['is_prime'] = Unclassed.map(is_prime_proj)
print(Unclassed)
del Unclassed['is_prime']
#replacing  (simplier method of mapping)
Unclassed.replace( True , 'HA' )
Unclassed.replace( [1,2],['A','B'])
Unclassed.replace({1:'A',2:'B'})
print(Unclassed)
del Unclassed


#renaming Axis indexing:(repilca)
data = pd.DataFrame(np.arange(25).reshape(5,5),index = ['Aasf','biybiCTb','sdkvhFc','iasfDD','CXIadE'])

transform = lambda x : x[:4].upper
data.index.map(transform)
data.index = data.index.map(transform)

#if want a new version
###! print(data.rename(index = str(data.index.name).title(), columns= str(data.columns.name).upper) ) #? why str

data.rename(index = {'OHIO':'SAIBAF'}, columns = {'IAUVS':'AIUW'},inplace=True)


#boxing 
Ages = [1,2,5,15,335,61,42,43,6,13,423,54,4,412]

bin = [0,30,100,300]
cats = pd.cut(Ages,bin)
#return a Catagorial objetct which has:

cats.codes   #showing boxes data fell
cats.categories #showing boxes status
pd.value_counts(cats) #calcing

#default: right is closed(True) 
#box names: can be labled
cats = pd.cut(Ages,bin,right=False ,labels=['A','AA','AAA'])

#giving boxnumbers: 
cats = pd.cut(Ages,2,precision=3)

#qcut-ing (?)
data = np.random.randn(1000)
cats = pd.qcut(data,4)
print(pd.value_counts(cats))
#also :
cats = pd.qcut(data,[0,0.1,0.5,1])  #feng wei shu?


#filtering data and errors"
data = pd.DataFrame(np.random.randn(1000,4))
data.describe()
#--to locate a number abs >3 :
col = data.iloc[2]
print(col[np.abs(col) > 2])

#or:
data[(np.abs(data)>2).any(1)]
#get data signs
np.sign(data) #? head?


#replacing(plus) and random sampling
data = pd.DataFrame(np.arange(20).reshape((5,4))) #only 1st column()

#sampler
sampler = np.random.permutation(4)
data.take(sampler)

#-or
data.sample(3) #no -overlapping
data.sample(10,replace=True)



#Calcuting #!expers
data = pd.DataFrame({'key' : [1,2,3,14,1,42,14,12,43,5] , 'lines':range(10)})

pd.get_dummies(data['key']) #return a matrix with 1 (shot dummies)
####see p206 , multiple parterners indexing
#also
pd.get_dummies(pd.cut(np.random.rand(10),5))


#str methods plus
#-Normal str methods:
#q-doing
val = 'a,b ,  fundo'
pieces = [x.strip() for x in val.split(',')]
#q-combing
'::'.join(pieces)

#regex
import re
text = 'a  bar \t aw\t wq'
re.split('\s+',text)
#or
reg = re.compile('\s+',flags= re.IGNORECASE)
reg.split(text)

#findall match search
mail_re = re.compile(r'([A-Z0-9._%+-]+)@([A-Z0-9.-]+)\.([A-Z]{2,7})',flags=re.IGNORECASE) #care about the usage of ()
packs = mail_re.match('vallaha@goss.net') #matched object
print(packs.groups())
print(mail_re.sub(r'NAME : \1 , DOMIAN :\2 ,SUFFIX: \3','vallaha@goss.net'))  #grouping print ,like printf in C



#str methods in pandas(vectoried) (by item and skipping nans)
# -----data.str
# match.str.get()
# match.str[0]
# match.str[:5]


