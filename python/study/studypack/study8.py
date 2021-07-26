#modules and its func
##   all modules are .py files

#import would execute all lines in that py.file
#to conquer this ,use if(__name__ == '__main__")

#import [modulename] [as alias]
import math as m
#when with modulename math is replaced with m
#all func/vars need [modulename.X]

#from [module] import [member/* for all]
#no need for adding modulename
from math import pi 
print(dir())  #to see all imported definations 

import sys
#         sys.path.append('Mouduleaddress')
#to temporally install a  moudule
