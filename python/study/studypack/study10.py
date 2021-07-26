#file-related commands
#open('name//address','mode',buffer)
file = open('Huanlistudy.txt','wb+')    #default:GBK
#only w w+ a a+ can create files
###ONLY keyword : file(one file at a time only??)

#close it
file.close()

with open('Huanlistudy.txt','w+') as file: 
    file.write('Alone')
#intended to close it within time
###need more info about 'with' 

#file writing

##write the message into buffer,when close() it would it be written
#  file.close()

with open('Huanlistudy.txt','r') as file:
    print(file.read(3)) #also can be sized


#use seek() to move the curosr around the file
with open('Huanlistudy.txt','r') as file:       #warning,using + mode will need IOBASE
    print(file.readline())
    file.seek(0,0)
    for mess in file.readlines():
        print(mess)

#####        Directory            #########
import os
print(os.name)  #show OS version,and alot else
print(os.linesep)  


#abs dir and rel dir
print(os.getcwd())
with open('Nagi.txt','w+') as file:
    file.write('death'+'\n')
    file.write(os.path.abspath('Nagi.txt')+'\n')
    file.write(os.path.join(os.path.abspath('Nagi.txt'),'block\\Nagi.txt')+'\n')
    #use this fuction to join paths ,can avoid bug differ from OS
    file.write(str(os.path.exists(r'hope.txt')))
if not os.path.isdir(r'd:\#PhantomDatabase\X\python\study\Dir'):
    os.mkdir(r'd:\#PhantomDatabase\X\python\study\Dir')
    print('created')
else:
    os.rmdir(r'd:\#PhantomDatabase\X\python\study\Dir')
    print('deleted')
os.makedirs('pre-tests\\box')

#deleting dirs
os.rmdir('pre-tests\\box')
#deleteall :from shutil import rmtree
#Walk  TBa
Walks = os.walk(r'd:\#PhantomDatabase\X',True)
for a in Walks:
    print(a)

#RE-NAME
if not os.path.isdir(r'd:\#PhantomDatabase\X\python\study\DIR'):
    os.renames(r'd:\#PhantomDatabase\X\python\study\Dir',r'd:\#PhantomDatabase\X\python\study\DIR')
else:
    os.rmdir(r'd:\#PhantomDatabase\X\python\study\DIR')
print('complete')
#rename can only modify the last dir
#
# for i in os.stat(r'd:\#PhantomDatabase\X\Nagi.txt'):
#  print(i)
#   WRONG
#AS Test

