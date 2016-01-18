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
        self.prijzen = self.db.getPrijzenlijst()
        self.users = self.db.getUsers()
        #print(self.users)
        #print(self.users[1])
        #print(self.users[1][1])
        
        self.welkompaneel = Welkomstscherm(self, -1)
        self.menupaneel = Menuscherm(self, -1)
        self.menupaneel.Hide()
        self.boxje.Add(self.welkompaneel, 1, wx.EXPAND | wx.ALL)
        self.welkompaneel.koffie_knop.Bind(wx.EVT_BUTTON, lambda evt : self.naarMenu(evt, "koffie"))
        #self.welkompaneel.koffie_knop.Bind(wx.EVT_BUTTON, self.koffie)
        self.welkompaneel.bier_knop.Bind(wx.EVT_BUTTON, lambda evt : self.naarMenu(evt, "bier"))
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
        self.welkompaneel.koffie_knop.Bind(wx.EVT_BUTTON, lambda evt : self.naarMenu(evt, "koffie"))
        #self.welkompaneel.koffie_knop.Bind(wx.EVT_BUTTON, self.koffie)
        self.welkompaneel.bier_knop.Bind(wx.EVT_BUTTON, lambda evt : self.naarMenu(evt, "bier"))
        #self.welkompaneel.bier_knop.Bind(wx.EVT_BUTTON, self.bier)
        self.SetSize((1000, 750))
        self.SetSizer(self.boxje)
        self.Centre()
        self.boxje.Layout()

    def naarMenu(self, event, tijd):
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
        self.menupaneel.drinken_halen_knop.Bind(wx.EVT_BUTTON, lambda evt : self.naarIn_dr_ha_1(evt, tijd))
        self.SetSize((850, 550))
        self.SetSizer(self.boxje)
        self.Centre()
        self.boxje.Layout()

    def naarIn_dr_ha_1(self, event, tijd):
        self.drinken_1_paneel = In_dr_ha_1_scherm(self, -1, self.users)
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
        self.drinken_1_paneel.terug_knop.Bind(wx.EVT_BUTTON, lambda evt : self.naarMenu(evt, tijd))
        self.drinken_1_paneel.random_knop.Bind(wx.EVT_BUTTON, lambda evt : self.naarBestelling(evt, tijd))
        self.drinken_1_paneel.hoogste_s_knop.Bind(wx.EVT_BUTTON, lambda evt : self.naarBestelling(evt, tijd))
        self.SetSize((950, 550))
        self.SetSizer(self.boxje)
        self.Centre()
        self.boxje.Layout()

    def naarBestelling(self, event, tijd):
        dezewillen = self.drinken_1_paneel.bestellers
        if len(dezewillen) > 0:
            self.bestelling_paneel = Be_dr_ha_1_scherm(self, -1, dezewillen, self.prijzen, tijd)
            try:
                self.boxje.Add(self.bestelling_paneel, 1, wx.EXPAND | wx.ALL)
                self.drinken_1_paneel.Hide()
            except wx._core.PyAssertionError:
                pass
            self.bestelling_paneel.Show()
            #self.drinken_1_paneel.drinken_halen_knop.Bind(wx.EVT_RADIOBUTTON, self.naam)
            self.bestelling_paneel.doorgaan_knop.Bind(wx.EVT_BUTTON, lambda evt : self.naarPopUp(evt, tijd))
            self.bestelling_paneel.terug_knop.Bind(wx.EVT_BUTTON, lambda evt : self.naarIn_dr_ha_1(evt, tijd))

            self.SetSize((800, 700))
            self.SetSizer(self.boxje)
            self.Centre()
            self.boxje.Layout()

    def naarPopUp(self, event, tijd):
        self.frame1 = PopUpFrame()
        self.frame1.Show()
        self.frame1.ok.Bind(wx.EVT_BUTTON, lambda evt : self.naarMenu(evt, tijd))

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
