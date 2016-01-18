"""
Jeroen Kuivenhoven      s1084216

"""

import wx


class Welkomstscherm(wx.Panel):
    def __init__(self, parent, id):
        """ 
        """
        wx.Panel.__init__(self, parent, id)
        paneel1 = wx.Panel(self, id)
        self.teksten(paneel1)
        self.buttons()
        boxje = self.boxen(paneel1)
        self.eindbox = wx.BoxSizer()
        self.eindbox.Add(boxje, 1, wx.EXPAND | wx.ALL)
        self.SetSizer(self.eindbox)
        

    def teksten(self, paneel1):
        """ 
        """
        #paneel1.SetBackgroundColour("Black")
        titeltje = wx.StaticText(paneel1, -1, "Wat voor tijd is het?",
                                 pos=(200, 10), size=(295, -1),
                                 style=wx.ALIGN_CENTER)
        titeltje.SetFont(wx.Font(40, wx.DECORATIVE, wx.NORMAL, wx.NORMAL))

    def buttons(self):
        """ 
        """
        plaatje1=wx.Image("koffiebonen3.bmp", wx.BITMAP_TYPE_BMP).ConvertToBitmap()
        plaatje2=wx.Image("bier3.bmp", wx.BITMAP_TYPE_BMP).ConvertToBitmap()
        self.koffie_knop = wx.BitmapButton(self, -1, plaatje1, size=(450,300))
        self.bier_knop = wx.BitmapButton(self, -1, plaatje2, size=(450,300))
        #paneel2 = wx.Panel(self, id)
        #koffietekst = wx.StaticText(paneel2, -1, "koffie",
        #                         size=(295, -1), style=wx.ALIGN_CENTER)
        #koffietekst.SetFont(wx.Font(30, wx.DECORATIVE, wx.NORMAL, wx.NORMAL))
        #self.stoppen_knop = wx.Button(self, -1, ("koffie"))
        #self.starten_knop = wx.Button(self, -1, ("BIER"))

    def boxen(self, paneel1):
        """ 
        """
        knopboxje = wx.BoxSizer(wx.HORIZONTAL)
        knopboxje.Add(self.koffie_knop, 1, wx.EXPAND | wx.ALL)
        knopboxje.Add(self.bier_knop, 1, wx.EXPAND | wx.ALL)
        boxje = wx.BoxSizer(wx.VERTICAL)
        boxje.Add(paneel1, 1, wx.EXPAND | wx.ALL)
        boxje.Add(knopboxje, 8, wx.EXPAND | wx.ALL)
        return boxje
