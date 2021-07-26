class repeater():
    '''
    repeat everything
    '''
    Content = ' '
    Index = 0
    def repeat_in_order(self):
        repeater.Index = repeater.Index + 1
        print(repeater.Index,":",repeater.Content)

    def repeat_start(self):
        repeater.Content = input("What\'s going on ?")

repeaterA = repeater()
repeaterA.repeat_start()
for i in range(1,10,1):
    repeaterA.repeat_in_order()

 