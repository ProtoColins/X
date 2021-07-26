import wx
class Interface(wx.Frame):
    def __init__(self,parent,title):
        super().__init__( parent , title = title)
        self.control = wx.TextCtrl(self,value = 'QWQ',style = wx.TE_MULTILINE)
      
###Notice that in function defination , you still need to find 
# DEFAULTING AND PASSING
# realize that *args  &*kwargs
if __name__ == '__main__':
    app = wx.App()
    HLOS = Interface(None,'HLOS')
    HLOS.Show()
    app.MainLoop()
