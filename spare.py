#Note:

#Docstrings are but one example of Python’s powerful introspection capabilities,
#and we will encourage you to provide them for modules, classes, methods, functions,
#and any other place that Python supports.


#!/usr/bin/env python

"""Spare.py is a starting point for a wxPython program."""

import wx

class Frame(wx.Frame): #Introduce your own custom Frame class
    pass

class App(wx.App):
    def OnInit(self):
        self.frame=Frame(parent=None, title='Spare')
        self.frame.Show()
        self.SetTopWindow(self.frame) #it was inherited from the wx.app parent class.
        return True
if __name__ == '__main__': #test whether the module is being run as a program or was imported by another module.
    app = App()
    app.MainLoop()    
