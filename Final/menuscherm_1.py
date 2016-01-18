"""
Jeroen Kuivenhoven      s1084216

"""

import wx


class Menuscherm(wx.Panel):
    def __init__(self, parent, id):
        """ 
        """
        wx.Panel.__init__(self, parent, id)
        titelpaneel = wx.Panel(self, id)
        self.teksten(titelpaneel)
        menubox = self.menubuttons()
        navigatiebox = self.navigatiebuttons()
        boxje = self.boxen(titelpaneel, menubox, navigatiebox)
        self.eindbox = wx.BoxSizer()
        self.eindbox.Add(boxje, 1, wx.EXPAND | wx.ALL)
        self.SetSizer(self.eindbox)
        #self.paneel.SetBackgroundColour("Black")

    def teksten(self, paneel):
        """ 
        """
        titeltje = wx.StaticText(paneel, -1, "Menu",
                                 pos=(0, 5), size=(295, -1),
                                 style=wx.ALIGN_CENTER)
        titeltje.SetForegroundColour((232,144,30))
        titeltje.SetFont(wx.Font(40, wx.DECORATIVE, wx.NORMAL, wx.NORMAL))

    def menubuttons(self):
        """ 
        """
        
        self.drinken_halen_knop = wx.Button(self, -1, "Drinken halen")
        self.prijzenkaart_knop = wx.Button(self, -1, "Prijzenkaart")
        self.statistiek_knop = wx.Button(self, -1, "Statistiek")
        self.beheer_knop = wx.Button(self, -1, "Beheer")
        menubox_left = wx.BoxSizer(wx.VERTICAL)
        menubox_right = wx.BoxSizer(wx.VERTICAL)
        for x in [self.drinken_halen_knop, self.prijzenkaart_knop]:
            box = self.layoutbox(x)
            menubox_left.Add(box, 1, wx.EXPAND | wx.ALL)
        for x in [self.statistiek_knop, self.beheer_knop]:
            box = self.layoutbox(x)
            menubox_right.Add(box, 1, wx.EXPAND | wx.ALL)
        endbox = wx.BoxSizer(wx.HORIZONTAL)
        endbox.Add(menubox_left, 1, wx.EXPAND | wx.ALL)
        endbox.Add(menubox_right, 1, wx.EXPAND | wx.ALL)
        #menubox.Add(self.drinken_halen_knop, 1, wx.EXPAND | wx.ALL)
        #menubox.Add(self.prijzenkaart_knop, 1, wx.EXPAND | wx.ALL)
        #menubox.Add(self.statistiek_knop, 1, wx.EXPAND | wx.ALL)
        #menubox.Add(self.beheer_knop, 1, wx.EXPAND | wx.ALL)
        return endbox

    def layoutbox(self, button):
        ver_box = wx.BoxSizer(wx.VERTICAL)
        ver_box.Add((wx.Panel(self, -1)), 2, wx.EXPAND | wx.ALL)
        ver_box.Add(button, 3, wx.EXPAND | wx.ALL)
        ver_box.Add((wx.Panel(self, -1)), 2, wx.EXPAND | wx.ALL)
        hor_box = wx.BoxSizer(wx.HORIZONTAL)
        hor_box.Add((wx.Panel(self, -1)), 1, wx.EXPAND | wx.ALL)
        hor_box.Add(ver_box, 2, wx.EXPAND | wx.ALL)
        hor_box.Add((wx.Panel(self, -1)), 1, wx.EXPAND | wx.ALL)
        return hor_box
        
        
        
    def navigatiebuttons(self):
        """
        """
        self.terug_knop = wx.Button(self, -1, ("Terug"))
        self.stop_knop = wx.Button(self, -1, ("Stoppen"))
        navigatiebox = wx.BoxSizer(wx.HORIZONTAL)
        navigatiebox.Add((wx.Panel(self, -1)), 1, wx.EXPAND | wx.ALL)
        navigatiebox.Add(self.terug_knop, 1, wx.EXPAND | wx.ALL)
        navigatiebox.Add((wx.Panel(self, -1)), 1, wx.EXPAND | wx.ALL)
        navigatiebox.Add(self.stop_knop, 1, wx.EXPAND | wx.ALL)
        navigatiebox.Add((wx.Panel(self, -1)), 1, wx.EXPAND | wx.ALL)
        return navigatiebox

    def boxen(self, paneel, box1, box2):
        """ 
        """
        boxje = wx.BoxSizer(wx.VERTICAL)
        boxje.Add(paneel, 1, wx.EXPAND | wx.ALL)
        boxje.Add(box1, 8, wx.EXPAND | wx.ALL)
        boxje.Add(box2, 1, wx.EXPAND | wx.ALL)
        return boxje
