import wx
class app(wx.App):
    def OnInit(self):
        frame = wx.Frame(parent = None , title = 'HLOSDEV')
        frame.Show()
        return True
App = app()
App.MainLoop()
