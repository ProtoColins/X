#Class objects

class PRCV:
    '''
    check if a member is its member
    '''
    def __init__ (self,PID):        #init way is combined to class claiming 
        #forming way  == a function defined in a class,operate with given params
        #[all functioins] self(also other names) param should not be given to ,but you can give sth others
        print('memberlist')

#for a class, it's body share same charri- with a function
#to create a example
Phill = PRCV(123)      #New data type,execute __init__
print(Phill)


###_______________________
class Huanli:
    '''
    The 3rd genneration of a VIR group
    '''
    heart = 'void'
    memberlist = ('Phill','Colins','Chaos','Void')

    def checkPID(self,PID):
        self.heart = 'empty'         #only accesilbe with a entity,    need:self
        print(PID,self.heart)

#How to use a class&its functions
#InstanceName.FuctionName(paramlist)
HuanliDemo = Huanli()           #Fisrt create a Instance,it will automatically do the class job
HuanliDemo.checkPID(123)        #then call the instance


#data menbers : defined in the class
#A :class-global must add classname
print(Huanli.memberlist)

#modify/add class parm
Huanli.char = 'sincere'
print (Huanli.char)
#B:built-in parm
print(HuanliDemo.char)  #it shared its father-set characteristics  
print(HuanliDemo.heart) #not Huanli.heart
print(Huanli.heart)  

#strcict request
class final:
    '''
    nothing
    '''
    _bot =  '1' #protected ,only inferrior and self  can't 'from module import'
    __bot2 ='2' #private , only this class or its ori function   
    def __init__(self):
        print(final._bot)           #direct request  A

boo = final()
print(boo._bot)                     #object request  A

print(boo._final__bot2)         #private,acc from instance.class.__XXXX

#property
class Rect():
    '''
    rectangle
    '''
    def __init__(self,a,b):
        self.width = a
        self.length = b 
    @property      #no arguments
    def area(self):      
        return self.width * self.length

square = Rect(10,10)
print(square.area)   #un re-nameable

#       @ property is also used to protect it while still accessible 
class safe:
    '''
    it's not safe
    '''
    def __init__(self,data):
        self.__data = data
    @property
    def obtdata(self):
        return self.__data

soul = safe('me')
print(soul.obtdata)     #ok
#soul._safe__data    no

#base#
class HL:
    '''
    code of huanli
    '''
    color = ''
    def __init__(self):
        HL.color = 'white'
    def verify(self,name):
        
        print( name if name in Huanli.memberlist else 'failed')
        print(HL.color)
class Phill(HL):
    '''
    dead guy
    '''
    def __init__(self):
        super().__init__()              #to re-use its father class-__init__
    def verify (self , name = '123'):
         
        print('NObody is verified',HL.color)

Phill.verify(1)      #re-writing    
    
