from numpy.core.fromnumeric import size
import pandas as pd
import numpy as np

#13.1 How to combine Pandas and Other Modeling packs:
#-1 using pandas to load data and wash
DF = pd.DataFrame({'x':np.arange(0,10),'y':np.arange(0,10),'z':np.arange(0,10),})
DF.values #Convert it into Numpyarray
DF = pd.DataFrame( DF.values ,columns= ['x','y','z']) #convert it back

#selecting datacols ( if with unwanted data ):
DF['shabby'] = np.arange(100,110,)
DF[['x','y','z']].values

#replaceing data with dummies(save data):
DF['shabby'] = ['a','b','a','b','a','b','a','b','a','b']
dummy = pd.get_dummies(DF['shabby'])
DF_dummied = DF.drop('shabby',axis = 1).join(dummy)


#Pasty creates modeling describsion:
import patsy
y , X = patsy.dmatrices('y ~ x + z',DF)
print( y , "\n" , X) #designmatrixes are ndarray with more data
print(patsy.dmatrices('y ~ x + z + 0',DF)[1])
#pasty - designed matrices can be passed to sth for a minimal er chenghuigui
coef , resid , _ , _ =np.linalg.lstsq(X,y,rcond= None)

#get the info(col-name)back:
coef = pd.Series(coef.squeeze() , index=X.design_info.column_names)

#mixing patsy with pythoncode:
my , mx = patsy.dmatrices(' x ~ y + np.log(np.abs(z) + 1 )' , DF) #np-codes
my , mx = patsy.dmatrices(' x ~ standardize(y) + center(z)',DF) #some func are built-in
#saving original data:
newX = patsy.build_design_matrices([X.design_info],DF)
#patsy adding:   I( )
my , mx =patsy.dmatrices(' x ~ I(y + z)',DF)


#sepreation and patsy:
#if you use non-num data ,it will auto-convert into dummies:
my , mx = patsy.dmatrices('x ~ shabby',DF) #have a col for interception
my , mx = patsy.dmatrices('x ~ shabby + 0',DF) #don't have one
#C ( ) stands for cat···？
my , mx = patsy.dmatrices('x ~ C(shabby)',DF)
#multiple lines:
DF['shabby2'] = DF['shabby'].map({'a':'A' , 'b':'B'})
my , mx = patsy.dmatrices('x ~ shabby + shabby2',DF)
#?_?



import statsmodels.api as sm
import statsmodels.formula.api as smf
#线性模型，广义线性模型，鲁棒线性模型，线性混合效应模型，方差分析，时间序列过程，状态空间模型，广义矩量法
def dnorm ( mean , vari , size = 1 ):
    if isinstance(size , int):
        size = size
    return mean + np.sqrt(vari) *np.random.randn(size)
np.random.seed(12345)
N = 100
X = np.c_[dnorm( 0, 0.4, size=N ),dnorm( 0, 0.6, size=N ),dnorm( 0, 0.2, size=N )]
eps = dnorm(0,0.1,size = N)
beta = [0.1 ,0.3,0.5]
y = np.dot(X,beta) + eps
#beta- a model / dmorm: randn with specified mean and sqrt

X_model = sm.add_constant(X) #add interception to a known mat\
#should be [1.  ,~]

model = sm.OLS(y,X) #make a OLS

#model object and its fitting
result = model.fit()
print(result.params)
print(result.summary()) #var names standardized to x1,x2,x3

#?suppose all data are in mat:
data = pd.DataFrame(X , columns=['c1' , 'c2' , 'c3'])
data['y'] = y

results = smf.ols('y ~ c1 + c2 +c3' , data = data ).fit()
results.params
results.tvalues
#??

#predicting
results.predict(data[:5])


#time-sequencing:
init_x = 4
values = [ init_x , init_x ]
N = 1000
b0 = 0.8
b1 = -0.4
noise = dnorm( 0 , 0.1 , N )
for i in range(N):
    new_x = values[-1] * b0 + values[-2] * b1 + noise[i]
    values.append(new_x)
#? AR(2) model
MaxLag = 5
model = sm.tsa.AR(values)
results = model.fit(MaxLag)
# first: intercep , then : 2 lag 
#????(fall)


#scikit-learn~~
#scikit-learn hasn't combine with pandas yet(?)
train = pd.read_csv(r'Dummies\pydata-book-2nd-edition\datasets\titanic\train.csv')
test = pd.read_csv(r'Dummies\pydata-book-2nd-edition\datasets\titanic\test.csv')
#scikit&statsmodels can't deal with nans:
print(train.isnull().sum(),"\n",test.isnull().sum())
#using age-line model  , to imputation this:
impute_val = train['Age'].median()
train['Age'] = train['Age'].fillna(impute_val)
test['Age'] = test['Age'].fillna(impute_val)
#specify our model:
train['IsFemale'] = (train['Sex'] == 'female').astype(int)
test['IsFemale'] = (test['Sex'] == 'female').astype(int)
#create vars , ndarray
predictors = ['Pclass' , 'IsFemale' , 'Age']
X_train = train[predictors].values
X_test = test[predictors].values
y_train = train['Survived'].values
from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
model.fit(X_train , y_train)
y_predict = model.predict(X_test)
#dead

#cross-validating - CV /blahblah
from sklearn.linear_model import LogisticRegressionCV
model_cv = LogisticRegressionCV(10)
model_cv.fit(X_train , y_train)
from sklearn.model_selection import cross_val_score
model = LogisticRegressionCV(cv = 10)
scores = cross_val_score(model , X_train , y_train , cv = 4 )

