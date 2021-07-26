import sys , os 

Stat = input('Are you Sure to clear all .exe files? Y/N')
if (Stat != 'Y'):
    exit()
else:
    path = os.getcwd()
    
    Walks =os.walk(path,True)
    
    for item in Walks:
        for data in item[2]:
            if data.endswith(".exe"):
                name = item[0] + '\\' + data
                try :
                    os.remove( name )
                    print ( name + " is removed!")
                except os.error:
                    print("failed to remove " + name )
                
                    
    print("exececution complete")
            