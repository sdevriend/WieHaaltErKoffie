"""
Jeroen Kuivenhoven      s1084216

"""

import wx


class Logscherm(wx.Panel):
    def __init__(self, parent, days, log):
        """ 
        """
        self.days = days
        self.log = log
        wx.Panel.__init__(self, parent)
        titelpaneel = wx.Panel(self)
        self.teksten(titelpaneel)
        self.menubuttons(titelpaneel)
        self.radio(titelpaneel)
        self.logbox(titelpaneel)
        boxje = self.boxen(titelpaneel)
        self.eindbox = wx.BoxSizer()
        self.eindbox.Add(boxje, 1, wx.EXPAND | wx.ALL)
        self.SetSizer(self.eindbox)

    def teksten(self, paneel):
        """ 
        """
        titeltje = wx.StaticText(paneel, -1, "Logscherm",
                                 pos=(10, 10), size=(295, -1),
                                 style=wx.ALIGN_LEFT)
        titeltje.SetForegroundColour((232,144,30))
        titeltje.SetFont(wx.Font(40, wx.DECORATIVE, wx.NORMAL, wx.NORMAL))

    def menubuttons(self, paneel):
        """ 
        """
        self.terug = wx.Button(paneel, -1,'Terug', pos=(10, 330), size=(200, 60))

    def radio(self, paneel):
        """
        """
        self.stTxtDatum = wx.StaticText(paneel, -1, "Datum", pos = (15, 80))
        self.stTxtDatum.SetForegroundColour((255,255,255))
        self.CBDatum = wx.ComboBox(paneel, -1, "alles",pos=(55, 80), choices=self.days)

    def logbox(self, paneel):
        self.list = wx.ListCtrl(paneel, -1, pos=(15,110), size=(550, 200), style=wx.LC_REPORT|wx.SUNKEN_BORDER)
        self.list.SetBackgroundColour((46,24,0))
        self.list.SetTextColour((255,255,255))
        self.list.Show(True)
        self.list.InsertColumn(0,"Datum", width=130)
        self.list.InsertColumn(1,"Geberurtenis",  width=wx.LIST_AUTOSIZE_USEHEADER)

        try:
            for i in reversed(self.log):
                for a in i:
                    pos = self.list.InsertStringItem(0,str(a[0]))
                    self.list.SetStringItem(pos,1,str(a[1]))
        except:
            pass
        
    def boxen(self, paneel):
        """ 
        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(self.new, 0, wx.CENTER, wx.TOP, 30)
        vbox.Add((1, 1), 2)
        vbox.Add(self.ren, 0, wx.CENTER,wx.TOP, 30)
        vbox.Add((1, 1), 2)
        vbox.Add(self.dlt, 0, wx.CENTER,wx.TOP, 30)
        vbox.Add((1, 1), 2)
        vbox.Add(self.clr, 0, wx.CENTER,wx.TOP, 30)
        vbox.Add((1, 1), 2)
        """
        
        boxje = wx.BoxSizer(wx.VERTICAL)
        boxje.Add(paneel, 1, wx.EXPAND | wx.ALL)
        
        #boxje.Add(vbox, 8, wx.EXPAND | wx.ALL)
        return boxje
