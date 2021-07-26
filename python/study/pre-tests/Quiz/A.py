lista = [1,1,0,0,0,1,2,3,4,5,5,5,999]
#rearrange them accroding to frequency
Values = []
for i in lista:
    if not Values.count(i) > 0:
         Values.append(i)
d1 = {}
DICT = d1.fromkeys(Values,0)
for i in lista:
    DICT[i] = DICT[i] + 1
print(DICT)


