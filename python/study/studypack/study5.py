#zhen ze biao da shi
import re
#INculding

#   ^ start of a line  / $ endl    ^keyword / keyword$  orboth: keyword(also \b)
#  .(anychar but /n)  \w(word)  \s(anyblank)  \d(int)  
#exapmle  \bhat\w\bcup

#time limit   ?for 0/1  +for 1or more  *for any   {n} for n times  {n,} for atleast n  {n,m}for n<= time <= m

#set,connect with - :[0-3],[a-p],[A-C],[0-3a-c]

#EXcluding    [^a-z0-3]

#logicing  :  |  
#(^\d{15})|(^\d{18})|(^\d{17})(^\d|X|x)
#use \ for any char used in the program


#how to use re:
pat1 =r'main*'
# \b\w*\b  wrong
pat2 = '\\b\\w*\\b' #  r'\b\w*\b' also right
match = re.match(pat1,'mainnnnn',re.I)
match2 = re.match(pat1,'miannnn',re.I)
print(match,'\n',match2,end = "\n")
#indexin match object:
#??????   COME BACK WHEN YOU MASTERED DEALING WITH OBJECTS

#match only match the firstwords ,use search for full-string-matching
print(re.search(pat1,'mianmain',re.I),end = "\n")
#search only get one feedback,use findall for all answers
print(re.findall(pat1,'mainminmiamainnnnfaubdmainnmabimmain',re.I))

ip_pat = r'[1-9]{3}(\.[0-9]{1,3}){3}'
print(re.findall(ip_pat ,'192.168.131.1'))  #only for ()content
print(re.findall(r'([1-9]{3}(\.[0-9]{1,3}){3})' ,'192.168.131.1'))  #right result, but only for the 1st   (?????)

#sub(see pre-test,replacing)
#spliting
url = 'http://www.huanliHQ.com/database.jsp?username="Colins"&checkdata=date'
print(re.split(r'[?|&]',url))



