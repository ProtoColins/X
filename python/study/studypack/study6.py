def firstfunction ( seed , name = 'huanli'):    #deafult value
    '''
    generate the uiltimate answer of the universe \n
    return the truth
    '''
    seed = seed + 1
    return 42

print(firstfunction(3075,'huanli'))
print(firstfunction(name = 'huanli',seed = 3075))

#multuple params
def secondfunction (*shards):       #also use * to create a tuple parm 
    '''
    useless to confort yourself
    '''
    for item in shards:
        print(item)

secondfunction('sadness','sad','saad')

def thirdfunction( **memori ):      # ** turn sth into a dict
    '''
    kylie eleision
    '''

    global hope
    hope = 'dead'
    for  index in memori:
        print( index +' is '+memori[index] ,end = '\n' )

thirdfunction( head = 'Phill' , Programmer = 'Colins', Guard = 'Chaos' ,equitiee = 'void')

#claiming golbal var
print(hope)

#lambda function
import math
r = 10
cover = lambda r : math.pi * r**3 *4 /3
print(cover(r))

