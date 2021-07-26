import wx
class HLGUI(wx.Frame):
    '''
    Use to Interact with others \n
    should content: \n
    GUI    login   graphing    
    '''
    U_keylist = [ 'About' , 'Help' ]
    F_keylist = [ 'Settings' , 'About' , 'Help']
    MenuDict = dict( Settings = 'Show OS settings panel' , About = 'Programme and Developer Info' , Help = 'Show any help availible')
    def __init__(self):
        TopWindow = wx.Frame.__init__( self ,None ,id = wx.ID_HOME , title = 'HUANLI OS' )
        
        StatusBar = wx.StatusBar(self,id = wx.ID_HELP_CONTEXT , name = 'Status')      
        self.SetStatusBar(StatusBar)  
        PanelA = wx.Panel( self)
        PanelB = wx.Panel( self )
        TextA = wx.StaticText( self  )
        TextB = wx.StaticText( self )
        Tbox = wx.TextCtrl( self )

    def MakeMenu( self , Mode ):
        Menu = wx.Menu( title = 'TOP')
        MenuBar = wx.MenuBar( )
        if Mode == True :
            for index in HLGUI.F_keylist:
                Menu.Append( id = wx.ID_ANY , item = index , helpString = HLGUI.MenuDict[ index ])
                Menu.AppendSeparator()
        else:
            for index in HLGUI.U_keylist:
                Menu.Append( id = wx.ID_ANY , item = index , helpString = HLGUI.MenuDict[ index ],)
                Menu.AppendSeparator()
        MenuBar.Append( Menu , 'DEMO' )
        self.SetMenuBar(MenuBar)

    def UserManage( self ):
        UMBox = wx.BoxSizer( wx.VERTICAL )
        UMBox.Add( HLGUI.Topwindow , HLGUI.TextA , propotion = 2  )


    @property
    def StartAnim():
        '''a mini initionalizatoin animation'''
        pass
    
    

    


app = wx.App()
GUI = HLGUI()
GUI.MakeMenu(True)
GUI.Show(True)
app.MainLoop()

