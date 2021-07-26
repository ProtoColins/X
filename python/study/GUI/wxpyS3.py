import wx

class Interface(wx.Frame):
    def __init__(self,parent,title):
        wx.Frame.__init__(self,parent = parent, title= title )
        self._TEControl = wx.TextCtrl(self ,value = 'defaut content',style = wx.TE_MULTILINE)
        self.CreateStatusBar()

        self._filemenu = wx.Menu( )

        self._filemenu.Append(wx.ID_ABOUT, 'ABOUT' , 'More information about this program&developer')
        self._filemenu.AppendSeparator()
        self._filemenu.Append(wx.ID_EXIT , 'EXIT' , 'Terminate this program')

        self._MenuBar = wx.MenuBar()
        self._MenuBar.Append(self._filemenu,'Head')
        self.SetMenuBar(self._MenuBar)
        self.Show(True)

app = wx.App()
Frame = Interface(parent =  None ,title = 'HLOS' )
app.MainLoop()
