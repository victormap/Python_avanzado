import wx

class Ventana_Ejemplo(wx.Frame):
    def __init__(self, parent, title):
        super(Ventana_Ejemplo, self).__init__(parent, title="Segunda Ventana", size=(20, 20))
        self.Show(True)

app = wx.App()
ventana = Ventana_Ejemplo(None, 'Hola')