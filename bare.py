import wx #Step1, import wxPython

class App(wx.App): #working with application and frame
    def OnInit(self): #Define an application initializtion method
        frame = wx.Frame(parent=None, title ='Bare')
        frame.Show()
        #frame.Hide()
        return True
app = App() #Create an application class instant
app.MainLoop() #Enter its main event loop
