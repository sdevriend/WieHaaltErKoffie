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
        wx.Panel.__init__(self, parent, id)
        self.panelen()
        self.teksten()
        self.functioneel2()
        middenbox = self.totaal()
        navigatiebox = self.navigatiebuttons()
        boxje = self.boxen(middenbox, navigatiebox)
        self.eindbox = wx.BoxSizer()
        self.eindbox.Add(boxje, 1, wx.EXPAND | wx.ALL)
        self.SetSizer(self.eindbox)

    def panelen(self):
        self.titelpaneel = wx.Panel(self, -1)
        self.betaler = wx.Panel(self, -1)
        self.tekst = wx.Panel(self, -1)

    def teksten(self):
        """ 
        """
        titeltje = wx.StaticText(self.titelpaneel, -1, "Drinken halen",
                                 pos=(0, 5), size=(295, -1),
                                 style=wx.ALIGN_CENTER)
        titeltje.SetForegroundColour((232,144,30))
        titeltje.SetFont(wx.Font(40, wx.DECORATIVE, wx.NORMAL, wx.NORMAL))
        self.haler = random.choice(self.bestellers)
        tekst1 = wx.StaticText(self.betaler, -1, str(self.haler) + " gaat drinken halen",
                                 pos=(5, 3))
        tekst1.SetForegroundColour((255,255,255))
        tekst1.SetFont(wx.Font(11, wx.DECORATIVE, wx.NORMAL, wx.NORMAL))
        tekst2 = wx.StaticText(self.tekst, -1, "Bestelling:",
                                 pos=(5, 3), style=wx.ALIGN_CENTER)
        tekst2.SetForegroundColour((255,255,255))
        tekst2.SetFont(wx.Font(11, wx.DECORATIVE, wx.NORMAL, wx.BOLD))
        
        """
    def functioneel(self):
        positieteller = 2
        self.naambox = wx.BoxSizer(wx.VERTICAL)
        self.totalecombo = []
        for x in self.bestellers:
            
            self.naampaneel = wx.Panel(self, -1)
            naamtekst = wx.StaticText(self.naampaneel, -1, x, pos=(2, positieteller))
            naamtekst.SetForegroundColour((255,255,255))
            self.combobox = wx.ComboBox(self.naampaneel, -1, value="", pos=(102, positieteller),
                              choices=self.keuzes, style=0)
            self.totalecombo.append(self.combobox())
            self.naambox.Add(self.naampaneel)
            positieteller =+ 20
        """

    def functioneel2(self):
        self.naambox = wx.BoxSizer(wx.VERTICAL)
        self.totalecombo = []
        try:
            self.naampaneel_1 = wx.Panel(self, -1)
            naamtekst_1 = wx.StaticText(self.naampaneel_1, -1, self.bestellers[0], pos=(2, 22))
            naamtekst_1.SetForegroundColour((255,255,255))
            self.combobox_1 = wx.ComboBox(self.naampaneel_1, -1, value="", pos=(102, 22),
                              choices=self.keuzes, style=0)
            #self.totalecombo.append(self.combobox())
            self.naambox.Add(self.naampaneel_1)
        except IndexError:
            pass
        try:
            self.naampaneel_2 = wx.Panel(self, -1)
            naamtekst_2 = wx.StaticText(self.naampaneel_2, -1, self.bestellers[1], pos=(2, 22))
            naamtekst_2.SetForegroundColour((255,255,255))
            self.combobox_2 = wx.ComboBox(self.naampaneel_2, -1, value="", pos=(102, 22),
                              choices=self.keuzes, style=0)
            #self.totalecombo.append(self.combobox())
            self.naambox.Add(self.naampaneel_2)
        except IndexError:
            pass
        try:
            self.naampaneel_3 = wx.Panel(self, -1)
            naamtekst_3 = wx.StaticText(self.naampaneel_3, -1, self.bestellers[2], pos=(2, 22))
            naamtekst_3.SetForegroundColour((255,255,255))
            self.combobox_3 = wx.ComboBox(self.naampaneel_3, -1, value="", pos=(102, 22),
                              choices=self.keuzes, style=0)
            #self.totalecombo.append(self.combobox())
            self.naambox.Add(self.naampaneel_3)
        except IndexError:
            pass
        try:
            self.naampaneel_4 = wx.Panel(self, -1)
            naamtekst_4 = wx.StaticText(self.naampaneel_4, -1, self.bestellers[3], pos=(2, 22))
            naamtekst_4.SetForegroundColour((255,255,255))
            self.combobox_4 = wx.ComboBox(self.naampaneel_4, -1, value="", pos=(102, 22),
                              choices=self.keuzes, style=0)
            #self.totalecombo.append(self.combobox())
            self.naambox.Add(self.naampaneel_4)
        except IndexError:
            pass
        try:
            self.naampaneel_5 = wx.Panel(self, -1)
            naamtekst_5 = wx.StaticText(self.naampaneel_5, -1, self.bestellers[4], pos=(2, 22))
            naamtekst_5.SetForegroundColour((255,255,255))
            self.combobox_5 = wx.ComboBox(self.naampaneel_5, -1, value="", pos=(102, 22),
                              choices=self.keuzes, style=0)
            #self.totalecombo.append(self.combobox())
            self.naambox.Add(self.naampaneel_5)
        except IndexError:
            pass
        try:
            self.naampaneel_6 = wx.Panel(self, -1)
            naamtekst_6 = wx.StaticText(self.naampaneel_6, -1, self.bestellers[5], pos=(2, 22))
            naamtekst_6.SetForegroundColour((255,255,255))
            self.combobox_6 = wx.ComboBox(self.naampaneel_6, -1, value="", pos=(102, 22),
                              choices=self.keuzes, style=0)
            #self.totalecombo.append(self.combobox())
            self.naambox.Add(self.naampaneel_6)
        except IndexError:
            pass
        try:
            self.naampaneel_7 = wx.Panel(self, -1)
            naamtekst_7 = wx.StaticText(self.naampaneel_7, -1, self.bestellers[6], pos=(2, 22))
            naamtekst_7.SetForegroundColour((255,255,255))
            self.combobox_7 = wx.ComboBox(self.naampaneel_7, -1, value="", pos=(102, 22),
                              choices=self.keuzes, style=0)
            #self.totalecombo.append(self.combobox())
            self.naambox.Add(self.naampaneel_7)
        except IndexError:
            pass
        try:
            self.naampaneel_8 = wx.Panel(self, -1)
            naamtekst_8 = wx.StaticText(self.naampaneel_8, -1, self.bestellers[7], pos=(2, 22))
            naamtekst_8.SetForegroundColour((255,255,255))
            self.combobox_8 = wx.ComboBox(self.naampaneel_8, -1, value="", pos=(102, 22),
                              choices=self.keuzes, style=0)
            #self.totalecombo.append(self.combobox())
            self.naambox.Add(self.naampaneel_8)
        except IndexError:
            pass
        try:
            self.naampaneel_9 = wx.Panel(self, -1)
            naamtekst_9 = wx.StaticText(self.naampaneel_9, -1, self.bestellers[8], pos=(2, 22))
            naamtekst_9.SetForegroundColour((255,255,255))
            self.combobox_9 = wx.ComboBox(self.naampaneel_9, -1, value="", pos=(102, 22),
                              choices=self.keuzes, style=0)
            #self.totalecombo.append(self.combobox())
            self.naambox.Add(self.naampaneel_9)
        except IndexError:
            pass
        try:
            self.naampaneel_10 = wx.Panel(self, -1)
            naamtekst_10 = wx.StaticText(self.naampaneel_10, -1, self.bestellers[9], pos=(2, 22))
            naamtekst_10.SetForegroundColour((255,255,255))
            self.combobox_10 = wx.ComboBox(self.naampaneel_10, -1, value="", pos=(102, 22),
                              choices=self.keuzes, style=0)
            #self.totalecombo.append(self.combobox())
            self.naambox.Add(self.naampaneel_10)
        except IndexError:
            pass
        

    def totaal(self):
        """ 
        """
        totalebox = wx.BoxSizer(wx.VERTICAL)
        totalebox.Add(self.betaler, 1, wx.EXPAND | wx.ALL)
        totalebox.Add(self.tekst, 1, wx.EXPAND | wx.ALL)
        totalebox.Add(self.naambox, 10, wx.EXPAND | wx.ALL)
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
