"""
Jeroen Kuivenhoven      s1084216

"""

import wx
import random

hoogsteschulden = 'Jolanda'
#keuzes = ["cola", "bier", "koffie"]

class Be_dr_ha_1_scherm(wx.Panel):
    def __init__(self, parent, id, bestellers, prijzen, tijd):
        """ 
        """
        self.bestellers = bestellers
        self.prijzen = prijzen
        self.keuzes = []
        for x in self.prijzen:
            self.keuzes.append(x[1])
        if tijd == "koffie":
            self.keuzes.remove("Bier")
            self.keuzes.remove("Wijn")
        #print(prijzen)
        wx.Panel.__init__(self, parent, id)
        self.panelen()
        #self.titelpaneel = wx.Panel(self, id)
        #self.tekstpaneel = wx.Panel(self, id)
        #self.tekstpaneel2 = wx.Panel(self, id)
        self.teksten()
        self.functioneel()
        middenbox = self.totaal()
        navigatiebox = self.navigatiebuttons()
        boxje = self.boxen(middenbox, navigatiebox)
        self.eindbox = wx.BoxSizer()
        #self.SetBackgroundColour((255,255,20))
        self.eindbox.Add(boxje, 1, wx.EXPAND | wx.ALL)
        self.SetSizer(self.eindbox)
        #self.paneel.SetBackgroundColour("Black")

    def panelen(self):
        self.titelpaneel = wx.Panel(self, -1)
        self.betaler = wx.Panel(self, -1)
        self.tekst = wx.Panel(self, -1)
        
        """self.naam1 = wx.Panel(self, -1)
        self.naam2 = wx.Panel(self, -1)
        self.naam3 = wx.Panel(self, -1)
        self.naam4 = wx.Panel(self, -1)
        self.naam5 = wx.Panel(self, -1)
        self.naam6 = wx.Panel(self, -1)
        self.naam7 = wx.Panel(self, -1)
        self.naam8 = wx.Panel(self, -1)
        self.naam9 = wx.Panel(self, -1)
        self.naam10 = wx.Panel(self, -1)"""

    def teksten(self):
        """ 
        """
        titeltje = wx.StaticText(self.titelpaneel, -1, "Drinken halen",
                                 pos=(0, 5), size=(295, -1),
                                 style=wx.ALIGN_CENTER)
        titeltje.SetForegroundColour((232,144,30))
        titeltje.SetFont(wx.Font(40, wx.DECORATIVE, wx.NORMAL, wx.NORMAL))
        naam = random.choice(self.bestellers)
        tekst1 = wx.StaticText(self.betaler, -1, str(naam) + " gaat drinken halen",
                                 pos=(5, 3))
        tekst1.SetForegroundColour((255,255,255))
        tekst1.SetFont(wx.Font(11, wx.DECORATIVE, wx.NORMAL, wx.NORMAL))
        tekst2 = wx.StaticText(self.tekst, -1, "Bestelling:",
                                 pos=(5, 3), style=wx.ALIGN_CENTER)
        tekst2.SetForegroundColour((255,255,255))
        tekst2.SetFont(wx.Font(11, wx.DECORATIVE, wx.NORMAL, wx.BOLD))

    def functioneel(self):
        positieteller = 2
        self.naambox = wx.BoxSizer(wx.VERTICAL)
        for x in self.bestellers:
            
            self.naampaneel = wx.Panel(self, -1)
            naamtekst = wx.StaticText(self.naampaneel, -1, x, pos=(2, positieteller))
            naamtekst.SetForegroundColour((255,255,255))
            wx.ComboBox(self.naampaneel, -1, value="", pos=(102, positieteller),
                              choices=self.keuzes, style=0)
            self.naambox.Add(self.naampaneel)
            positieteller =+ 20

    def totaal(self):
        """ 
        """
        totalebox = wx.BoxSizer(wx.VERTICAL)
        totalebox.Add(self.betaler, 1, wx.EXPAND | wx.ALL)
        totalebox.Add(self.tekst, 1, wx.EXPAND | wx.ALL)
        totalebox.Add(self.naambox, 10, wx.EXPAND | wx.ALL)
        """totalebox.Add(self.naam2, 1, wx.EXPAND | wx.ALL)
        totalebox.Add(self.naam3, 1, wx.EXPAND | wx.ALL)
        totalebox.Add(self.naam4, 1, wx.EXPAND | wx.ALL)
        totalebox.Add(self.naam5, 1, wx.EXPAND | wx.ALL)
        totalebox.Add(self.naam6, 1, wx.EXPAND | wx.ALL)
        totalebox.Add(self.naam7, 1, wx.EXPAND | wx.ALL)
        totalebox.Add(self.naam8, 1, wx.EXPAND | wx.ALL)
        totalebox.Add(self.naam9, 1, wx.EXPAND | wx.ALL)
        totalebox.Add(self.naam10, 1, wx.EXPAND | wx.ALL)"""
        
        return totalebox

    def checker(self, event, getal):
        print("gek", getal)
        print(self.drinken_halen_knop.GetValue())
        
    def navigatiebuttons(self):
        """
        """
        self.terug_knop = wx.Button(self, -1, ("Terug"))
        self.prijzenkaart_knop = wx.Button(self, -1, ("Prijzenkaart"))
        self.doorgaan_knop = wx.Button(self, -1, ("Bestelling"))
        navigatiebox = wx.BoxSizer(wx.HORIZONTAL)
        navigatiebox.Add(self.terug_knop, 1, wx.EXPAND | wx.ALL)
        navigatiebox.Add(self.prijzenkaart_knop, 2, wx.EXPAND | wx.ALL)
        navigatiebox.Add(self.doorgaan_knop, 1, wx.EXPAND | wx.ALL)
        return navigatiebox

    def boxen(self, box1, box2):
        """ 
        """
        boxje = wx.BoxSizer(wx.VERTICAL)
        boxje.Add(self.titelpaneel, 1, wx.EXPAND | wx.ALL)
        boxje.Add(box1, 8, wx.EXPAND | wx.ALL)
        boxje.Add(box2, 1, wx.EXPAND | wx.ALL)
        return boxje

class PopUpFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title="Second Frame", size=(250, 150))
        panel = wx.Panel(self)
        self.SetBackgroundColour((46,24,0))
        self.Centre()
        txt = wx.StaticText(panel, label="Uw bestelling is opgenomen", pos = (15, 10),
                            style=wx.ALIGN_CENTER)

        txt.SetForegroundColour((255,255,255))
        #txt.SetFont(wx.Font(11, wx.DECORATIVE, wx.NORMAL, wx.NORMAL))
        self.ok = wx.Button(panel, -1,'Oke', pos=(70, 70), size=(100, 30))
