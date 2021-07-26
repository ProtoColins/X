#           NDARRAY!!!!!!
import numpy as n

#summoning ndarry

a = n.array(1,dtype=n.int32)     #any listform object

b = n.arange(0 ,20 ,2 ) #range for a ndarry     

c = n.asfarray(a)       #convert to ndarry

#ones ,ones_like ,zeros,empty,full,eye,etc

data = n.random.randn(4,5)



#ndarry features:

data.shape
data.dtype
data.ndim

##ndarry  methods

data.reshape((5,4))
data.astype(n.float64)

#   NUMPY  calc (when two same array): by item
data + data - data *  data / data 
#   Not same : radio?? feature

#numpy slicing:     slicing is not making replica!!
one_dimension = data[1]
data[1:-1] = 1
data[:]
data[1:-1].copy()

higher_dimension = data[0][3]
also_higher = data[0,3]
multiple = data[ 0:1 , 1:3 ]
data[:,:]

bool_array = (data == 1)
how_to_useba = (data[~bool_array])
#booling will copy it(use | , &)
data[data < 0] = 0   #exapmle

#? Magic indexing , always return 1-dim array
data[[-1,-2,-3]]  #????

#axis shifts__ from axis ( transpose )
complexarray = n.array([[[1,2,3],[4,5,6]],[[7,8,9],[0,0,0]]])
complexarray.transpose((2,0,1))

#ufunc: not below ufunc
n.sqrt(data)
n.maximum(data[0],data[1])
n.exp(data)

#ndarry for object ori-programme

# array- oriented programming
xs , ys = n.meshgrid( data , data)

type(xs)
type(ys)


# where ( x if condition else y)
n.where(bool_array ,data ,data)

#statistic means

stdarr = n.random.randn( 5,5)
stdarr.mean( axis = 1)
stdarr.sum()
stdarr.cumsum()

#bool array meathods:
bools = n.asfarray(data , dtype= bool)
bools.any
bools.all


#sorting:
stdarr.sort()
stdarr.sort( 1 )
#####SEE more at pandas ,etc

#logics abouts( towards 1d array)

n.unique(data)

###         saving data             ####

n.save('balhbalhname', stdarr)
#ar = n.load('balhbalhname')
n.savez('/oasfubcie' , c = data , b = stdarr)
#ar = n.load('/oasfubcie')
#ar[b]
#ar[c]

# linar alog:
stdarr.dot(stdarr)
n.dot(stdarr,stdarr)

#------more see reference,as you hadn't learnt l.a

# fake random numbers:

n.random.seed(17)
#blahblahblah