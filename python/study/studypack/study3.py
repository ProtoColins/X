PoemA = ["fan,fan,fan ","i love fan ","fan is my love ","my love is fan"]
PoemB = ["tao,tao,tao ","fan loves tao ","tao is fan's love ","fan's love is tao"]
#dictionaries  (Map object in C&java)
#dict= {'key1':'value 1','key2':'value 2'}
#key&value =anything
dictionary = dict()  #an empty dict //also {}
dictionary = dict(zip(PoemA , PoemB))  #creating dict with lists
#You can also : dictionary = dict(key1 ='value1' ,key2 = 'value2' )

print(dictionary)

dictionary2 =dict.fromkeys(PoemA)   #value = None
print(dictionary2)
dictionary3 = {tuple(PoemA) : PoemB} #dictionary = {tuple : list} 
print(dictionary3) 

#noting that this form of dict is different from 1&2
print(dictionary["fan,fan,fan "])
print(dictionary.get("fan,fan,fan ")) # equal expression
print(dictionary2.get("fan,fan,fan "))
print(dictionary3.get(tuple(PoemA)))
#smtimes ,using if for checking

print(dictionary["fan fan fan"] if "fan fan fan" in dictionary else "sorry" )

##scanning  dict.items()[key+value]  value/keys
for i in dictionary.items():
    print(i)

#modifing
dictionary2.clear()
dictionary3.clear() #clearing
del dictionary2 , dictionary3

dictionary["fan"] = "tao"   #adding item
dictionary["fan"] = "fan"   #modifing item
del dictionary["fan"]       #deleting item(key_based)

#summonning
import random
randict = {i : random.randint(10,100) for i in range(10)}
randict2 = {i : random.randint(10,100) for i in range(10)}  #inrange-summonning
randict3 = {i:j for i,j in zip( PoemA , PoemB ) }       # another way of zipping
print (randict)
print (randict2)
print (randict3)


#Sets
SET = {1,2,3}   #defination of set  {item,item,item}
Poem = []
Poem.extend(PoemA)
Poem.extend(PoemB)
SET= set(Poem)  #using set() creating set

#modifing
SET.add("Fate chosen")

#pop remove clear del
SET.remove("Fate chosen")
SET.pop()
print(SET)

#set calcs:  & for together     | for or    - for minus     ^ for  ???
randict = set(i for i in randict.values())
randict2 = set(i for i in randict2.values())
randict.add(1)
randict2.add(1)
print (randict)
print(randict2)
print(randict & randict2)
print(randict | randict2)
print(randict - randict2)
print(randict ^ randict2)

