"""
Jeroen Kuivenhoven      s1084216

"""

import wx


class Logscherm(wx.Panel):
    def __init__(self, parent):
        """ 
        """
        wx.Panel.__init__(self, parent)
        titelpaneel = wx.Panel(self)
        self.teksten(titelpaneel)
        self.menubuttons(titelpaneel)
        self.radio(titelpaneel)
        self.log(titelpaneel)
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
        titeltje.SetForegroundColour((255,191,0))
        titeltje.SetFont(wx.Font(40, wx.DECORATIVE, wx.NORMAL, wx.NORMAL))

    def menubuttons(self, paneel):
        """ 
        """
        self.terug = wx.Button(paneel, -1,'Terug', pos=(10, 330), size=(200, 60))

    def radio(self, paneel):
        """
        """
        self.stTxtDatum = wx.StaticText(paneel, -1, "Datum", pos = (15, 80))
        self.stTxtDatum.SetBackgroundColour((255,255,255))
        keuze = ["alles","vandaag", "1 dag geleden", "2 dagen geleden", "3 dagen geleden", "4 dagen geleden",
                 "5 dagen geleden", "6 dagen geleden"]
        self.CBDatum = wx.ComboBox(paneel, -1, "alles",pos=(55, 80), choices=keuze)

    def log(self, paneel):
        lijst = [("7-1-16", "Jesse is Homo."), ("7-1-16", "Bier!"), ("6-1-16", "geen zin meer"), ("5-1-16", "Noit gehad")]
        self.list = wx.ListCtrl(paneel, -1, pos=(15,110), style=wx.LC_REPORT|wx.SUNKEN_BORDER)
        self.list.SetBackgroundColour((46,24,0))
        self.list.SetTextColour((255,255,255))
        self.list.Show(True)
        self.list.InsertColumn(0,"Datum")
        self.list.InsertColumn(1,"Geberurtenis",  width=wx.LIST_AUTOSIZE_USEHEADER)

        for i in reversed(lijst):
            pos = self.list.InsertStringItem(0,i[0])
            self.list.SetStringItem(pos,1,i[1])

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
