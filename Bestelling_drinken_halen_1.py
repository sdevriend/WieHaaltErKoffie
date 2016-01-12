"""
Jeroen Kuivenhoven      s1084216

"""

import wx

namen = {1: 'Jeroen', 2: 'Dwin', 3: 'Jolanda', 4: 'Jesse', 5: 'Sebastiaan'}
namen2 = ['Jeroen', 'Jolanda', 'Sebastiaan']
hoogsteschulden = 'Jolanda'

class Be_dr_ha_1_scherm(wx.Panel):
    def __init__(self, parent, id):
        """ 
        """
        wx.Panel.__init__(self, parent, id)
        self.panelen()
        self.titelpaneel = wx.Panel(self, id)
        self.tekstpaneel = wx.Panel(self, id)
        self.tekstpaneel2 = wx.Panel(self, id)
        self.teksten(titelpaneel)
        middenbox = self.functioneel1()
        navigatiebox = self.navigatiebuttons()
        boxje = self.boxen(titelpaneel, middenbox, navigatiebox)
        self.eindbox = wx.BoxSizer()
        #self.SetBackgroundColour((255,255,20))
        self.eindbox.Add(boxje, 1, wx.EXPAND | wx.ALL)
        self.SetSizer(self.eindbox)
        #self.paneel.SetBackgroundColour("Black")

    def panelen(self):
        self.titelpaneel = wx.Panel(self, id)
        self.betaler = wx.Panel(self, id)
        self.tekst = wx.Panel(self, id)
        self.naam1 = wx.Panel(self, id)
        self.naam2 = wx.Panel(self, id)
        self.naam3 = wx.Panel(self, id)
        self.naam4 = wx.Panel(self, id)
        self.naam5 = wx.Panel(self, id)
        self.naam6 = wx.Panel(self, id)
        self.naam7 = wx.Panel(self, id)
        self.naam8 = wx.Panel(self, id)
        self.naam9 = wx.Panel(self, id)
        self.naam10 = wx.Panel(self, id)

    def teksten(self, paneel):
        """ 
        """
        titeltje = wx.StaticText(self.titelpaneel, -1, "Drinken halen",
                                 pos=(0, 5), size=(295, -1),
                                 style=wx.ALIGN_CENTER)
        titeltje.SetForegroundColour((232,144,30))
        titeltje.SetFont(wx.Font(40, wx.DECORATIVE, wx.NORMAL, wx.NORMAL))
        tekst1 = wx.StaticText(self.betaler, -1, "Joep gaat drinken halen",
                                 pos=(5, 3))
        tekst1.SetForegroundColour((255,255,255))
        tekst1.SetFont(wx.Font(15, wx.DECORATIVE, wx.NORMAL, wx.NORMAL))
        tekst2 = wx.StaticText(self.tekst, -1, "Bestelling:",
                                 pos=(5, 3), style=wx.ALIGN_CENTER)
        tekst2.SetForegroundColour((255,255,255))
        tekst2.SetFont(wx.Font(15, wx.DECORATIVE, wx.NORMAL, wx.BOLD))
        

    def functioneel1(self):
        """ 
        """
        totalebox = wx.BoxSizer(wx.VERTICAL)
        #drinkhaler = 
        
        
        
        return totalebox

    def checker(self, event, getal):
        print("gek", getal)
        print(self.drinken_halen_knop.GetValue())
        
    def navigatiebuttons(self):
        """
        """
        self.terug_knop = wx.Button(self, -1, ("Terug"))
        self.prijzenkaart_knop = wx.Button(self, -1, ("Prijzenkaart"))
        self.stop_knop = wx.Button(self, -1, ("Doorgaan"))
        navigatiebox = wx.BoxSizer(wx.HORIZONTAL)
        navigatiebox.Add(self.terug_knop, 1, wx.EXPAND | wx.ALL)
        navigatiebox.Add(self.prijzenkaart_knop, 2, wx.EXPAND | wx.ALL)
        navigatiebox.Add(self.stop_knop, 1, wx.EXPAND | wx.ALL)
        return navigatiebox

    def boxen(self, paneel, box1, box2):
        """ 
        """
        boxje = wx.BoxSizer(wx.VERTICAL)
        boxje.Add(paneel, 1, wx.EXPAND | wx.ALL)
        boxje.Add(box1, 8, wx.EXPAND | wx.ALL)
        boxje.Add(box2, 1, wx.EXPAND | wx.ALL)
        return boxje
