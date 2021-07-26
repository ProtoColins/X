#==What is ndarray:
import numpy as np
#it contains: 
# pointer to data
# dtype data for ram bloacks:
# turple for shape
# turple for step(dimensions)
# ...?


#== reshaping:
len = np.arange(0,36)
print(len.reshape((3,12)))
print(len.reshape((3,12)).reshape((12,3))) #==len.reshape(12,3)


#C-way: first go through higher dim
#Fortan : first go through lower dim

#arr connnection/seperation
arr1 = np.array([[1,2,3],[4,5,6]])
arr2 = np.array([[7,8,9],[10,11,12]])
#1: vstack / hstack
print(np.vstack(arr1,arr2))
print(np.hstack(arr1,arr2))
#2: split 
arr = np.random.randn(6,6)
np.split(arr,[1,3])
#more: contanate / vstack,hstack / column_stack / dstack / split / hspilt,vsplit

#? r_ , c_
np.r_(arr1,arr2)
np.c_(arr1,arr2)


#repeating elements:
arr = np.arange(3)
arr.repeat(3) #repeat numbers individually
arr = np.array([[1,2,3],[4,5,6]])
arr.repeat(3 , axis=1) #if no axis= param , it will be flattened first
np.tile(arr , 3 ) # repeat whole list

#broadcasting:

