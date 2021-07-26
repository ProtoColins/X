import pandas as pd
import numpy as np
#datatime / timestamps / timesteps / timepart


#basic of datatimes
from datetime import datetime

from pandas.core.indexes.period import period_range
from pandas.io.formats import style
now = datetime.now() #datatime object
now.year
now.month
now.day

delta = datetime(2000,10,10,10,10,10,10) - datetime.now()
delta.days #timedelta object

future = now + delta #datatime + timedelta = datatime


#str - datetime method:
print(str(now))
now.strftime('%Y - %m - %d')  #datetime to str
datetime.strptime('2001 - 01 - 03' , '%Y - %m - %d') #str to datetime
# %Y , %y ,%m , %d , %H ,%I ,%M ,%S , %w , %U , %W , %z ,%F ,%D 

#auxiliary pack: dateutil(in pandas)
from dateutil.parser import parse
parse('2001 -10 - 03') #most human-can-understand pattern (?)


#Basic timesequence:
datetimes = [datetime(2011,1,1),datetime(2011,1,2),datetime(2011,1,3),datetime(2011,1,4)]
ts = pd.Series(np.random.randn(4),index=datetimes)
print(ts.index)  #datmetime index automaticlaly put into index
#datatype is M8ns


#indexing selecting subsets:
ts['2011-01-01'] #can be converted to a datetime can be used as index
ts = pd.Series(np.random.randn(500) , index = pd.date_range('1/1/2000',periods=500))

#only-to-month is okay:
ts['2000-07']
#using datatime to slice:
ts[datetime(2000,1,30):]
#using a datetime not in the index:
ts['1999-01-01':'2020-01-01']
ts.truncate(after='2000-04-01') #eval



#multiple datetime index:
ts = pd.Series(np.random.randn(4),index = [datetime(2011,1,1),datetime(2011,1,3),datetime(2011,1,3),datetime(2011,1,5)])
#getslicing will be uncertain:
ts['2011-01-03']
ts['2011-01-05']
#get unique data(groupby)
ts.groupby(level=0)


#date segration, sample frequency:
resampler = ts.resample('D')
#more later


#summon date-range:
index = pd.date_range('2012-04-01','2012-06-01',freq='D') #default freq is d
index = pd.date_range(start='2020-01-01' , periods=2)#or with start/ends + peroid
    #Frequency list:
    #D , B , H, T/min , S , L/ms , ···
#with a start/end , it will be saved
index_plus  = pd.date_range(start = '2020-02-02' ,periods=10 , normalize=True) #normalize: make anydata lower that freq 0


#more date frequencies:
from pandas.tseries.offsets import Hour , Minute
hour = Hour() #this is an hour-freq-obj
three_hrs = Hour(3)
#actuallly use '3H' is okay
#they can calculate:
fourhrs = hour + three_hrs


#datetime shifts:
ts.shift(2)  
ts.shift(-2) #data shifts with its date, NAN for empty dates
ts/ts.shift(-1) - 1 #calc the changing rate

#shift does not change index (may easliy cause nan)
ts.shift(2 ,freq='3H') #with a freq(not default 'D')

#bias?
from pandas.tseries.offsets import Day , MonthEnd
now = datetime(2000,10,10)
now + Day(3)
now + MonthEnd(2) #to next 2nd monthend
now + MonthEnd(3) #to next 3rd monthend

offsetter = MonthEnd(1)
offsetter.rollforward(now) #same as now + Monthend(1)



#TIMEZONESs:
#summon datepreoids using UTC:
pd.date_range('2020-03-01',periods=10 , tz = 'UTC')

#localization ( transferring preparation)
ts_utc = ts.tz_localize('UTC')
#true transferring
ts_utc.tz_convert('Asia/Shanghai')

#also for datetimeindex:
ts.index.tz_localize('Asia/Shanghai')



#timestamp with timeoznes:
#updating timestamp:
stomp = pd.Timestamp('2011-03-12')
stomp_utc = stomp.tz_localize('UTC')
stomp_utc.tz_convert('Asia/Shanghai')
#xor:
stomp_direct = pd.Timestamp('2020-02-20',tz='Asia/Shanghai')

