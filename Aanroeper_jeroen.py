"""
Jeroen Kuivenhoven      s1084216
De aanroeper

"""

from welkomstscherm_1 import Welkomstscherm
from menuscherm_1 import Menuscherm
from Instellingen_drinken_halen_1 import In_dr_ha_1_scherm
from Bestelling_drinken_halen_1 import Be_dr_ha_1_scherm
from Bestelling_drinken_halen_1 import PopUpFrame
from BakkieControlDatabase import BakkieControlDatabase

import wx
import random


class Schermpje(wx.Frame):
    def __init__(self, parent, id, title):
        """ 
        """
        wx.Frame.__init__(self, parent, id, title, style=wx.SYSTEM_MENU |
                          wx.CAPTION | wx.CLIP_CHILDREN, size=(1000, 750))
        self.boxje = wx.BoxSizer()
        self.SetBackgroundColour((46,24,0))
        self.welkom()
        self.SetSizer(self.boxje)
        self.Centre()
        self.Show()

    def welkom(self):
        """ 
        """
        self.db = BakkieControlDatabase()
        prijzen = self.db.getPrijzenlijst()
        users = self.db.getUsers()
        
        self.welkompaneel = Welkomstscherm(self, -1)
        self.menupaneel = Menuscherm(self, -1)
        self.menupaneel.Hide()
        self.boxje.Add(self.welkompaneel, 1, wx.EXPAND | wx.ALL)
        self.welkompaneel.koffie_knop.Bind(wx.EVT_BUTTON, self.naarMenu)
        #self.welkompaneel.koffie_knop.Bind(wx.EVT_BUTTON, self.koffie)
        self.welkompaneel.bier_knop.Bind(wx.EVT_BUTTON, self.naarMenu)
        #self.welkompaneel.bier_knop.Bind(wx.EVT_BUTTON, self.bier)

    def bier(self, event):
        self.SetBackgroundColour((255,255,20))

    def koffie(self, event):
        self.SetBackgroundColour((46,24,0))

    def naarWelkom(self, event):
        self.menupaneel.Hide()
        self.welkompaneel.Hide()
        self.welkompaneel = Welkomstscherm(self, -1)
        self.menupaneel = Menuscherm(self, -1)
        try:
            self.boxje.Add(self.welkompaneel, 1, wx.EXPAND | wx.ALL)
            self.menupaneel.Hide()
        except wx._core.PyAssertionError:
            pass
        #self.menupaneel.Hide()
        #self.boxje.Add(self.welkompaneel, 1, wx.EXPAND | wx.ALL)
        self.welkompaneel.koffie_knop.Bind(wx.EVT_BUTTON, self.naarMenu)
        #self.welkompaneel.koffie_knop.Bind(wx.EVT_BUTTON, self.koffie)
        self.welkompaneel.bier_knop.Bind(wx.EVT_BUTTON, self.naarMenu)
        #self.welkompaneel.bier_knop.Bind(wx.EVT_BUTTON, self.bier)
        self.SetSize((1000, 750))
        self.SetSizer(self.boxje)
        self.Centre()
        self.boxje.Layout()

    def naarMenu(self, event):
        """
        """
        try:
            self.drinken_1_paneel.Hide()
            self.bestelling_paneel.Hide()
            self.frame1.Hide()
        except AttributeError:
            pass
        self.menupaneel = Menuscherm(self, -1)
        try:
            self.boxje.Add(self.menupaneel, 1, wx.EXPAND | wx.ALL)
            self.welkompaneel.Hide()
        except wx._core.PyAssertionError:
            pass
        self.menupaneel.Show()
        self.menupaneel.stop_knop.Bind(wx.EVT_BUTTON, self.onStop)
        self.menupaneel.terug_knop.Bind(wx.EVT_BUTTON, self.naarWelkom)
        self.menupaneel.drinken_halen_knop.Bind(wx.EVT_BUTTON, self.naarIn_dr_ha_1)
        self.SetSize((850, 550))
        self.SetSizer(self.boxje)
        self.Centre()
        self.boxje.Layout()

    def naarIn_dr_ha_1(self, event):
        self.drinken_1_paneel = In_dr_ha_1_scherm(self, -1)
        try:
            self.bestelling_paneel.Hide()
        except AttributeError:
            pass
        try:
            self.boxje.Add(self.drinken_1_paneel, 1, wx.EXPAND | wx.ALL)
            self.menupaneel.Hide()
        except wx._core.PyAssertionError:
            pass
        self.drinken_1_paneel.Show()
        #self.drinken_1_paneel.drinken_halen_knop.Bind(wx.EVT_RADIOBUTTON, self.naam)
        self.drinken_1_paneel.stop_knop.Bind(wx.EVT_BUTTON, self.onStop)
        self.drinken_1_paneel.terug_knop.Bind(wx.EVT_BUTTON, self.naarMenu)
        self.drinken_1_paneel.random_knop.Bind(wx.EVT_BUTTON, self.naarBestelling)
        self.drinken_1_paneel.hoogste_s_knop.Bind(wx.EVT_BUTTON, self.naarBestelling)
        self.SetSize((950, 550))
        self.SetSizer(self.boxje)
        self.Centre()
        self.boxje.Layout()

    def naarBestelling(self, event):
        self.bestelling_paneel = Be_dr_ha_1_scherm(self, -1)
        try:
            self.boxje.Add(self.bestelling_paneel, 1, wx.EXPAND | wx.ALL)
            self.drinken_1_paneel.Hide()
        except wx._core.PyAssertionError:
            pass
        self.bestelling_paneel.Show()
        #self.drinken_1_paneel.drinken_halen_knop.Bind(wx.EVT_RADIOBUTTON, self.naam)
        self.bestelling_paneel.doorgaan_knop.Bind(wx.EVT_BUTTON, self.naarPopUp)
        self.bestelling_paneel.terug_knop.Bind(wx.EVT_BUTTON, self.naarIn_dr_ha_1)

        self.SetSize((800, 700))
        self.SetSizer(self.boxje)
        self.Centre()
        self.boxje.Layout()

    def naarPopUp(self, event):
        self.frame1 = PopUpFrame()
        self.frame1.Show()
        self.frame1.ok.Bind(wx.EVT_BUTTON, self.naarMenu)

    def naam(self, event):
        print("jaja")
        #self.drinken_1_paneel.drinken_halen_knop.

    def onStop(self, event):
        """ 
        """
        self.Destroy()

    

# de klasse schermpje wordt aangeroepen
if __name__ == "__main__":
    app = wx.App()
    Schermpje(None, -1, "Bakkie")
    app.MainLoop()
