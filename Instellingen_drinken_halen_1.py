"""
Jeroen Kuivenhoven      s1084216

"""

import wx

namen = {1: 'Jeroen', 2: 'Dwin', 3: 'Jolanda', 4: 'Jesse', 5: 'Sebastiaan'}
namen2 = ['Jeroen', 'Dwin', 'Jolanda', 'Jesse', 'Sebastiaan']
hoogsteschulden = 'Jolanda'

class In_dr_ha_1_scherm(wx.Panel):
    def __init__(self, parent, id):
        """ 
        """
        wx.Panel.__init__(self, parent, id)
        titelpaneel = wx.Panel(self, id)
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

    def teksten(self, paneel):
        """ 
        """
        titeltje = wx.StaticText(paneel, -1, "Drinken halen",
                                 pos=(0, 5), size=(295, -1),
                                 style=wx.ALIGN_CENTER)
        titeltje.SetForegroundColour((232,144,30))
        titeltje.SetFont(wx.Font(40, wx.DECORATIVE, wx.NORMAL, wx.NORMAL))
        tekst1 = wx.StaticText(self.tekstpaneel, -1, "Wie willen er een bakkie PLUR?",
                                 pos=(5, 3))
        tekst1.SetForegroundColour((255,255,255))
        tekst1.SetFont(wx.Font(15, wx.DECORATIVE, wx.NORMAL, wx.NORMAL))
        tekst2 = wx.StaticText(self.tekstpaneel2, -1, "Wie gaat er halen?",
                                 pos=(5, 3), style=wx.ALIGN_CENTER)
        tekst2.SetForegroundColour((255,255,255))
        tekst2.SetFont(wx.Font(15, wx.DECORATIVE, wx.NORMAL, wx.NORMAL))
        

    def functioneel1(self):
        """ 
        """
        totalebox = wx.BoxSizer(wx.HORIZONTAL)
        namenbox = wx.BoxSizer(wx.VERTICAL)
        rechterbox = self.functioneel2()
        #namenknoppen = wx.RadioBox(self, -1, choices=namen2)
        namenbox.Add(self.tekstpaneel, 1, wx.EXPAND | wx.ALL)
        knoppenlijst = []
        counter = 1
        for x in namen2:
            self.drinken_halen_knop = wx.CheckBox(self, -1, x,
                                                 pos=(5, 5))
            self.drinken_halen_knop.Bind(wx.EVT_CHECKBOX, lambda evt : self.checker(evt, counter))
            self.drinken_halen_knop.SetForegroundColour((255, 255, 255))
            knoppenlijst.append(self.drinken_halen_knop)
            #self.drinken_halen_knop.SetBackgroundColour((255, 255, 255))
        # self.drinken_halen_knop = wx.Button(self, -1, "Drinken halen")
        
            namenbox.Add(self.drinken_halen_knop, 2, wx.EXPAND | wx.ALL)
            counter += 1
        #namenbox.Add(namenknoppen, 2, wx.EXPAND | wx.ALL)
        totalebox.Add((wx.Panel(self, -1)), 1, wx.EXPAND | wx.ALL)
        totalebox.Add(namenbox, 15, wx.EXPAND | wx.ALL)
        totalebox.Add(rechterbox, 15, wx.EXPAND | wx.ALL)
        print(knoppenlijst)
        
        return totalebox

    def checker(self, event, getal):
        print("gek", getal)
        print(self.drinken_halen_knop.GetValue())

    def functioneel2(self):
        self.random_knop = wx.Button(self, -1, ("Random"))
        self.hoogste_s_knop = wx.Button(self, -1, ("Hoogste schulden"))
        box3 = wx.BoxSizer(wx.VERTICAL)
        box3.Add(self.tekstpaneel2, 1, wx.EXPAND | wx.ALL)
        box4 = wx.BoxSizer(wx.HORIZONTAL)
        box4.Add((wx.Panel(self, -1)), 1, wx.EXPAND | wx.ALL)
        box4.Add(self.random_knop, 5, wx.EXPAND | wx.ALL)
        box4.Add((wx.Panel(self, -1)), 5, wx.EXPAND | wx.ALL)
        box4.Add(self.hoogste_s_knop, 5, wx.EXPAND | wx.ALL)
        box4.Add((wx.Panel(self, -1)), 1, wx.EXPAND | wx.ALL)
        box3.Add(box4, 1, wx.EXPAND | wx.ALL)
        box3.Add((wx.Panel(self, -1)), 5, wx.EXPAND | wx.ALL)
        return box3
        
    def navigatiebuttons(self):
        """
        """
        self.terug_knop = wx.Button(self, -1, ("Terug"))
        self.stop_knop = wx.Button(self, -1, ("Stoppen"))
        navigatiebox = wx.BoxSizer(wx.HORIZONTAL)
        navigatiebox.Add(self.terug_knop, 1, wx.EXPAND | wx.ALL)
        navigatiebox.Add((wx.Panel(self, -1)), 2, wx.EXPAND | wx.ALL)
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
