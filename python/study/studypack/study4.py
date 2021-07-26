#STRINGS    str&bytes
STRING = 'TaoFan涛帆HuanliKaze幻卡'
#STRING.encode([ encoding :"utf-8"] [errors:"strict"]) 
STRING.encode(encoding = "utf-8",errors= "strict")
#encoding parms:    utf-8  gb2312(chinese) GBK also opt out"encoding"if there is only "codelanguage"
#errors parms:  strict:error when fail(default)  /   ignore:skip when fail   /   relpace: ? for illegal  /xmlcharrrefreplace
print(STRING+"\n")

STRING = STRING.encode("GBK")
print(STRING)

#decoding
STRING = STRING.decode(encoding = "GBK", errors= "strict")  #you need to re-give it
print(STRING)

#string combining
name1 = 'Tao涛'
name2 = 'Fan'
print(name1 + ' love ' + name2 + '\n')

#length of STRING   len() counting anyting as 1
#to split chinese and others,encode first
print(len(name1))
name1 = name1.encode(encoding= 'GBK',errors= 'strict')
print(len(name1))
name1 = name1.decode(encoding= 'GBK',errors= 'strict')
print(len(name1))
#use to calc differrnt language chars,no use when only english

#slicing
print(name1[0:4:1] + "\t")  #continuious output
#spliting
COG = "12345678901234567890"
print(COG.split("0"))   # sep , maxsplit 
#join
Fate = "*".join(COG.split("123"))
print(Fate)
#count(output int)
print(COG.count("123"))
#find (output index)
print(COG.find("123"))
#index(simplified find(error))
print(COG.index("123"))

#starts/ends with
print(COG.startswith("123"),COG.endswith("890"))

#lower/upper
#strip,rstrip lstrip

####TEMPLATE
#   multiple arguments need to be turpled
template = ' CODE: %d %d %d'
#  %s   %c    %d    %x  %f   %r    %o    %e    %E    %%
fill = (1,2,3)
print(template % fill )
#OR  str.format(arguments)       {[ index    ][:[[  fill    ]   align   ][  sign    ][ # ][    width   ][   .precision  ][  type  ]}
#                                 auto/manu         (???)   fixtype     (???)      show 0b/0o/0x                          datatype
print('main{:^d}'.format(1))