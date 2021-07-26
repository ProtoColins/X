import re
vir_pat =r'((^13[4-9])|(^15[1-27-9])|(^18[2-8]))\d{8}$'
phone = str(input("input your phonenumber"))
res = re.match(vir_pat,phone)                    
print ('rightnum' if res != None else "Failed" )
res_num = re.sub('^1\d{10}','1XXXXXXXXXX',phone)
print (res_num)
