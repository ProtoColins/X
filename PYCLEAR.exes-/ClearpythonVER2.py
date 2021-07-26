import  os
Stat = input('Are you Sure to clear all .exe files? Y/N')
if (Stat.lower != 'y'):
    path = os.getcwd()
    Walks =os.walk(path,True)
    
    PIPE = {}
    indexes =  0
    for item in Walks:
        for data in item[2]:
            if data.endswith(".exe"):
                name = item[0] + '\\' + data
                PIPE.update({ indexes :name} )
                indexes += 1
    if (PIPE != {}):
        print('Find EXES as follows:')
        for i  in PIPE :
            print(  PIPE.get(i)  )
        Stat2 = input('Really delete them? Y/N')
        if (Stat.lower != 'y'):
            for i in PIPE:
                try :
                    os.remove( PIPE.get(i) )
                    print ( PIPE.get(i) + " is successfully removed!")
                except os.error:
                    print("failed to remove " + PIPE.get(i) )
                    print("exececution complete")
                    exit()
        else:
            
            exit()   
         
    else:
        print("find no .exe files qwq")
        print("exececution complete")
        exit()            
else:
    exit()
    