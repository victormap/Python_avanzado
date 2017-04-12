import wx

app = wx.App()
frame = wx.Frame(None, -1, 'Primer Ventana', style = wx.MINIMIZE_BOX | wx.MAXIMIZE_BOX | wx.RESIZE_BORDER | wx.SYSTEM_MENU | wx.CAPTION)
frame.Show()

app.MainLoop()