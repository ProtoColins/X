import pandas as pd
 #pandas read a_looot
 #  read_csv ,read_table
 #  read_excel , read_json
 #  read_sql

MEOW = pd.read_csv(r'D:\#CXNOVA\UNI-STOCK\Codes\Dummies\meow.csv')

MEOW = pd.read_table(r'D:\#CXNOVA\UNI-STOCK\Codes\Dummies\meow.csv',sep = ',')
print(MEOW)  # will auto give it an index
MEOW = pd.read_csv(r'D:\#CXNOVA\UNI-STOCK\Codes\Dummies\meow.csv',header= None)
print(MEOW)
#or pass name_list to it

print(pd.read_csv(r'D:\#CXNOVA\UNI-STOCK\Codes\Dummies\pydata-book-2nd-edition\examples\ex6.csv',nrows= 6))
#readlines()

chunker = pd.read_csv(r'D:\#CXNOVA\UNI-STOCK\Codes\Dummies\pydata-book-2nd-edition\examples\ex6.csv',chunksize= 100)
blah = pd.Series([])
for gaba in chunker:
    blah = blah.add( gaba['key'].value_counts() , fill_value = 0)
print(blah)
#READ WITH CHUNKS

#write to
blah.to_csv(r'D:\#CXNOVA\UNI-STOCK\Codes\Dummies\pydata-book-2nd-edition\examples\waaaaa!.csv',na_rep='?')
#you can outline the index and columns(headers)
blah.to_csv(r'D:\#CXNOVA\UNI-STOCK\Codes\Dummies\pydata-book-2nd-edition\examples\waaaaa!.csv', index = [],columns=[])
#pass a list for write specific lines


import sys
blah.to_csv(sys.stdout ,sep='|')  #sys.stdout cmdcontroller

#you can also fileout series


#? using sep-format
import csv
files = open(r'D:\#CXNOVA\UNI-STOCK\Codes\Dummies\pydata-book-2nd-edition\examples\ex7.csv')
reader = csv.reader(files)
for item in reader :
    print(item)      #losing marks  " "
files.close
#then list it ,zip it ,etcetcetc

#own csv Dialect:
class Dialect(csv.Dialect):
    '''?dialect'''
    lineterminator = "\n"
    delimiter = ";"
    quotechar = "'"
    quoting = csv.QUOTE_MINIMAL    # ? what is this ?
    doublequote = True

    # can also pass parms directly tp reader



#jsons:
import json

jsoncontent = '''[{"a": 1, "b": 2, "c": 3},
 {"a": 4, "b": 5, "c": 6},
 {"a": 7, "b": 8, "c": 9}]
'''

result = json.loads(jsoncontent)

result = json.dumps(result)

#see more at chapter 7


####! XML HTML capturing

tables = pd.read_html(r'D:\#CXNOVA\UNI-STOCK\Codes\Dummies\pydata-book-2nd-edition\examples\fdic_failed_bank_list.html')
print(len(tables),"\n",tables[0].head())

from lxml import objectify
parsed = objectify.parse(open(r'D:\#CXNOVA\UNI-STOCK\Codes\Dummies\pydata-book-2nd-edition\datasets\mta_perf\Performance_MNR.xml'))
rooot = parsed.getroot()

#### an i dont know example ####
data  = [ ]
skip_fields = ['PARENT_SEQ' , 'INDICATOR_SEQ' , 'DESIRED_CHANGE' ,'DECIMAL_PLACES']
for elt in rooot.INDICATOR :
    el_data = {}
    for child in elt.getchildren() :
        if child.tag in skip_fields:
            continue
        el_data[child.tag] = child.pyval
    data.append(el_data)

#qwq


#? binary data storage
# short storage
frame =pd.read_csv(r'D:\#CXNOVA\UNI-STOCK\Codes\Dummies\meow.csv',)
frame.to_pickle(r'D:\#CXNOVA\UNI-STOCK\Codes\Dummies\meow_pickle')


#read_excels:
xlsx = pd.ExcelFile(r'D:\#CXNOVA\PPAC\大学阶段\Miscellaneous\A_data.xlsx')
print(pd.read_excel(xlsx))
#write excels:

writer = pd.ExcelWriter(r'D:\#CXNOVA\UNI-STOCK\Codes\Dummies\pydata-book-2nd-edition\examples\ex1.xlsx')
blah.to_excel(writer , 'Sheet2')
writer.save

#or to_excel(filepath)

#WEB API
import requests
url = r'https://cn.bing.com/'
#resp = requests.get(url).json()
#print(resp[0]['title'])