#.value: Unix to now nanoseconds
stomp_utc.value
##time calculations follow summertime(?)


#actions with timezones:
ts.tz_localize('Asia/Shanghai') + ts.tz_localize('Europe/London')
#no need to convert thx for unix


#peroids & maths:
per_y = pd.Period(2007,freq='A-DEC')
per_y + 5  #2012 whole year
per_y - 2  #~

#sub:
pd.Period(2020 , freq='A-DEC') - per_y
#return numbers of peroid

#indexing:
pd.period_range('2020-01-01','2021-02-01' , freq= 'M') #auto-peroidindex
pd.PeriodIndex(['2020-01-01','2020-02-01','2020-03-01'],freq = 'M') #or

#peroid convert(change freqency)
per_y.asfreq('M',how='start')
per_y.asfreq('S')    #for peroids
ts.asfreq('M')      #for data

#finacial years: Q-JAN to Q-DEC
PQ = pd.Period('2020Q3',freq='Q-FEB')  #!!! warning: freq= is right ,auto-import freqstr= is false


#converting timestamp to peroids:(also reverse)
rangeer = pd.date_range('2000-01-01' , periods= 5 , freq = 'M')
ts = pd.Series(np.random.randn(5),index = rangeer)
a = ts.to_period('M')
a.to_timestamp(how = 'end')

#summon peroidindex from list:
datayear = np.arange(2000.0,2020.0,1.0,dtype='float')
datamonth = [1,2,3,4]*5
index = pd.PeriodIndex( year = datayear , quarter = datamonth , freq = 'Q-DEC')




#reeeesampling and freq-convertion
#one freq to another freq:
rangeer = pd.date_range('2000-01-01','2020-01-01',freq = 'M')
data = pd.Series(np.random.randn(len(rangeer)),index= rangeer)

data.resample('D' , kind = 'peroid').mean() #kind : index-format
#down sample:
#care: closed = 'right/left' ,left is deafault
#label ='right/left'  label-index
#loffset : movelabel (timeoffset)


#OHLC resampling:
data.resample('D').ohlc()

#upward sample:
data.resample('min').asfreq()
#no need to gather , but need to fill:
data.resample('min').ffill( limit = 3)  #ffill with fill-time-limit

#resample using a time peroid:
data.resample('Q-DEC',convention='start')


import matplotlib as mplt
#movable-window-func(?)
#pointing to those func wih ?,u4f for smoothing and de-noising
close_px_all = pd.read_csv(r'Dummies\pydata-book-2nd-edition\examples\stock_px_2.csv' , parse_dates=True , index_col= 0)
close_px = close_px_all[['AAPL','MSFT','XOM']]
close_px = close_px.resample('B').ffill()
#?now, rolling item:
close_px.AAPL.plot()
close_px.AAPL.rolling(250).mean().plot()

#?
appl_std250 = close_px.AAPL.rolling(250 , min_periods = 10).std()
expanding_mean = appl_std250.expanding().mean()

#?
close_px.rolling(60).mean().plot(logy =True)

#?zhi shu jia quan han shu
aapl_px = close_px.AAPL['2006':'2007']

ma60 = aapl_px.rolling(30 , min_periods = 20).mean()
ewma60 = aapl_px.ewm(span = 30).mean()

ma60.plot(style = 'k--' , label = 'SIMP - MA')
ewma60.plot(style = 'k-' , label = 'EM - MA')

#??? dual- func
spx_px = close_px_all['SPX']
spx_rets = spx_px.pct_change()
returns = close_px.pct_change()

corr = returns.AAPL.rolling(125,min_periods = 100).corr(spx_rets)
corr.plot( style = 'g--' , label = '?')

corr = returns.rolling(125,min_periods = 100).corr(spx_rets)
corr.plot( style = 'b--' , label = '-?-')

#?  self-apply-func
from scipy.stats import percentileofscore
score_at_2percent = lambda x : percentileofscore(x , 0.02)
result = returns.AAPL.rolling(250).apply(score_at_2percent)
result.plot()

mplt.pyplot.show()


