import wx
import Schuldenscherm
import VereffenSchuld

class SchuldenSchermCode(wx.Frame):

    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size=(750, 600))
        self.setpanel()
        self.startscherm()
        self.buttonevents()

    def setpanel(self):
        self.paneel = wx.Panel(self, -1)
        self.paneel1 = Schuldenscherm.Schuldenscherm1(self.paneel, -1)
        self.paneel2 = VereffenSchuld.VereffenScherm(self.paneel, -1)

    def startscherm(self):
        self.boxje = wx.BoxSizer(wx.VERTICAL)
        self.boxje.Add(self.paneel1, 1, wx.EXPAND)
        self.boxje.Add(self.paneel2, 1, wx.EXPAND)
        self.panelhide(self.paneel1, (750, 600))
        self.paneel.SetSizer(self.boxje)
        self.Centre()
        self.Show(True) 
           
    def panelhide(self, zie, bh):
        self.paneel1.Hide()
        self.paneel2.Hide()
        zie.Show()
        self.SetSize(bh)
        self.Centre()
        self.Refresh()

    def buttonevents(self):
        self.paneel1.Terug.Bind(wx.EVT_BUTTON, self.TerugButton)
        self.paneel1.Schuldknop.Bind(wx.EVT_BUTTON, self.SchuldButton)
        self.paneel2.Vereffenknop.Bind(wx.EVT_BUTTON, self.VereffenButton)
        self.paneel2.drop1.Bind(wx.EVT_COMBOBOX, self.DropButton1)
        self.paneel2.drop2.Bind(wx.EVT_COMBOBOX, self.DropButton2)

    def TerugButton(self, event):
        #Code voor scherm terug
        pass

    def SchuldButton(self, event):
        self.panelhide(self.paneel2, (450, 300))
        
    def VereffenButton(self, event):
        print(self.schuldige)
        print(self.schuldeiser)
    
    def DropButton1(self, event):
        self.schuldige = self.paneel2.drop1.GetValue()

    def DropButton2(self, event):
        self.schuldeiser = self.paneel2.drop2.GetValue()
        


app = wx.App(False)
SchuldenSchermCode(None, -1, "Schuldenscherm")
app.MainLoop()
