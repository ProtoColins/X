import pandas as pd
import numpy as np

#12.1 Catagorial object (better power and usage)
fruits = pd.Series(['apple','banana','apple','apple']*2)
# dim --- used to show duplicatied data
values = pd.Series([1,0,1,1]*2)
dim = pd.Series(['apple', 'orange'])
#get them back:
dim.take(values) #alias: fruits
#dict - form (better for: renaming)

#True Catagorials:
dataffframe = pd.DataFrame(
    {'fruit':fruits,
    'basket_id': np.arange(len(fruits)),
    'count': np.random.randint(3,15,size=len(fruits)),
    'weight': np.random.uniform(0,4,size=len(fruits))},
    columns = ['basket_id','fruit','count','weight'])
fruity_cat = dataffframe['fruit'].astype('category')
print(fruity_cat)


#categorials.features:
fruity_cat_value = fruity_cat.values

fruity_cat_value.categories
#Index['apple','banana'] , dtype= ~

fruity_cat_value.codes 
#array[0,1,0,0,0,1,0,0] dtype = ~

#also from other list-forms:
my_cat = pd.Categorical(['0','1','0','0','0','0','0'])
#from back:
cat_kinds = ['zero','0','lin']
my_zeroes = pd.Categorical.from_codes(fruity_cat_value.codes , cat_kinds)
#make it ordered:?
ordered_zeroes = pd.Categorical.from_codes(fruity_cat_value.codes , cat_kinds , ordered=True)


#Categorial Calculations:
np.random.seed(12345)
draws = np.random.randn(1000)
bins = pd.qcut(draws,4 , labels=['Q1','Q2','Q3','Q4']) # sample of categorial
pd.Categorical(bins.codes,['Q1','Q2','Q3','Q4']) #maybe the same(?)

#memory boostage:
N = 10000
draws = pd.Series(np.random.randn(N))
labels = pd.Series(['A','B','C','D']*(N//4))
cats = labels.astype('category')
print(labels.memory_usage(),cats.memory_usage()) #about 8 times the cost
#also , using groupby on cats will faster(---)
del draws , labels , cats

#Catting methology
fruity_cat.cat.codes #how it cats
fruity_cat.cat.categories #fruity_cat_value.categories(?)
#if actual cat is bigger than observed cat:(update the cat.cat.categories)
act_cat = ['a','b','c','d','zoom']
cat_act = fruity_cat.cat.set_categories(act_cat)
#if bigger cat is useless(update the cat.cat.categories
less_cat = fruity_cat[fruity_cat.isin(['apple'])]
less_cat.cat.remove_unused_categories()

#Creating fake_var:(one_hot data(martix_map))
pd.get_dummies(fruity_cat)



#Adcanced_Groupby:
#-transform  :-----: must be a biaoliang ,same size of the original , cannot change its inputs?
keys = pd.DataFrame({'key':['A','B','C','D']*3,'value':np.arange(12)})
gkeys = keys.groupby('key').value
gkeys.mean()
#to get a series with the sizeof keys['value'] , valueof mean_of_groupby
gkeys.transform(lambda x : x.mean())
gkeys.transform('mean')
gkeys.transform(lambda x : x * 2)
gkeys.transform( lambda x : x.rank(ascending = False))
#speed: transform + built-in func <transform < apply 
def normalize(x):
    return (x -x.mean())/x.std()
alias = [
    gkeys.transform(normalize),
    gkeys.apply(normalize),
    ((keys['value'] - gkeys.transform('mean')) / gkeys.transform('std'))
]


#grouped -timing resample:
N = 15 
times = pd.date_range('2017-01-01 00:00',freq= '1min',periods=N)
data = pd.DataFrame({'time' : times , 'value':np.arange(N)})
#index time and then resample:
data.set_index('time').resample('5min').count()
#if with extra key:
data2 = pd.DataFrame({ 'time' : times.repeat(3)  , 'value':  np.arange(N *3) ,'key' : np.tile(['a','b','c'],N)})
{
#! TimeGrouper has been removed!
#for reasmpleing each key and time:
#    timer_key = pd.TimeGrouper('5min') #restiriction : index = time object
#    resampled = data2.set_index('time').groupby(['key',timer_key]).sum()
}
#method chains:
#make less useless variables:
data_plus = data.copy()
data_plus['time'] = 0 #old way and space consuming:
data_plus = data.assign( time = 0 ) #new-fashioned(saving)way
#-?
def get_data( x , y ):
    return data
data3 = get_data()
data3 = data3[data3['value'] < 0] #old
data3 = (get_data [lambda x : x['value'] <0]) #????\

#pipe method:
a = get_data( data , y = 0)
data.pipe( get_data , y = 0)# easier for chains







