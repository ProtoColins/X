import os

def mkdirU( path ):
    '''
    Split path and create it fully
    '''
    T = []
    temp = [str(path)]
    while True :
        
        if not os.path.isdir(temp[0]):
            temp = os.path.split(temp[0])
            T.append(temp[1])
            continue
        else:
            j = temp [ 0 ] 
            i = - 1 
            while not os.path.isdir(path):
                j = os.path.join(j ,T[i])
                os.mkdir(j)
                i -= 1
        print('successful')
        break
                    

        

    
mkdirU(r'D:\Kaze\Huanli\Colins\Heart\Main\Killer')

