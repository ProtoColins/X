##Errors
#recite errorlist
try:
    ##code##
    tpu = 0/0
except ZeroDivisionError:
    print('you fool')
except ValueError as e :
    print(e)
else:
    print ('owo')
finally:
    print('you should remember the sort')

#raise error
raise ZeroDivisionError('mie')

#only when in debugmode
# assert (expression,reason[when false])
assert 0+0 , 'its\' false'
