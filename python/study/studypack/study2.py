#python study of verses
#two types of indexing:

PoemA = ["fan,fan,fan ","i love fan ","fan is my love ","my love is fan"]
PoemB = ["tao,tao,tao ","fan loves tao ","tao is fan's love ","fan's love is tao"]
print([PoemA[3]])  #versed output
print(PoemA[-1])

#slicing:summon a new Poem//sname[start:end:step]  or verse[:] for a full repelication

print(PoemA[0:3:2])

#verse combination  + and *

print(PoemA + PoemB)
Emptylist = [None] * 5
del Emptylist
Mat =[0]

for i in range(1,10,1):
    Mat = Mat + [i]    #Or Mat = list(range(1,10,1))
print (Mat)

# check:  (bool) = value in// not in sequence 

print (3 in Mat)

#len(name)[length] max(~) min(~) 
#TBA : list() convert a verse into a list   //what's the difference??         
# str() verse to string(itis a string(-))
# sum()   sorted()  reversed() enumerate()?????
#              
#For a list ,it can contain everything

for index,buffer in enumerate(PoemA) :   # note that there's no need for claiming a temp-variable
    print( index ," "*2 + buffer)        # also,caution the types when print

#enlargeing lists   +(lowspeed)  listname.append()^insert()extend()

PoemA.append("and then")
Poem = PoemA
Poem.extend(PoemB)
print(Poem)
Poem[4] ="For sure"
print(Poem)

#deleting units
del Poem[4]
#test is a must,or would exit  use count for checking
if Mat.count(0)>0:
    Mat.remove(0)
else:pass   #or 0 in Mat
#listname.index() for the first index an object appers,also check, or would exit
#now sort
Poem.sort( key=str.lower , reverse = False )  #Also sorted(~,~,~)
print(Poem)

#expression for list
LIST = [ (x**2) for x in Mat if x <= 8]
del LIST
Arr = []
for i in range(4):
    Arr.append([])
    for j in range(4) :
        Arr[i].append(j)  #remember the grammar
print(Arr)        
del Arr
Arr =[[ i**j for j in range(4)] for i in range(5)]
print (Arr)
#expecting for more dimensions

#tuple time(inchangeable list)
tupleA = (1,1,1,1)
tupleB = ("Poem","PoemA",PoemB)#no need for a bracket
tupleC = ("main"),
tuple(range(1,100,10))

#tuples are inchangable ,but re-defination is ok
tupleC = tupleB

#however ,appending is considerable
tupleC = tupleA +tupleB
print(tupleB)

#tuple generation needs an extra converting

import random
randommain =(random.randint(10,100) for i in range (10))
print(randommain)
#GENERATOR OBJECT
randommain = tuple(randommain)
print(randommain)