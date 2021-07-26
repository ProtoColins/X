#Machine Learning Frame:
# import data -> taste data -> preprocessing -> item-pipeline -> train model ->prediction
import numpy as np
import pandas as pd
import matplotlib as mlp
import matplotlib.pyplot as mplt
import sklearn

datasets = pd.DataFrame([[1,2,3,4,5,6],[1,2,3,4,5,6]],columns=['data','target_num'])
#-----------------------------------------------------#
#tasting data:

#numerial:   
datasets.head   #first (5) rows of data
datasets.info   #dtype, not-nan information of columns
datasets.value_counts #data count of a certain column
datasets.describe #statics of every column(std, mean, 25%,etc)

#visual:
datasets.hist #tiao xing tu----- bins
datasets.plot #kind = scatter/  [ x = (data1) y = (data2) ] aplha = 0.2 , figsize = (A,B)
#more: cmap = plt.get_cmap("jet") , colorbar , s(size) = somedata , c(color) = somedata


#-----------------------------------------------------#
#preprocessing:

#simple-random-split train/test/explore sets ----A:
def simple_split_sets( datasets , split_ratio , shuffled = True):
    '''return (set1 , set2) , length of set1 is ratio*origindata'''
    
    set1_size = int(len(datasets) * split_ratio)

    if shuffled:
        shuffled_index = np.premutaion(len(datasets))
        #!------np.premutaion-------
    else:
        shuffled_index = np.arange(len(datasets) + 1)

    set1_indices = shuffled_index[:set1_size]
    set2_indices = shuffled_index[set1_size:]

    print("set1 :", set1_size ,"set2 :",len(datasets) - set1_size)
    return datasets.iloc[set1_indices],datasets.iloc[set2_indices]

#Straified-split------B:
from sklearn.model_selection import StratifiedShuffleSplit #!
splitter = StratifiedShuffleSplit(n_splits= 1, test_size=0.5, random_state=3075)
for set1_index , set2_index in splitter.split(datasets,datasets['target_num']):
    strat_set1 = datasets.loc[set1_index]
    strat_set2 = datasets.loc[set2_index]

#correlation_matrix:
datasets.corr().sort_values(ascending=False)   #!

#scatter_maxtrix:
from pandas.plotting import scatter_matrix
attributes = ['data','target_num']

scatter_matrix(datasets[attributes])   #!

#-----------------------------------------------------#
#item - pipeline:

datasets.fillna
datasets.median

#simple imputing
try:
    from sklearn.impute import SimpleImputer # Scikit-Learn 0.20+
except ImportError:
    from sklearn.preprocessing import Imputer as SimpleImputer

imputer = SimpleImputer(strategy="median")
imputer.fit    #fillna with strategy
imputer.statistics_   #show every possible fill-in data
imputer.transform # return a fully digested dataframe
imputer.strategy #re-check your pre-set strategy

#converting non-numerical data:
#Ordinal encoder
try:
    from sklearn.preprocessing import OrdinalEncoder
except ImportError:
    from future_encoders import OrdinalEncoder # Scikit-Learn < 0.20

ordinal_encoder = OrdinalEncoder()
ordinal_encoder.fit_transform #fully digest, return encoded
ordinal_encoder.categories_

#One hot encoder
try:
    from sklearn.preprocessing import OneHotEncoder
except ImportError:
    from future_encoders import OneHotEncoder # Scikit-Learn < 0.20

onehotencoder = OneHotEncoder()
onehotencoder.fit_transform  #default return sparse row matrix, or sparse = false
onehotencoder.categories_

#-----------------------------------------------------#
#! Wrinting a pipeline conpoment
from sklearn.base import BaseEstimator, TransformerMixin
#BaseEstimator:(do not use *args, **kwargs) 
#   get two methods adjusting super-param:   get_param() & set_param
#TransformerMixin: auto combine fit & transform into fit_transform
#       to build a pipeline object: write  fit() -- return self & transform -- functional
class AllKazeConventor(BaseEstimator,TransformerMixin):
    '''turn every item into KAZE'''
    def __init__(self, capital = True):
        self.capital = capital
    def fit(self,X,y=None):
        return self
    def transform(self,X,y=None):
        if self.capital:
            self.replace = 'Kaze'
        else:
            self.replace = 'kaze'
        return np.zeros_like(X).map({0 : self.replace})

#or base on a function :
from sklearn.preprocessing import FunctionTransformer
def Kazetransformer(X , capital = True):
        if capital:
            replace = 'Kaze'
        else:
            replace = 'kaze'
        return np.zeros_like(X).map({0 : replace})

FunctionTransformer( Kazetransformer , validate=False, kw_args={"capital" : True})
#validate ophion is used for ensure inputdata = float(?)


#!Build the pipeline
#every fit/transform will proceeded thoughout the pipeline
#pipeline.fit() = fit_transform()*n-1 + fit()
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

pipelinee = Pipeline([
    ('imputerName',SimpleImputer(strategy='mean')),
    ('KazeConventor',FunctionTransformer(Kazetransformer,validate=False)),
    ('StandardScaler',StandardScaler())
])


#Assembling the pipeline:
#Column transformer:
try:
    from sklearn.compose import ColumnTransformer
except ImportError:
    from future_encoders import ColumnTransformer # Scikit-Learn < 0.20
full_pipeline = ColumnTransformer([
    ('num',pipelinee,list(datasets)),
    ('cat',OneHotEncoder(),['target_num'])
])

#or FeatureUnion:
from sklearn_features.transformers import DataFrameSelector
from sklearn.pipeline import FeatureUnion

full_pipeline= FeatureUnion(transformer_list=[
    ('num',pipelinee),
    ('cat',Pipeline('labelbinarizor',DataFrameSelector()))
])


#-----------------------------------------------------#
#! Train YR model

#1 linar model:
from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit #data & label
lin_reg.predict #give data

#other models:
from sklearn.tree import DecisionTreeRegressor
des_tree = DecisionTreeRegressor()

from sklearn.ensemble import RandomForestRegressor
forest_reg = RandomForestRegressor()


#-----------------------------------------------------#
#To value them:
#targets: RMSE / MAE  ,etc:
from sklearn.metrics import mean_squared_error

#cross_val:
#1 cross_val
from sklearn.model_selection import cross_val_score
scores = cross_val_score #model , data , labels , scroing_method ,cv=10
scores_validate = np.sqrt #- score(?)

#saving models:
from sklearn.externals import joblib
joblib.dump #model , 'filename.pkl'
loaded_model = joblib.load # filename.pkl


#-----------------------------------------------------#
#searching parameters:
#   grid search:
from sklearn.model_selection import GridSearchCV
param_grid = [{'n_estimators' : [10,20,30]},{'max_features':[1,2,3]}]
grid_search = GridSearchCV # model , param_grid , cv = 5(folds)

grid_search.best_params_
grid_search.best_estimator_
cvres = grid_search.cv_results_

#   random_search: 
from sklearn.model_selection import RandomizedSearchCV

##? for randomforest searching:
grid_search.best_estimator_.feature_importantces_


