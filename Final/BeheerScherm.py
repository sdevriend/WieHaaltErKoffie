"""
Jeroen Kuivenhoven      s1084216

"""

import wx


class Beheerscherm(wx.Panel):
    def __init__(self, parent):
        """ 
        """
        wx.Panel.__init__(self, parent)
        titelpaneel = wx.Panel(self)
        self.teksten(titelpaneel)
        self.menubuttons(titelpaneel)
        self.navigatiebuttons()
        boxje = self.boxen(titelpaneel)
        self.eindbox = wx.BoxSizer()
        self.eindbox.Add(boxje, 1, wx.EXPAND | wx.ALL)
        self.SetSizer(self.eindbox)

    def teksten(self, paneel):
        """ 
        """
        titeltje = wx.StaticText(paneel, -1, "Beheer",
                                 pos=(10, 10), size=(295, -1),
                                 style=wx.ALIGN_LEFT)
        titeltje.SetForegroundColour((255,191,0))
        titeltje.SetFont(wx.Font(40, wx.DECORATIVE, wx.NORMAL, wx.NORMAL))

    def menubuttons(self, paneel):
        """ 
        """
        self.pri = wx.Button(paneel, -1,'Verander prijzenlijst', pos=(350, 110) ,size=(250, 60))
        self.geb = wx.Button(paneel, -1,'Gebruikers beheren', pos=(350, 190), size=(250, 60))
        self.log = wx.Button(paneel, -1,'Logbestand', pos=(350, 270), size=(250, 60))
        self.terug = wx.Button(paneel, -1,'Terug', pos=(10, 330), size=(200, 60))
        
    def navigatiebuttons(self):
        """
        """
        self.terug_knop = wx.Button(self, -1, ("Terug"))

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
