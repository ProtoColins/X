from matplotlib import colors
import matplotlib.pyplot as mplt
import numpy as np
#mplt.show()  show all plotted

# make a picture object:
fig = mplt.figure()  # empty pic bowl ,can't draw
ax1 = fig.add_subplot(2,2,1)
ax2 = fig.add_subplot(2,2,2)
mplt.plot(np.random.randn(50).cumsum(),'k--')  #k-- means style ,auto plot the last subplot
nn = ax1.hist(np.random.randn(100),bins = 20 ,color = 'k',alpha = 0.3)
ax2.scatter(np.arange(30),np.arange(30)+3 * np.random.randn(30))   
#previous are for fun

#new fig with axes imported:
fig , axes = mplt.subplots(3,3) #axes is a 2d NDARRAY
#sharex ,sharey ,make them have same x/y cords


#modify plot bounds
# U/B/L/R w(hite)space , h(?)space
#make them expand:
fig , axes = mplt.subplots(2,2 , sharex=True ,sharey= True)
for i in range(2):
    for j in range(2):
        axes[i,j].hist(np.random.randn(500),bins = 50,color = 'k',alpha = 0.5)
mplt.subplots_adjust(wspace= 0 , hspace= 0 ) #these can also be shown in configurations


#color, tags, lineform, drawstyle:
ax2.plot(20*np.random.randn(20),linestyle = '--' , color = 'g',marker = 'o') 
#more color for '#FFFFFF' ,linestyles for help , markers,etc
ax1.plot(50*np.random.randn(50),linestyle = '--' , color = 'r',label = 'D')
ax1.plot(50*np.random.randn(50),linestyle ='-', color = 'b',drawstyle = 'steps-post',label = 'S-P')
ax1.legend(loc = 'best') #generate tuli

del fig , ax1,ax2, nn , axes
#more decorations:
#by pylots or matplotlib API
# -pyplot:  xlim for drawtablesacle , xticks for ticklocation ,xticklabels for ticklabels
#---most recent subplot---
#if called with no arguments:
mplt.xlim()
#if called with arguments:
mplt.xlim([0,1000])

fig = mplt.figure()
ax = fig.add_subplot(1,1,1)
ax.plot(np.random.randn(1000).cumsum())

ticks = ax.set_xticks([0,200,400,600,800,1000]) 
labels = ax.set_xticklabels(['A','B','C','D','E','F'],rotation = 45 , fontsize = 'medium')  #rotation : reversed-clockwise
ax.set_title('MY 4th MMMMMMMMATplotlib plot')
ax.set_xlabel('xlabel')
#or also using ax.set method:
dicto = {'title' : 'MY 4th MMMMMMMMATplotlib plot', 'xlabel' : 'xlabel'}
ax.set(**dicto)

#adding legend:
#1 : adding labels for each line and use plt.legend()
#loc = best for best///
#if want no legend , label = '_nolegend_'

#annotaions and sub_plot manageing:
#-text -annote -arrow:
a = dict( facecolor = 'black' , headwidth = 4, width = 2 , headlength = 4 ) 
ax.annotate( '?' ,xy = (500, 0),xytext = (500,0),arrowprops = a,horizontalalignment = 'left' ,verticalalignment = 'top')
#see more at matplotlib online exhibition(x) for more annotations

#patch object:
rect = mplt.Rectangle((0,0),1000 ,5 ,color = 'k' ,alpha = 0.3)#bottom-left point + width + height
circ = mplt.Circle((0,0),10,color = 'b',alpha = 0.3)
pgon = mplt.Polygon([[0,0],[500,-10],[750,-20],[1000,10]],color = 'g',alpha = 0.5)
ax.add_patch(rect)
ax.add_patch(circ)
ax.add_patch(pgon)


#saving pictures:
mplt.savefig(r'D:\#CXNOVA\UNI-STOCK\Codes\Dummies\matmat.svg',dpi = 72 ,bbox_inches = 'tight')#if suffix = pdf is okay!
#the last fig


#global settings:
mplt.rc('figure',figsize = (10,10)) #set figures to 10*10 pix
#first : target ,second: paradict



#using pandas and seaborn
import seaborn
import pandas as pd
#importing will change default matplotlib paras

#in pandas: Series has .plot method:
ad = mplt.figure()
ad1 = ad.add_subplot(1,1,1)
s1 = pd.Series(np.random.randn(10).cumsum(),index = np.arange(0,100,10))
s1.plot()
#in this , Series index will be the x-label  (or use_index = false)
#also .plot can have (ax = ) param , for a specified location

s2 = pd.DataFrame(np.random.randn(10,4), columns=['A','B','C','D'],index = np.arange(0,100,10))
s2.plot(ax = ad1)
#---series---plot---param---#




#other style plotter:
fig , ades = mplt.subplots(3,1)
data = pd.Series(np.random.randn(9),index = list('asdfghjkl'))
data.plot.bar(ax = ades[0])
data.plot.barh(ax = ades[1])
s2.plot.bar( ax = ades[2] ,stacked  =True)


#tmn,skipped____9.2.2~
#   .plot.hist
#   .plot.density
#   seaborn.displot
#   seaborn.regplot
#
mplt.show()