#
# this is the through of 利用python数据分析
# 

#review of py turples

tup = 4 , 5 , 6
tup = ( [ 4 , 5 , 6 ])
tup[0]

#拆包赋值
a , b , c = tup
a , *resb = tup
#交换赋值
a , b = b , a

#lists
lis = [range(0,10,2)]
lis.append(1)
lis.insert(-1,"sa-bi")
lis.pop(-1)
try:
    lis.remove(1)
finally:
    pass

0 in lis
1 not in lis

lis+lis
lis.extend(lis)
lis.sort( key = len ) # other keys*

# --- bisect --- #

#    import bisect

### SLICING ###
lis [ 1 : 5 : 2]
lis [ 0 : 1 ] = [ 3 ,4 ]

#Enumeration , return (index & value)
for index , value in enumerate ( lis ):
    pass

sorted(lis) #keys same as sorted

#zippin'

zip ( tup , lis , tup)
zip( [('a','b'),('c','d')])

#dict
dic = enumerate(lis)
dic.update(dict(1,0))
dic.get( key = 1 ,default_value = 0 )
dic.pop( key = 1 ,default_value = 0 )
#   dic.setdefault( )  ?
#dict keys hashmethod
hash(1)

# object generation
[(i+1) for i in lis if (i is not None)]
# expr for val in collection if condition
# for val in collection:
# if condition:
# result.append(expr)
dict_plus = {(i+1):(i+2) for i in lis if (i is not None)}
# key_expr : value_expr for expr
{(i+1) for i in lis if (i is not None)}

#? set(map(len,strings))

data=[['a'],['b']]
multiple_gen = [name for names in data for name in names]
#
#   for names in all data:
#       full = [name for name in names if ~]
#       result.append(full)

#iterator::
iter(lis)

def giveout(intiger):
    for i in range(intiger):
        yield i 
#Asking contents in iter will it move

#File systems
# read seek tell
